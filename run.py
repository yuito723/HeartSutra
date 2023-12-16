"""
cyber-yuito723/HeartSutra
(C) 2023 cyber-yuito723
"""

import pyautogui
import pyperclip
import subprocess
import time

print("３秒後にメモ帳が起動した後、５秒後に写経を開始します。")
time.sleep(3)
subprocess.Popen("notepad.exe")
time.sleep(5)

def display(letter):
    pyperclip.copy(letter)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

a = ["あ", "い", "う"]

for i in a:
    display(i)