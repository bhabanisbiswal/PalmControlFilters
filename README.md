---

# ✋ PalmControlFilters

This project applies **real-time video filters** using **hand gestures** 🖐️ with **OpenCV** 🎥 and **MediaPipe** 🤖.
By performing a **pinch gesture** with your thumb and index finger, you can cycle through filters like **Black & White**, **Invert**, **Thermal**, and **Depth**, which are applied dynamically inside the region formed by your hands.

---

## ✨ Features

* 🎥 **Real-time hand gesture detection** using webcam.
* 🖐️ Control filters with simple **pinch gestures**.
* 🎨 Multiple filters – Black & White, Invert, Thermal, Depth.
* 🔲 Filters applied **only inside hand regions** for dynamic visuals.
* 🖥 Works on any system with a camera.

---

## 🛠 Tech Stack

* 🐍 **Python**
* 🎥 **OpenCV** – Real-time video capture & filter processing.
* 🤖 **MediaPipe** – Hand tracking and gesture detection.
* 🔢 **NumPy** – Array manipulation & pixel processing.

---

## 📂 Project Structure

```
PalmControlFilters/
│── main.py          # Main script for hand gesture filters
│── README.md        # Project documentation
│── .gitignore       # Ignored files
```

---

## ⚙ How It Works

1️⃣ **Hand Detection**

* Uses **MediaPipe** to detect hand landmarks in real-time.

2️⃣ **Gesture Recognition**

* Recognizes **pinch gesture** (thumb + index finger).

3️⃣ **Filter Switching**

* Cycles through filters each time the gesture is detected.

4️⃣ **Filter Application**

* Applies the selected filter **only within the hand region** for dynamic effects.

---

## 📥 Installation

1. 📂 Clone the repository:

```bash
git clone https://github.com/your-username/PalmControlFilters.git
```

2. 📁 Navigate into the folder:

```bash
cd PalmControlFilters
```

3. 📦 Install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

4. ▶ Run the project:

```bash
python main.py
```

---

## 🚀 Usage

* 🎥 Ensure your webcam is connected.
* ✋ Perform a **pinch gesture** to switch filters.
* 🎨 Watch filters apply dynamically inside your hand region.
* ❌ Press `Q` to quit.

---

## 📸 Demo

📷 *\[Add screenshots or GIFs of your project output here]*

---

## 🔮 Future Improvements

* 🖼 Add more filter effects (Cartoon, Blur, Sepia, etc.).
* 🧠 Integrate with AI-based filters (style transfer).
* 🌐 Deploy as a web app using Flask or Streamlit.

---

## 👤 Author

**Bhabani S Biswal** – Python & AI/ML Developer

📧 Email: [bhabanibiswalb17@gmail.com](mailto:bhabanibiswalb17@gmail.com)
🔗 GitHub: [Bhabani S Biswal](https://github.com/bhabanisbiswal)

---
