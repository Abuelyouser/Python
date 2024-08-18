import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import re
from PIL import Image, ImageChops
import numpy as np
import pyautogui
import keyboard
import shutil
from colorama import init, Fore, Style
from termcolor import colored
import random

######################################################################################################
# positions
# Mouse_position = (1422, 927)
# Mouse position: (286, 133) record button
# Mouse position: (1016, 491) vido click pause/play/maximize/minimize
#######################################################################

# Mouse position: (1505, 67)   markdownload icon for download labs
# Mouse position: (1308, 683)  markdownload "Download"
# Mouse position: (218, 316)   Tasks lab
# Mouse position: (329, 310)   Solutions Lab

#######################################################################
user = 'i.selem@absega.com'
password = "Sky!sthelimit90"
login_link = "https://my.ine.com/login"
print("!! Do not forget to open recorder !!")
print("!! Check the player maximize and play paths .. !!")
course_link = input('Enter the course link: ')
course_name = course_link.split('/')[-1]

# pyautogui references
presentaion_resume_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\resume-presentaiton.png"
no_resume_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\no_resume.png"
maximize_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\maximize.png'
go_refernce_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\go_refernce.png'
out_lines_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\outlines.png'
stop_recorder_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\stop_recorder.png'
vid_minimize_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\vid_minize.png'
driver_noThanks_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\driver_NoThanks.png'
driver_Cookie_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\driver_CookieGotIt.png'
vid_maximize_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\vid_maximize.png'
vid_close_image = r'D:\Abuelyouser\Scripts\INE-downloader\refernces\vid_close_button.png'
vid_play_pause_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\vid_play_button.png"
quiz_exit_button_image = r"D:\Abuelyouser\Scripts\INE-downloader\refernces\quiz_exit_button.png"


#######################################################################################################
def check_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        # If it doesn't exist, create it
        os.mkdir(dir_path)
        print(f"Directory {dir_path} created.")
    else:
        print(f"Directory {dir_path} already exists.")


# locations ####
records_location = r'C:\Users\MohamedAbuelyouser\Videos\Captures'
# D:\Abuelyouser\Courses\INE\Enterprise Defense Administrator Path [eEDA]\SECTION 1 Secure Engineering Fundamentals

# https://my.ine.com/CyberSecurity/courses/f9b1d2d7/introduction-to-security-engineering-change-management
course_path = rf'D:\Abuelyouser\Courses\INE\{course_name}'

# to do check if the course already exist
# os.mkdir(rf'D:\Abuelyouser\Courses\INE\{course_name}')
check_directory_exists(course_path)
base_dir = rf'D:\Abuelyouser\Courses\INE\{course_name}'


def make_directories_tree(dirname):
    module_or_sub = os.path.join(base_dir, dirname)
    if os.path.exists(module_or_sub):
        print(f"{module_or_sub} Already exists!")
        return module_or_sub
    else:
        os.makedirs(module_or_sub, exist_ok=True)
        return module_or_sub


def INE_login():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 "
        "Edg/127.0.0.0")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # navigate to the website
    print("Opening INE ...")
    driver.get(login_link)
    wait = WebDriverWait(driver, 20)
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
    search_input.send_keys(user)
    search_input1 = driver.find_element('xpath', "//input[@placeholder='Password']")
    search_input1.send_keys(password)
    search_btn = driver.find_element('xpath', "//div[@class='ine-form__submit-btn-wrapper "
                                              "auth-form__actions-submit-wrapper "
                                              "auth-form__actions-submit-wrapper--login']")
    time.sleep(10)
    search_btn.click()
    time.sleep(40)
    print("Logged in!")
    return driver


def page_elements():
    sections = driver.find_elements(By.CSS_SELECTOR, 'section.group__topic-wrapper')
    result = []
    module_index = 1
    for section in sections:
        sub_modules = []
        details = []
        selenium_sub_modules_location = []
        # validate show/hide here

        module_name_element = section.find_element(By.CSS_SELECTOR, '.topic__title')
        module_name = f"{module_index}-" + sanitize_path(
            module_name_element.text.strip()) if module_name_element else 'Unknown Module'

        sub_module_wrapper_elements = section.find_elements(By.CSS_SELECTOR, '.level__title-wrapper')
        button_elements = section.find_elements(By.CSS_SELECTOR, '.level__resume')
        sub_module_index = 1
        for wrapper, button in zip(sub_module_wrapper_elements, button_elements):
            p_element = wrapper.find_element(By.CSS_SELECTOR, '.level__title > span')
            try:
                title_detail = wrapper.find_element(By.CSS_SELECTOR, '.level__title__label-detail')
                details.append(title_detail.text)
                #print(f"the detail  are {title_detail.text}")
            except NoSuchElementException:
                details.append("lab")
            if p_element:
                sub_module_text = sanitize_path(p_element.text.strip() + f" {button.text.split()[1]}")
                sub_module_text_numbered = (f"{sub_module_index}-" + sub_module_text).replace(":", '')
                sub_modules.append(sub_module_text_numbered)
                selenium_sub_modules_location.append(wrapper)

            sub_module_index += 1
        # Store the module name and its sub-modules
        result.append({
            'moduleName': module_name,
            'subModules': sub_modules,
            'details': details,
            'subModulesPointer': selenium_sub_modules_location
        })
        module_index += 1

    return result


def take_shot(end, start, destination):
    if os.path.exists(fr"{destination}\{start}.png"):
        print('slides exists .. break!')
        return 'Similar'
    while start < end:
        time.sleep(2)
        # try this on jupyter

        if start == 1:
            print(fr"{destination}\{start}")
            pyautogui.screenshot(fr"{destination}\{start}.png",
                                 region=(30, 100, 1895, 886))
            print("first Screen saved!")
        else:
            pyautogui.screenshot(fr"{destination}\{start}.png",
                                 region=(30, 100, 1895, 886))
            current = fr"{destination}\{start}.png"
            previous = fr"{destination}\{start - 1}.png"
            if images_are_similar(current, previous):
                return f'The screenshots {start} And {start - 1} are Similar.'
            else:
                print(f'The screenshots {start} And {start - 1} are Different.')
        pyautogui.click(x=1504, y=948)
        start += 1


def check_presentation_resume():
    try:
        presentaion_resume_box = pyautogui.locateOnScreen(presentaion_resume_image, grayscale=False, confidence=0.6)
        time.sleep(3)
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
    except pyautogui.ImageNotFoundException:
        print('Image for resume from last slide not found on screen')

    maximize_image_box = pyautogui.locateOnScreen(maximize_image, grayscale=False, confidence=0.6)
    if maximize_image_box:
        print("Maximizing")
        pyautogui.click(maximize_image_box)
        time.sleep(3)
    else:
        print("maximize button not found!")


def images_are_similar(current_image, previous_image, tolerance=5):
    img1 = Image.open(current_image).convert('RGB')
    img2 = Image.open(previous_image).convert('RGB')
    diff = ImageChops.difference(img1, img2)
    diff_array = np.array(diff)
    num_diff_pixels = np.sum(diff_array > tolerance)
    # Check if the number of different pixels is within the acceptable tolerance
    print(f'the diff_pixels are {num_diff_pixels}')
    return num_diff_pixels == 0


def click_show_hide_details():
    try:
        toggle_element = driver.find_elements(By.CSS_SELECTOR, "[class='topic__toggle']")
        for toggle in toggle_element:
            toggle_element_text = toggle.text.strip()
            if toggle_element_text == "Show details":
                actions = ActionChains(driver)
                actions.move_to_element(toggle).click().perform()
                print('clicked on Show details')
    except Exception as e:
        print(f"An error occurred: {e}")


def quiz_exit():
    try:
        quiz_exit_button = driver.find_element(By.XPATH, "//button[contains(@class, 'quiz__exit__btn')]")
        check_then_click(quiz_exit_button)
        #quiz_exit_button.click()
        print('Exiting the quiz')
    except NoSuchElementException:
        print("Quiz not started, Button not found.")
        try:
            driver.execute_script("window.scrollBy(0, 100);")
            quiz_exit_button = pyautogui.locateOnScreen(quiz_exit_button_image, grayscale=False, confidence=0.6)
            if quiz_exit_button:
                pyautogui.click(quiz_exit_button)
                print('clicked on exit quize button using gui')
        except pyautogui.ImageNotFoundException:
            print('quiz exit not found by gui')


def convert_time_to_seconds(time_str):
    pattern = re.compile(r"^((\d+h\s*)?(\d+m\s*)?(\d+s\s*)?)$")
    if not pattern.match(time_str):
        return None
    hours = 0
    minutes = 0
    seconds = 0
    time_parts = time_str.split()
    for part in time_parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
        elif 's' in part:
            seconds = int(part.replace('s', ''))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def vid_record_2(vid_length):
    time.sleep(2)
    quiz_exit()
    # click on the button of screen => x=844,y=1052
    #time.sleep(8)
    # click on the video to pause it, so it can be maximized (maximize by gui if  find element failed)
    # pause the video
    #click_vid_play_pause()
    # this will move to close then move to player then maximize it
    close_after("move")

    #click_vid_max_min()
    # click on the video slide bar => Mouse position: (89, 956)
    pyautogui.click(85, 956, duration=0.5)
    print("open recorder")
    keyboard.send('alt+a')
    time.sleep(1)
    print(f"Now sleeping for {vid_length} seconds")

    # try by clicking on play by coordinates
    # try:
    #     # play the video
    #     click_vid_play_pause()
    #     print('play the video using click_vid_play_pause()')
    #
    # except:
    #     pyautogui.click(101, 1016)
    #     print('clicked on play button using coordinates')

    time.sleep(vid_length - 5)  # time of video
    # pause/play button of the player Mouse position: (98, 1018)
    print('Stopping the video before Minimizing!')
    pyautogui.click(101, 1016)
    # stop recording
    print('stop recording')
    keyboard.send('alt+a')
    try:
        keyboard.send('esc')
        keyboard.send('esc')
        print('Minimizing using esc')
    except Exception as e:
        print(f"An error occurred while exiting video: {e}. Clicking on exit coordinates as a fallback.")
        pyautogui.click(1821, 1020)
        print('Minimizing by click on 1821, 1020')
    time.sleep(3)
    quiz_exit()


def move_recorded_file(destination_dir, vid_name):
    mp4_files = [f for f in os.listdir(records_location) if f.endswith('.mp4')]
    # Check if there's exactly one MP4 file
    if len(mp4_files) == 1:
        # Get the full path of the source file
        source_file = os.path.join(records_location, mp4_files[0])

        # Create the full path of the destination file
        destination_file = os.path.join(source_file, destination_dir)

        # Move and rename the file
        #shutil.move(source_file, destination_file)
        shutil.move(source_file, f"{destination_file}\\{vid_name}.mp4")

        print(f"Moved and renamed {mp4_files[0]} to {destination_file}")
    else:
        print("There is not exactly one MP4 file in the source directory.")


def click_vid_max_min():
    try:
        fullscreen_button = driver.find_element(By.XPATH, '//*[@id="player"]/div[2]/div[12]/div[5]/div[2]/div[16]')
        # //*[@id="player"]/div[2]/div[12]/div[5]/div[2]/div[15] another xpath form the same in course malware
        check_then_click(fullscreen_button)
        # xpath_actions = ActionChains(driver)
        # xpath_actions.move_to_element(fullscreen_button).click().perform()
        print("Fullscreen button clicked successfully using XPATH 16.")
    except NoSuchElementException:
        try:
            fullscreen_button_17 = driver.find_element(By.CSS_SELECTOR,
                                                       '#player > div.jw-wrapper.jw-reset > div.jw-controls.jw-reset > '
                                                       'div.jw-controlbar.jw-reset > div.jw-reset.jw-button-container >'
                                                       'div:nth-child(17)')
            check_then_click(fullscreen_button_17)
            # css_actions = ActionChains(driver)
            # css_actions.move_to_element(fullscreen_button_17).click().perform()
            print("Fullscreen button clicked successfully using CSS 17.")
        except NoSuchElementException:
            print('CSS_Selector not found!')
            try:
                fullscreen_button_16 = driver.find_element(By.CSS_SELECTOR,
                                                           '#player > div.jw-wrapper.jw-reset > '
                                                           'div.jw-controls.jw-reset >'
                                                           'div.jw-controlbar.jw-reset > '
                                                           'div.jw-reset.jw-button-container >'
                                                           'div:nth-child(16)')
                check_then_click(fullscreen_button_16)
                print("Fullscreen button clicked successfully using CSS 16.")
            except Exception as mmm:
                print(f'an Error happened! {str(mmm)}')
                try:
                    close_after("move")
                    pyautogui.doubleClick(duration=0.5)
                    print('using the close_after(move) function then double click to maximize')
                except Exception as ii:
                    print(f'An error happened while maximizing video using move and click {ii}')
        # position of exit full screen Mouse position: (1821, 1020)


def check_then_click(click_element):
    try:
        element_to_check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(click_element))
        element_to_check.click()
    except (TimeoutException, ElementNotInteractableException) as ee:
        print(f"Web Driver wait failed {str(ee)}")
        try:
            click_action = ActionChains(driver)
            click_action.move_to_element(click_element).click().perform()
            print("Element clicked successfully using ActionChains")
        except Exception as nn:
            print(f" Both methods failed (wait and action) the Error:{str(nn)} ")


def click_vid_play_pause():
    play_button = driver.find_element(By.CSS_SELECTOR, '#player .jw-icon-playback')

    check_then_click(play_button)


def sanitize_path(path):
    # Replace invalid characters with an underscore or any other suitable character
    return re.sub(r'[\\:,<>"|?*/]', '', path)


def slide_exit():
    keyboard.press_and_release('esc')
    print("Exiting the Slides! Escape key pressed")
    time.sleep(1)


"""
this function have two arguments 
move >> just move to the close button then move to the player Note) it not click on the player
close >> it close the video by click on the close button
"""


def close_after(cm):
    buttons = driver.find_elements(By.CSS_SELECTOR, '.level__resume')
    for butt in buttons:
        while butt.text == 'Close':
            try:
                # handle error grab photo
                location = pyautogui.locateOnScreen(vid_close_image, grayscale=False, confidence=0.6)
                if location and cm == 'move':
                    center_x = location.left + location.width / 2
                    center_y = location.top + location.height / 2
                    # Move the mouse to the center of the close image
                    pyautogui.moveTo(center_x, center_y, duration=0.5)
                    print(f"Moved mouse to image at coordinates: ({center_x}, {center_y})")
                    # (693, 927) center of screen to maximize
                    pyautogui.moveTo(693, 927, duration=1)
                    #click to pause
                    #pyautogui.click()
                    # maximize the screen
                    try:
                        vid_maxmize = pyautogui.locateOnScreen(vid_maximize_image, grayscale=False, confidence=0.6)
                        if vid_maxmize:
                            print('found vid maximize button')
                            pyautogui.click(vid_maxmize)
                            print('Maximized Player using pyautogui icon')
                    except pyautogui.ImageNotFoundException:
                        print('trying to maximizing the video but the maximizing icon not found on scree!')
                        try:
                            click_vid_max_min()
                        except Exception as ees:
                            print(f'an error happened maximizing click_vid_max_min() {ees}')
                            try:
                                pyautogui.doubleClick(duration=0.5)
                            except Exception as es:
                                print(f'an error happened while maximizing double click {es}')
                    #print('Maximizing Player')
                    # doubel click to maximize screen
                    #pyautogui.doubleClick(duration=0.5)
                    # press f to full screen
                    # keyboard.send('f')
                    # print('video maximized')

                if location and cm == 'click':
                    print("Close video button found")
                    pyautogui.click(location)
            except pyautogui.ImageNotFoundException:
                driver.execute_script("window.scrollBy(0, -50);")


def get_screen_info(screen_index):
    monitors = get_monitors()
    if screen_index < len(monitors):
        monitor = monitors[screen_index]
        return monitor.width, monitor.height, monitor.x, monitor.y
    else:
        raise ValueError("Invalid screen index")


# use this function to make clicks works on any screen Resolution
def relative_click(x, y, screen_index=0):
    # screen_index = 0 if the primary screen
    screen_width, screen_height, screen_x, screen_y = get_screen_info(screen_index)

    x_ratio = x / screen_width
    y_ratio = y / screen_height

    #new_x = screen_width * (original_x / 1920) + screen_x

    new_x = screen_width * x_ratio + screen_x
    new_y = screen_height * y_ratio + screen_y
    return int(new_x), int(new_y)


def organize_videos(folder_path):
    # Create the "videos" directory if it doesn't exist
    videos_dir = os.path.join(folder_path, "videos")
    os.makedirs(videos_dir, exist_ok=True)
    # Dictionary to store folder names and their locations before moving
    folder_locations = {}
    # Iterate through the folders in the specified path
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            # Check if the folder ends with "video"
            if dir_name.endswith("video"):
                video_folder_path = os.path.join(root, dir_name)
                # Find .mp4 files in this folder
                for file_name in os.listdir(video_folder_path):
                    if file_name.endswith(".mp4"):
                        # Move the .mp4 file to the "videos" directory
                        src_file = os.path.join(video_folder_path, file_name)
                        dest_file = os.path.join(videos_dir, file_name)
                        shutil.move(src_file, dest_file)
                        # Save the folder name and its location before moving
                        folder_locations[dir_name] = video_folder_path
                        print(f"Moved {file_name} from {video_folder_path} to {videos_dir}")
    # Return the dictionary of folder names and their original locations
    return folder_locations


def move_videos_back(videos_dir, folder_locations):
    # Iterate through the dictionary of folder names and their original locations
    for folder_name, original_location in folder_locations.items():
        # Check if the folder still exists (it might have been deleted or moved)
        if os.path.exists(original_location):
            # Find the associated .mp4 files in the "videos" directory
            for file_name in os.listdir(videos_dir):
                if file_name.endswith(".mp4"):
                    # Move the .mp4 file back to its original location
                    src_file = os.path.join(videos_dir, file_name)
                    dest_file = os.path.join(original_location, file_name)
                    shutil.move(src_file, dest_file)
                    print(f"Moved {file_name} from {videos_dir} back to {original_location}")


driver = INE_login()
print('Navigating to the Course')
driver.get(course_link)
time.sleep(10)
print('Check if there is anything hide!')
#click_show_hide_details()
print('Getting all webpage elements')
course_page = page_elements()
time.sleep(3)

# The Orchestrator

course_duration = 0
videos_count = 0
slides_count = 0
lab_count = 0
for module in course_page:
    module_tree = make_directories_tree(sanitize_path(module['moduleName']))

    for index, sub_module_name in enumerate(module['subModules']):
        #sub_module_name = sub_module
        title_detail = module['details'][index]
        pointer = module['subModulesPointer'][index]
        directory_tree = make_directories_tree(f"{module_tree}\\{sanitize_path(sub_module_name)}")
        #print(f'this is the Module >>>>>{module}')
        print(f'this is the Sub_module_name >>>> {sub_module_name}')
        # print(f"this is the Title_detail >>>>>>>>> {title_detail}")
        #print(pointer)

        if 'slide' in sub_module_name:
            slides_count += 1
            print(f'this is a {sub_module_name} !')
            time.sleep(2)
            pointer.click()
            time.sleep(5)
            slide_exit()
            close_after('click')
            check_presentation_resume()
            if "Similar" in take_shot(500, 1, directory_tree):
                slide_exit()  # exist the slides by making escape
                time.sleep(10)
            quiz_exit()

        elif 'video' in sub_module_name:
            videos_count += 1
            course_duration = int(course_duration) + int(convert_time_to_seconds(title_detail))
            print(f'this is course duration after adding title_detail {course_duration}')

            print(f'this is {sub_module_name} and duration is {title_detail}')
            full_video_path = os.path.join(directory_tree, sub_module_name + ".mp4")
            # # check if this video name exists or not if exits continue
            if os.path.exists(full_video_path):
                print(f'The {sub_module_name} Video already exists!')
                continue
            print(f'Downloading The video full path: {full_video_path}')

            try:
                actions = ActionChains(driver)
                actions.move_to_element(pointer).click().perform()
                print("Pointer clicked successfully using ActionChains")

            except Exception as e:
                print(f"action chain fialed Error: {str(e)}")
                try:
                    # Wait for the element to be clickable
                    clickable_pointer = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable(pointer))
                    clickable_pointer.click()
                    print("Pointer clicked successfully using WebDriverWait")
                except (TimeoutException, ElementNotInteractableException) as e:
                    print(f"WebDriverWait method failed: {str(e)}")
            time.sleep(5)
            vid_record_2(convert_time_to_seconds(title_detail))
            #vid_record_2(convert_time_to_seconds("20s"))
            print('moving the recorded..')
            time.sleep(5)
            move_recorded_file(directory_tree, sanitize_path(sub_module_name))
            time.sleep(5)
            close_after("click")

        elif 'lab' in sub_module_name:
            lab_count += 1
            print('this is a lab .. ')
            quiz_exit()

        elif 'quiz' in sub_module_name:
            print(f'this is quiz and have {title_detail}')
            time.sleep(2)
            quiz_exit()
        print("############################################################################")

print(f'this is course duration {course_duration}')
course_duration = round(course_duration / 3600, 1)

print(colored("*" * 65, "cyan", attrs=["bold"]))
print(colored("Course details are:", "green", attrs=["bold", "underline"]))
print(f"{Fore.YELLOW}Duration  : {Fore.CYAN}{course_duration}      hours")
print(f"{Fore.YELLOW}Videos    : {Fore.CYAN}{videos_count}       videos")
print(f"{Fore.YELLOW}Slides    : {Fore.CYAN}{slides_count}        slides")
print(f"{Fore.YELLOW}Labs      : {Fore.CYAN}{lab_count}        labs")

print(colored('تمت بحمد الله', 'magenta', attrs=["bold", "blink"]))
print(colored('All is Done!', 'magenta', attrs=["bold", "blink"]))
print(colored("*" * 65, "cyan", attrs=["bold"]))

# To do >> fix the course details by add them in the page element function

# https://my.ine.com/CyberSecurity/courses/f9b1d2d7/introduction-to-security-engineering-change-management done
# https://my.ine.com/CyberSecurity/courses/7f61cf50/actionable-information-from-aggregated-log-data
# https://my.ine.com/CyberSecurity/courses/8a9ffaa1/introduction-to-security-sensors-logging-management    done (but check all videos)
# https://my.ine.com/CyberSecurity/courses/eab31d04/active-directory-penetration-testing                   done
# https://my.ine.com/CyberSecurity/courses/fd66065c/client-side-attacks
# hi Carl how are you? now i'm at MDP and no one deals with and i asked every one in the team to explain
