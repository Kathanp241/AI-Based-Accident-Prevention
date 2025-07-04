import datetime

def is_in_danger_zone(box, zone):
    x1, y1, x2, y2 = box
    zx1, zy1, zx2, zy2 = zone
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return zx1 <= center_x <= zx2 and zy1 <= center_y <= zy2

def log_event(label):
    with open("logs.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] ALERT: {label} in danger zone\n")