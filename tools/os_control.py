import pyautogui
import logging

class OSAutomation:
    def __init__(self):
        self.logger = logging.getLogger("TAHER.OS")
        pyautogui.FAILSAFE = True

    def type_text(self, text: str):
        pyautogui.write(text)

    def click_at(self, x: int, y: int):
        pyautogui.click(x, y)

    def press_key(self, key: str):
        pyautogui.press(key)

    def screenshot(self, path: str = "logs/screenshot.png"):
        return pyautogui.screenshot(path)
