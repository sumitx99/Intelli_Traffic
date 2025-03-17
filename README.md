# 🚦 Traffic_Management using AI/ML 🚦

<div align="center">
  
![TRAFFIC GIF](https://github.com/user-attachments/assets/6c494c2e-0552-4673-abdf-4778a8aa6044)

</div>
This project(IntelliTraffic) aims to optimize traffic light control using AI and machine learning techniques. The system detects vehicles in real-time using YOLOv8 and dynamically adjusts traffic light timing to reduce congestion and waiting times.🚗🚦

---


## 📌 About the Project
- **🚘 Vehicle Detection**: Uses YOLOv8 to detect cars, motorcycles, buses, and trucks.
- **⏳ Dynamic Traffic Light**: Automatically adjusts traffic signal timing based on the number of detected vehicles.
- **🖥️ Real-time Processing**: Works with live camera feeds for on-the-spot decision-making.
- **⌛ Traffic Signal Timing**:
  - **GREEN**: No vehicles detected.
  - **YELLOW**: Low traffic (1-2 vehicles).
  - **RED**: High traffic (adjusts time dynamically, max 60 sec).

---
## Technologies Used

- Python 🐍

- OpenCV (for image processing)

- Ultralytics YOLOv8 (for object detection)

- NumPy

- Time module (for timing logic)

---

## 🛠 Installation & Setup

### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Project
```sh
python main.py
```

---

## 🚀 Features
- Real-time vehicle detection using YOLOv8.
- Adaptive traffic light control based on vehicle count.
- Countdown timer for signal changes.
- Works with both webcam and video input.

---

## 📷 Demo
https://github.com/user-attachments/assets/1b386e26-6232-49b7-8bc2-5476c1353248

---

## 🔮 Future Enhancements
- 🚦 Implement pedestrian detection.
- 🛣️ Integrate smart IoT-based traffic light control.
- 📊 Generate traffic density analytics.

---

## 📌 License

This project is licensed under the MIT License.
---

🎯 **Contributions are welcome!** Feel free to fork, improve, and create pull requests. 🚀
