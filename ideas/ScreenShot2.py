"""
This the script that worked on the Working lab
"""
import pyautogui
import time
import os

# Path to the image
image_path = r'D:\Abuelyouser\Scripts\ScreenShot\ref.png'

course_name = 'Incident Handling & Response SOC 3.0 Operations & Analytics Course IR-03'
section_name = input("Enter Section Name: ")


# time.sleep(3)
# print(pyautogui.position())
# pyautogui.click(1504,948)
def get_imge_positions(location):
    try:
        location = pyautogui.locateOnScreen(image_path, grayscale=False, confidence=0.5)
        if location:
            print(location)
            return location
        else:
            print("Image not found on screen.")
    except pyautogui.ImageNotFoundException:
        print("Could not locate the image (ImageNotFoundException).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

end = 24
start = 1
os.mkdir(f"ScreenShot/{course_name}/{section_name}")
while start < end:
    pyautogui.screenshot(f"D:\\Abuelyouser\\Scripts\\ScreenShot\\{course_name}\\{section_name}\\{start}.png", region=(30, 100, 1895, 886))
    time.sleep(1)
    pyautogui.click(x=1504, y=948)
    start += 1
