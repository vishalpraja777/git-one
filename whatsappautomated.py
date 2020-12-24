import pyautogui as pg
import time
import pywhatkit
for i in range(10):
    pywhatkit.sendwhatmsg('+919980469341','Hello',11,56.0+(i/3),wait_time=10,print_waitTime=True)
    time.sleep(2)
    pg.hotkey('ctrl' , 'w')