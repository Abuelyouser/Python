import pyautogui
import time

# Path to the image
image_path = r'D:\New folder\Python\projects\Screenshot\ref.png'


def get_imge_positions(location):
    try:
        location = pyautogui.locateOnScreen(image_path, grayscale=False)
        if location:
            print(location)
        else:
            print("Image not found on screen.")
    except pyautogui.ImageNotFoundException:
        print("Could not locate the image (ImageNotFoundException).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


end = 152
start = 1
while start < end:
    time.sleep(2)
    pyautogui.click(x=1046, y=648)
    pyautogui.screenshot(f"D:\\New folder\\Python\\projects\\Screenshot\\{start}.png", region=(27, 71, 1313, 625))
    start += 1

#get_imge_positions(image_path)
