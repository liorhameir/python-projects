"""
Created by Lior Hameir
"""

import os
import time
from typing import Callable
try:
    import schedule
    import pyautogui
except ModuleNotFoundError as err:
    print(f"type: 'py -m pip install {err.name}' and run again\n")


KILL_MEETING = "taskkill /f /im  zoom.exe"
Minutes_TO_SECONDS = 60


def lesson(meeting_id: str, password: str, total_time_in_minutes: int) -> Callable:

    def join_zoom_meeting() -> None:
        # open zoom
        time.sleep(0.5)
        pyautogui.press('esc', interval=0.2)
        time.sleep(0.2)
        pyautogui.press('win', interval=0.5)
        pyautogui.write('zoom')
        time.sleep(2)
        pyautogui.press('enter', interval=0.5)
        # open screen
        location = pyautogui.locateOnScreen("joinM.png")
        button_x, button_y = pyautogui.center(location)
        pyautogui.click(button_x, button_y, interval=1)
        time.sleep(0.2)
        pyautogui.typewrite(meeting_id)
        location = pyautogui.locateOnScreen("videooff.png")
        time.sleep(0.2)
        button_x, button_y = pyautogui.center(location)
        pyautogui.click(button_x, button_y)
        time.sleep(0.2)
        location = pyautogui.locateOnScreen("join.png")
        button_x, button_y = pyautogui.center(location)
        pyautogui.click(button_x, button_y)
        time.sleep(1)
        pyautogui.typewrite(password)
        pyautogui.press('enter', interval=5)


        time.sleep(total_time_in_minutes * Minutes_TO_SECONDS)
        os.system(KILL_MEETING)
    return join_zoom_meeting


"""
specify your meetings dates and times like this:

schedule.every().sunday.at("12:00").do(lesson(
    meeting_id=111 1111 1111,
    password=5ch5h,
    total_time_in_minutes=100))
    
schedule.every().tuesday.at("14:00").do(lesson(
    meeting_id="222 2222 2222",
    password="1hg2h",
    total_time_in_minutes=30))
"""

while True:
    schedule.run_pending()
    time.sleep(1)
