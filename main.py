from ultralytics import YOLO # type: ignore
import cv2
import serial # type: ignore
from utils import is_in_danger_zone, log_event

DANGER_ZONE = (100, 100, 400, 300)
CONF_THRESHOLD = 0.5
SERIAL_PORT = 'COM3'

model = YOLO("yolov8n.pt")
arduino = serial.Serial(SERIAL_PORT, 9600, timeout=1)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    status = "SAFE"
    color = (0, 255, 0)
    x1, y1, x2, y2 = DANGER_ZONE
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.putText(frame, "Danger Zone", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    results = model(frame, verbose=False)
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]
            x1b, y1b, x2b, y2b = map(int, box.xyxy[0])

            if conf > CONF_THRESHOLD:
                cv2.rectangle(frame, (x1b, y1b), (x2b, y2b), color, 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1b, y1b - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                if label == "person" and is_in_danger_zone((x1b, y1b, x2b, y2b), DANGER_ZONE):
                    status = "ALERT"
                    color = (0, 0, 255)
                    arduino.write(b"STOP\n")
                    log_event(label)

    cv2.putText(frame, f"Status: {status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow("AI Safety Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()