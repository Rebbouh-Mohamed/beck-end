# 🛠️ Backend System Overview for Smart Site Management

This repository contains the complete backend architecture responsible for managing and tracking the state of monitored sites. It interfaces with both frontend and MQTT systems, handles data from multiple sensors, supports decision-making with AI models, and ensures secure and intelligent operations.

---

## 📡 System Integration Overview

### 1. **Frontend Communication**
- The backend provides APIs to the frontend to:
  - Visualize real-time data (security, environmental, status alerts).
  - Display system health and component diagnostics.
  - Show AI-generated decisions and historical logs.

### 2. **MQTT Communication**
- The backend connects to MQTT topics to:
  - Receive live sensor data (temperature, humidity, weather, etc.).
  - Monitor alert states and trigger events.
  - Track health status of remote devices and components.

### 3. **Sensor Data Handling**
- Sensor data is continuously received and:
  - Logged into historical databases for future analysis.
  - Used in real-time to assess site conditions.
  - Triggered in case of abnormal values or suspicious activity.

---

## 🧠 AI-Based Decision Making

The backend integrates **three machine learning models** to automate and optimize decision-making:

1. **Reinforcement Learning (RL) Model**:
   - Adjusts cooling and environmental controls based on real-time conditions.
   - Aims to maximize efficiency while maintaining safety thresholds.

2. **XGBoost Model - Frequency**:

3. **XGBoost Model - RB **:
   - Optimizes communication frequency or resource block
---

## 🔐 Security and Alert System

- **Unauthorized Access Detection**:
  - The backend receives alerts from the surveillance system when an unrecognized person is detected.
  - It logs this event and generates a detailed report automatically.

- **LLM Integration for Reporting**:
  - Uses a Large Language Model (LLM) to generate human-readable reports for security events (e.g., unauthorized entries, anomalies).

---

## 🎯 Key Features

- Full state management and data orchestration.
- Real-time communication with frontend (UI) and MQTT broker.
- AI-powered decision systems with reinforcement and tree-based learning.
- Historical tracking and system diagnostics.
- Smart alerting with automatic documentation and reporting.

---

