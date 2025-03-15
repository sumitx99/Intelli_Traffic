import cv2
import time
from ultralytics import YOLO
from traffic_signal import adjust_signal_time

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Traffic signal variables
traffic_light = "GREEN"
time_remaining = 0  # Countdown for traffic light
last_update_time = time.time()  # Track last update


def adjust_signal_time(vehicle_count):
    """Update traffic light status and timer based on vehicle count."""
    global traffic_light, time_remaining, last_update_time
    
    if vehicle_count == 0:
        traffic_light = "GREEN"
        time_remaining = 0  
    elif vehicle_count < 3:
        traffic_light = "YELLOW"
        time_remaining = 10  # Example: 10 sec for low traffic
    else:
        traffic_light = "RED"
        time_remaining = min(60, vehicle_count * 5)  # Max 60 sec

    last_update_time = time.time()  # Reset timer


# Open webcam (or use video file)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform vehicle detection
    results = model(frame)

    # Count vehicles
    vehicle_count = 0
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])

            if cls in [2, 3, 5, 7]:  # Car, Motorcycle, Bus, Truck
                vehicle_count += 1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # ✅ Update traffic light and timer logic at intervals
    if time.time() - last_update_time >= 1 and time_remaining > 0:
        time_remaining -= 1
        last_update_time = time.time()

    if time_remaining == 0:  # Re-evaluate traffic light when time is up
        adjust_signal_time(vehicle_count)

    # ✅ Show correct traffic light status
    light_color = (0, 255, 0) if traffic_light == "GREEN" else (0, 255, 255) if traffic_light == "YELLOW" else (0, 0, 255)
    cv2.putText(frame, f"Light: {traffic_light}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, light_color, 2)
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Time: {time_remaining} sec", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show output
    cv2.imshow("Traffic Management", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
