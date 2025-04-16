# ✋ Air Gesture Calculator using MediaPipe

This project demonstrates a step-by-step approach to building a hand gesture-based calculator using a webcam and MediaPipe. The calculator interprets finger counts to perform arithmetic operations like addition and subtraction, with hand gestures representing numbers and operators.

---

## 🔧 Project Overview

### 🔹 Step 1: Webcam Feed (`step_1.py`)
- Open the webcam using OpenCV.
- Flip the camera view for a mirror effect.
- Display the live webcam feed.

### 🔹 Step 2: Hand Tracking (`step_2.py`)
- Integrate MediaPipe's `Hands` module.
- Detect hand landmarks.
- Draw hand connections and landmarks on the webcam feed.

### 🔹 Step 3: Air Calculator (`step_3.py`)
- Use hand landmarks to detect how many fingers are up.
- Interpret finger counts:
  - `1` finger → Append `1`
  - `2` fingers → Append `2`
  - `3` fingers → Append `3`
  - `4` fingers → Append `+`
  - `5` fingers → Append `-`
  - `0` fingers → Evaluate the expression
- Display the ongoing arithmetic expression and its result in real-time.

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install opencv-python mediapipe
```

Or create a `requirements.txt` file with the following:

```
opencv-python
mediapipe
```

---

## Technologies Used
- **Python**
- **OpenCV**
- **MediaPipe**

---

## 🖥️ How to Run

Make sure your webcam is connected and accessible.

Run each step individually:

```bash
python step_1.py  # Step 1: Webcam feed
python step_2.py  # Step 2: Hand tracking
python step_3.py  # Step 3: Air gesture calculator
```

> Press **'q'** to exit any window.

---

## 🧠 How It Works

- MediaPipe's hand landmark detection model identifies 21 points on the hand.
- Finger tip landmarks (IDs: 4, 8, 12, 16, 20) are tracked.
- Logical rules determine if fingers are up/down based on joint positions.
- Count of fingers up is mapped to calculator input:
  - 0 fingers = Evaluate expression
  - 1-3 fingers = Input digits
  - 4-5 fingers = Input operators

---

## 🚀 Possible Extensions

- Add support for more operators: `*`, `/`
- Introduce parentheses and clear functionality
- Integrate voice feedback using `pyttsx3`
- Build a GUI overlay for clearer interaction

---

## 🤝 Contributing

Feel free to fork this repository and open pull requests for new features or improvements. Any contributions are welcome!

---

## 👨‍💻 Author

👤 D SRIVATSAV
GitHub: [@srivatsavdevarakonda](https://github.com/srivatsavdevarakonda)

---

## 📄 License

This project is licensed under the MIT License.
