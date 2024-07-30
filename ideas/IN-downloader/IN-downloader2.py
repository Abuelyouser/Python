import pyautogui
import time

#course_name = input("Enter course name: ")

JS_inject_ref = r"D:\New folder\Python\projects\Screenshot\INE-downloader\refernces\JS_injector.png"
time.sleep(5)
try:
    # Locate the icon and get its position
    JS_location = pyautogui.locateOnScreen(JS_inject_ref, grayscale=False)

    if JS_location is not None:
        # Get the center coordinates of the icon
        icon_center = pyautogui.center(JS_location)
        # Move the mouse to the icon and click it
        pyautogui.click(icon_center)
        print("Icon clicked successfully!")
    else:
        print("Icon not found on the screen.")
finally:
    print('not worked!')
# except Exception as e:
#     print(f"An error occurred: {e}")
