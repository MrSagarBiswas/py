from time import sleep
import pyautogui as py

sms = input("Write The SMS: ")
times = input("Number of Times to Sent: ")
sleep(5)
for i in range(times):
    sleep(0.1)
    p.typewrite(sms, 0.1)
    p.press("enter")
