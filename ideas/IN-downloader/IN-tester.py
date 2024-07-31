import os
import json
import pyautogui
import time
import keyboard


the_course_link = ('https://my.ine.com/CyberSecurity/courses/5c7838a9/incident-handling-response-soc-30-operations'
                   '-analytics')
course_name = 'incident-handling-response-soc-30-operations-analytics'

presentaion_resume_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\resume-presentaiton.png"
no_resume_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\no_resume.png"
maximize_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\maximize.png'
go_refernce_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\go_refernce.png'
out_lines_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\outlines.png'
xpath_for_pageNumber = ("//span[(starts-with(text(), 'p') or starts-with(text(), '|')) and (contains(text(), "
                        "'0') or contains(text(), '1') or contains(text(), '2') or contains(text(), '3') or contains("
                        "text(), '4') or contains(text(), '5') or contains(text(), '6') or contains(text(), "
                        "'7') or contains(text(), '8') or contains(text(), '9'))]")
orXPATH_for_pageNumber = "//span[starts-with(text(), 'p') or starts-with(text(), '|')]"

# positions
# Mouse_position = (1422, 927)
# Mouse position: (286, 133) record button
# Mouse position: (1016, 491) vido click pause/play/maximize/minimize



# os.mkdir(rf'D:\Abuelyouser\Courses\INE\{course_name}')
# base_dir = rf'D:\Abuelyouser\Courses\INE\{course_name}'
# json_file_path = r"D:\Abuelyouser\Scripts\INE-downloader\modules_and_submodules.json"
# with open(json_file_path, 'r') as f:
#     modules_sub_modules_json = json.load(f)
#
# for module_index, module in enumerate(modules_sub_modules_json, start=1):
#     module_name = f"{module_index:02d} - {module['moduleName']}"
#     module_dir = os.path.join(base_dir, module_name)
#     os.makedirs(module_dir, exist_ok=True)
#     for sub_index, sub_module in enumerate(module['subModules'], start=1):
#         sub_module_name = f"{sub_index:02d} - {sub_module}"
#         sub_module_dir = os.path.join(module_dir, sub_module_name)
#         os.makedirs(sub_module_dir, exist_ok=True)
# print("Directories created successfully.")

time.sleep(5)


def take_shot(end,start):
    while start < end:
        pyautogui.screenshot(f"D:\\Abuelyouser\\Scripts\\INE-downloader\\test-shots\\{start}.png",
                             region=(30, 100, 1895, 886))
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        start += 1

def video_recorder(vid_length):
    # first pause the video by click
    #pyautogui.click(1016, 491)
    time.sleep(3)
    #pyautogui.click(1016, 491)
    # maximize by double click
    pyautogui.doubleClick(1016, 491)
    # first pause the video by click
    time.sleep(3)
    pyautogui.click(1016, 491)
    # open windows recorder
    keyboard.send('windows+g')
    # # click on recorder to record
    pyautogui.click(286, 133)
    time.sleep(vid_length)

    # # then click play video
    # pyautogui.click(1016, 491)
    # time.sleep(vid_length)
    # # save the video
    # # double click to exit video
    # pyautogui.doubleClick(1016, 491)


def check_presentation_resume():
    presentaion_resume_box = pyautogui.locateOnScreen(presentaion_resume_image, grayscale=False, confidence=0.6)
    time.sleep(5)
    if presentaion_resume_box:
        print('presentaion box found')
        no_button_location = pyautogui.locateCenterOnScreen(no_resume_image, region=presentaion_resume_box,
                                                            confidence=0.6)
        if no_button_location:
            pyautogui.click(no_button_location)
            print('clicked no resume!')
            time.sleep(5)
        else:
            print("the button no found!")
    else:
        print('the box not found')
    maximize_image_box = pyautogui.locateOnScreen(maximize_image, grayscale=False, confidence=0.6)
    if maximize_image_box:
        print("Maximizing")
        pyautogui.click(maximize_image_box)
        time.sleep(5)
        take_shot(2,1)
        pyautogui.click(x=1504, y=948)
        pyautogui.click(x=1504, y=948)
        pyautogui.click(x=1504, y=948)
        time.sleep(5)
        #take screenshot
    else:
        print("maximize button not found!")
    refernce_box = pyautogui.locateOnScreen(go_refernce_image, grayscale=False, confidence=0.6)
    if refernce_box:
        print('go to reference')
        refernce_center = pyautogui.center(refernce_box)
        pyautogui.click(refernce_center)
        time.sleep(3)
        # make them click until the same previous image
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
        time.sleep(1)
        pyautogui.click(x=1504, y=948)
    else:
        print("reference not found!")
    # get last page number then go to outlines
    out_lines_box = pyautogui.locateOnScreen(out_lines_image,grayscale=False, confidence=0.6)
    if out_lines_box:
        print("go back to outlines")
        pyautogui.click(out_lines_box)
        time.sleep(3)
        take_shot(10,2)

        # from here the take screenshots


#check_presentation_resume()

#pyautogui.press("esc")

#video_recorder(15)

time.sleep(2)
keyboard.send('windows+g')
time.sleep(5)
# # click on recorder to record
pyautogui.click(286, 133)
time.sleep(400)
# try:
#     while True:
#         x, y = pyautogui.position()
#         print(f"Mouse position: ({x}, {y})")
#         time.sleep(5)  # Adjust the delay as needed to control the frequency of updates
# except KeyboardInterrupt:
#     print("Program terminated.")

