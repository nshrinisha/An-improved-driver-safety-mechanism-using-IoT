🚘 **An Improved Driver Safety Mechanism Using IoT** 🌟

Welcome to the Driver Safety Mechanism Project! This project leverages IoT technology and advanced image processing techniques to enhance road safety by detecting and preventing accidents caused by driver negligence, environmental factors, and traffic violations. 💡

---

## 📜 Table of Contents

1. ✨ Introduction
2. 🔧 Features
3. 💻 System Requirements
    - 🛠️ Hardware Requirements
    - 🖥️ Software Requirements
4. ⚙️ Setup Instructions
5. 🚀 Usage
6. 🐾 Challenges
7. 📊 Results
8. 🔮 Future Scope
9. 📚 References

---

## ✨ Introduction

Accidents remain a global concern 🌍, with driver negligence being a significant contributor. This project integrates IoT components and real-time image processing to:

- 🍷 Detect alcohol consumption.
- 😴 Monitor driver drowsiness.
- 🚦 Automatically adjust headlights.
- 🚸 Recognize traffic signboards.
- 🚑 Detect accidents and notify emergency services.

Our mission? To make roads safer for everyone! 🚗✨

---

## 🔧 Features

- **🚨 Alcohol Detection:** Prevents vehicle ignition if alcohol is detected above a threshold.
- **😴 Drowsiness Detection:** Alerts the driver if signs of drowsiness or yawning are identified.
- **💡 Light Beam Control:** Automatically switches between high and low beams to improve visibility and reduce glare.
- **🚸 Sign Board Recognition:** Identifies traffic signs and provides alerts.
- **📍 Accident Detection:** Sends alerts with GPS coordinates to emergency contacts in case of an accident.

---

## 💻 System Requirements

### 🛠️ Hardware Requirements

- Arduino Uno 🎛️
- MQ2 Alcohol Sensor 🍷
- LDR Sensor 💡
- RF Card and Reader 🛂
- Buzzer 🔔
- Webcam 📷
- Vibration Sensor 📟
- Power Source 🔌

### 🖥️ Software Requirements

- Python 🐍: Core programming language.
- OpenCV 📸: For real-time image processing.
- Arduino IDE: To program the Arduino Uno.

---

## ⚙️ Setup Instructions

Follow these steps to set up the project 🔍:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/DriverSafetyIoT.git
    cd DriverSafetyIoT
    ```
2. Install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Upload the Arduino code (`code.c`) using the Arduino IDE.
4. Connect the sensors as illustrated in the circuit diagram (`docs/circuit_diagram.pdf`).
5. Run the Python script to initiate the detection system:
    ```bash
    python test.py
    ```

---

## 🚀 Usage

1. Power on the system 🔌.
2. Execute the Python script to start monitoring 💻.
3. Real-time outputs include:
    - **Alcohol Detection:** 🚷 "Vehicle ignition off."
    - **Drowsiness Alerts:** 😴 "Wake up, driver!"
    - **Light Adjustment:** 💡 "Switching to low beam."
    - **Sign Board Alerts:** 🚸 "School Zone Ahead!"

---

## 🐾 Challenges

### 🚧 Implementation Challenges:

1. **Alcohol Detection:** Fine-tuning the MQ2 sensor for real-time accuracy.
2. **Light Beam Control:** Performance dependent on specific environmental conditions.
3. **Sign Board Detection:** Reliance on Google Maps for accurate mapping and approvals.

---

## 📊 Results

🎉 Key Achievements:

- **🚗 Alcohol Detection:** Prevented ignition when alcohol was detected above threshold levels.
- **😴 Drowsiness Detection:** Achieved 90% accuracy in fatigue detection.
- **💡 Light Beam Adjustment:** Automated transitions between high and low beams for better safety.
- **🚸 Sign Recognition:** Successfully identified school, hospital, and accident zones.

---

## 🔮 Future Scope

### 💡 Proposed Enhancements:

- **Emotional Detection:** Integrating sensors to monitor driver stress or frustration 🧠.
- **Weather Adaptation:** Enhancing system reliability in adverse weather conditions 🌦️.
- **Compact Design:** Miniaturizing components for seamless integration into modern vehicles 🚘.

---

## 📚 References

### 📖 Key Sources:

1. *IoT-Enabled Alcohol Detection System for Road Transportation Safety in Smart City* 📄.
2. *RF-Based Sign Board Detection and Collision Avoidance System* 📡.
3. *Road Accident Prevention System Using Driver's Drowsiness Detection* 😴.

For additional references, see the `References.pdf` file included in this repository.

---
