import pyautogui
import time

#save_point = (x=713, y=636)

time.sleep(3)
print(pyautogui.position())

# pyautogui.moveTo(844,696)
# pyautogui.click()
#

# cancel
##for i in range(200):
##    time.sleep(3)
##    pyautogui.moveTo(958, 694,)
##    pyautogui.click()
##    print(i)

def start():
    while True:
        try:
            res = pyautogui.locateOnScreen("save.PNG", grayscale=True, confidence=0.8)
            if res:
                pyautogui.moveTo(pyautogui.center(res))
                pyautogui.click()
            else:
                print('image not found on screen')
        except pyautogui.ImageNotFoundException:
            print("image not found")
        time.sleep(1)


start()
