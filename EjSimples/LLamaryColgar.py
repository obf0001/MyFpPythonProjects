import time
import pyautogui as robot
import keyboard

time.sleep(3)
while True:
    robot.moveTo(1485,130)
    robot.click()
    time.sleep(1)
    robot.moveTo(1200,300)
    robot.click()
    robot.moveTo(1150,300)
    robot.click()
    time.sleep(1)