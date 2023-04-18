import pyautogui
import time
import random
from datetime import datetime, timedelta

pyautogui.FAILSAFE = False

while True:
    interval = random.randint(30, 180)
    end_time = datetime.now() + timedelta(seconds=interval)
    while datetime.now() < end_time:
        remaining_time = (end_time - datetime.now()).seconds
        print(f" In {remaining_time}s    ", end="\r")
        time.sleep(1)

    print(f" Wait...", end="\r")
    for i in range(0, 200):
        pyautogui.moveTo(0, i * 4)
    pyautogui.moveTo(1, 1)
    for i in range(0, 3):
        pyautogui.press("shift")

    print(f"+{interval}s to {format(datetime.now().time())}")
