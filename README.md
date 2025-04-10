Sure! Here's a more detailed `README.md` that you can directly copy and paste into your GitHub repo:

---

# 🛰️ Rover Control and Monitoring Dashboard

A real-time web application built using **Streamlit** to **monitor and control a rover** using REST APIs. The dashboard supports **auto and manual driving modes**, shows **live sensor data**, detects **obstacles and RFID tags**, and plots a **real-time path and battery chart** for the rover.

---

## 📸 Preview
![rovermoment](https://github.com/user-attachments/assets/7eba0501-ed6b-4280-884d-5be098bc369b)
![manualmode](https://github.com/user-attachments/assets/b1d05b4f-8a36-440e-9150-17388818a8e3)
![sensor data](https://github.com/user-attachments/assets/78e2765c-6b38-4ca9-88ea-53e1533cb6be)
![battery](https://github.com/user-attachments/assets/5f1a9511-a7d7-40ed-a565-c8f2300f359f)




*Example view showing rover path, battery chart, manual mode and sensor data.*

---

## 🚀 Features

- ✅ Start a rover session and fetch real-time data via APIs  
- 🎮 Manual control (forward, backward, left, right, stop)  
- 🤖 Auto mode: Rover moves randomly and charges when battery is low  
- 🧠 Obstacle and RFID detection mapped on coordinates  
- 📉 Live-updating charts for:
  - Rover path map
  - Battery level over time
- 📡 Displays live sensor data (obstacles, RFID tags, battery, etc.)  
- ☁️ Built with Python, Streamlit, and Matplotlib

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rover-dashboard.git
cd rover-dashboard
```

### 2. Install Required Packages

Make sure Python 3.7+ is installed, then:

```bash
pip install -r requirements.txt
```

<details>
<summary>📦 If you don’t have a <code>requirements.txt</code>, install directly:</summary>

```bash
pip install streamlit requests matplotlib
```

</details>

### 3. Run the App

```bash
streamlit run rover_webapp.py
```

The app will open in your browser at `http://localhost:8501`

---

## ⚙️ Project Structure

```
rover-dashboard/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── preview.png           # Optional: screenshot for GitHub
```

---

## 🔐 API Endpoints Used

- `POST /api/session/start` – Start a rover session  
- `GET /api/rover/status` – Fetch current coordinates and battery  
- `GET /api/rover/sensor-data` – Get latest sensor readings  
- `POST /api/rover/move` – Move rover in a direction  
- `POST /api/rover/stop` – Stop rover movement  
- `POST /api/rover/charge` – Start rover charging  

> 📍 **Note:** APIs are hosted on [https://roverdata2-production.up.railway.app](https://roverdata2-production.up.railway.app)

---

## 🧪 Future Enhancements

- Add map background/grid  
- Replay path history  
- Store logs in a database  
- Add authentication and session management  
- Deploy on cloud (Streamlit Cloud, Heroku, etc.)

---

## 📄 License

This project is licensed under the **MIT License** – meaning you're free to use, modify, and distribute it for personal or commercial use.

---

## 🙌 Credits

Built with 💻 by Ritika @Esdeath4l ,Rekha @uvan dhamain. APIs powered by the Rover backend team.

---
