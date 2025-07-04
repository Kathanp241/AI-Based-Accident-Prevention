# AI-Based Accident Prevention in MMS

This system detects human presence in a predefined danger zone and sends a STOP signal to the machine via Arduino when unsafe activity is detected.

## Components
- YOLOv8 model for person detection
- Arduino + relay for machine stop control
- Optional: ArUco marker to detect machine ID/location

## Run the System
```bash
pip install -r requirements.txt
python main.py
```

## To Upload to Arduino
Use Arduino IDE to upload `drill_guard.ino`