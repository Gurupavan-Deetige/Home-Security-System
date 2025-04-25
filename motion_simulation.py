import time
import random
from datetime import datetime

print("🔁 Simulated Home Security System Running...")

try:
    while True:
        motion = random.choice([True, False, False])  # 1 in 3 chance
        if motion:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            print(f"[{timestamp}] ⚠️ Simulated Motion Detected!")
            with open("motion_log.txt", "a") as f:
                f.write(f"{timestamp} - Motion Detected!\n")
            time.sleep(2)
        else:
            time.sleep(1)
except KeyboardInterrupt:
    print("Simulation stopped.")
