import streamlit as st
import requests
import random
import time
import matplotlib.pyplot as plt

# API Endpoints
SESSION_URL = "https://roverdata2-production.up.railway.app/api/session/start"
ROVER_STATUS_URL = "https://roverdata2-production.up.railway.app/api/rover/status"
SENSOR_DATA_URL = "https://roverdata2-production.up.railway.app/api/rover/sensor-data"
MOVE_ROVER_URL = "https://roverdata2-production.up.railway.app/api/rover/move"
STOP_ROVER_URL = "https://roverdata2-production.up.railway.app/api/rover/stop"
CHARGE_ROVER_URL = "https://roverdata2-production.up.railway.app/api/rover/charge"

# Start session
@st.cache_resource
def start_session():
    response = requests.post(SESSION_URL)
    data = response.json()
    return data.get("session_id")

# Fetch data
def fetch_coordinates(session_id):
    response = requests.get(f"{ROVER_STATUS_URL}?session_id={session_id}")
    data = response.json()
    return data.get("coordinates", [0, 0]), data.get("battery", 100)

def fetch_sensor_data(session_id):
    response = requests.get(f"{SENSOR_DATA_URL}?session_id={session_id}")
    return response.json()

def move_rover(session_id, direction):
    requests.post(f"{MOVE_ROVER_URL}?session_id={session_id}&direction={direction}")

def stop_rover(session_id):
    requests.post(f"{STOP_ROVER_URL}?session_id={session_id}")

def charge_rover(session_id):
    requests.post(f"{CHARGE_ROVER_URL}?session_id={session_id}")

# Initialize session
session_id = start_session()

# App state
if "x" not in st.session_state:
    st.session_state.x = []
    st.session_state.y = []
    st.session_state.battery = []
    st.session_state.time = []
    st.session_state.obstacles = []
    st.session_state.tags = []
    st.session_state.auto_mode = True

# Sidebar controls
st.sidebar.title("Rover Controls")

st.sidebar.markdown("### Mode Selection")
auto_mode = st.sidebar.toggle("Auto Mode", value=st.session_state.auto_mode)
st.session_state.auto_mode = auto_mode

if not auto_mode:
    st.sidebar.markdown("### Manual Drive")
    col1, col2, col3 = st.sidebar.columns(3)
    with col2:
        if st.button("↑ Forward"):
            move_rover(session_id, "forward")
    col1.button("← Left", on_click=lambda: move_rover(session_id, "left"))
    col3.button("→ Right", on_click=lambda: move_rover(session_id, "right"))
    with col2:
        if st.button("↓ Backward"):
            move_rover(session_id, "backward")
    if st.sidebar.button("■ Stop"):
        stop_rover(session_id)

# Main view
st.title("🛰️ Rover Dashboard")

coords, battery = fetch_coordinates(session_id)
sensor_data = fetch_sensor_data(session_id)

x, y = coords
t = time.time()

# Store data
st.session_state.x.append(x)
st.session_state.y.append(y)
st.session_state.battery.append(battery)
st.session_state.time.append(t)

# Detect sensor info
if sensor_data.get("obstacle"):
    st.session_state.obstacles.append((x, y))
if sensor_data.get("rfid", {}).get("tag_detected"):
    st.session_state.tags.append((x, y))

# Auto mode behavior
if auto_mode:
    if battery < 10:
        stop_rover(session_id)
        charge_rover(session_id)
    else:
        move_rover(session_id, random.choice(["forward", "backward", "left", "right"]))

# Rover map
st.subheader("Rover Movement Map")
fig, ax = plt.subplots()
ax.plot(st.session_state.x, st.session_state.y, marker="o", linestyle="-", color="blue", label="Rover Path")
ax.scatter([x], [y], color="red", edgecolors="black", s=100, label="Current Position")
if st.session_state.obstacles:
    obs_x, obs_y = zip(*st.session_state.obstacles)
    ax.scatter(obs_x, obs_y, color="black", marker="x", label="Obstacles")
if st.session_state.tags:
    tag_x, tag_y = zip(*st.session_state.tags)
    ax.scatter(tag_x, tag_y, color="cyan", marker="s", label="RFID Tags")

ax.set_xlim(-250, 250)
ax.set_ylim(-250, 250)
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")
ax.set_title("Rover Real-Time Map")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Battery chart
st.subheader("🔋 Battery Level Over Time")
st.line_chart({"Battery %": st.session_state.battery})

# Sensor data
st.subheader("📡 Sensor Data")
st.json(sensor_data)


