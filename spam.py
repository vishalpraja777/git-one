import pyautogui, time
time.sleep(5)
f = open("text", 'r')
for word in f:
    pyautogui.typewrite(word)
    # time.sleep(1)
    pyautogui.press("enter")
    print('Done')