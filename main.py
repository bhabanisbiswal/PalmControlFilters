import cv2
import numpy as np
import mediapipe as mp
import time

# --- Initialize MediaPipe Hands ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# --- Video Capture ---
cap = cv2.VideoCapture(0)

# --- Filter Functions ---
def filter_bw(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

def filter_invert(frame):
    return cv2.bitwise_not(frame)

def filter_thermal(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.applyColorMap(gray, cv2.COLORMAP_JET)

def filter_depth(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.applyColorMap(gray, cv2.COLORMAP_BONE)

filters = {
    'Black & White': filter_bw,
    'Invert': filter_invert,
    'Thermal': filter_thermal,
    'Depth': filter_depth
}
filter_names = list(filters.keys())
current_filter = 0

# --- Pinch Detection Helper ---
def is_pinch(thumb, index, threshold=30):
    """Return True if thumb and index fingertips are close enough."""
    dist = np.hypot(thumb[0] - index[0], thumb[1] - index[1])
    return dist < threshold

# --- Main Loop ---
last_pinch_time = 0
debounce_interval = 0.5  # seconds

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        left_hand_points, right_hand_points = [], []
        pinch_detected = False

        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) == 2:
            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                label = hand_info.classification[0].label
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                index = (int(index_tip.x * w), int(index_tip.y * h))

                if is_pinch(thumb, index):
                    pinch_detected = True

                if label == 'Left':
                    left_hand_points = [thumb, index]
                else:
                    right_hand_points = [thumb, index]

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if left_hand_points and right_hand_points:
                # Create ROI polygon
                pts = np.array([left_hand_points[1], right_hand_points[1],
                                right_hand_points[0], left_hand_points[0]], np.int32)
                cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

                mask = np.zeros((h, w), dtype=np.uint8)
                cv2.fillPoly(mask, [pts], 255)
                mask3 = cv2.merge([mask, mask, mask]) // 255

                # Apply filter
                filter_func = filters[filter_names[current_filter]]
                filtered = filter_func(frame)
                output = (filtered * mask3 + frame * (1 - mask3)).astype(np.uint8)

                # Display filter name
                cv2.putText(output, filter_names[current_filter], (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0,0), 2)
                cv2.imshow('Hand Gesture Filter', output)

                # Change filter on pinch (with debounce)
                if pinch_detected and (time.time() - last_pinch_time > debounce_interval):
                    current_filter = (current_filter + 1) % len(filters)
                    last_pinch_time = time.time()
            else:
                cv2.imshow('Hand Gesture Filter', frame)
        else:
            cv2.imshow('Hand Gesture Filter', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
