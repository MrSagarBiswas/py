from time import sleep
import pyautogui as p

sleep(5)

for i in range(1000):
    sleep(0.1)
    p.typewrite("Oi", 1)
    p.press("enter")