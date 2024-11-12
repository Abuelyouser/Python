import os.path
import time
import webbrowser
import pyautogui
import keyboard
import json
import pyperclip

"""
pyautogui locations on screen
markdown icon  (1078, 65)
markdown Download icon (924, 563)
"""

save_image = 'icons/save_dialogue.png'
download_markdown = 'icons\download_markdown.png'
markdown_extention = 'icons\markdown_extention.png'
markdownload_path = r"C:\Users\Mohamed\Downloads\obsidian_md"
def click_on(used_image,time_out):
    # Start time
    start_time = time.time()

    # Wait until the image appears or timeout is reached
    while True:
        location = pyautogui.locateOnScreen(used_image, grayscale=False, confidence=0.6)  # Adjust confidence as needed
        if location:
            print("Image found!")
            keyboard.send("ctrl+c")
            pyautogui.click(location)
            break
        elif time.time() - start_time > time_out:
            print("Timeout reached. Image not found.")
            break
        else:
            print("Waiting for image to appear...")
            time.sleep(2)  # Wait for a second before trying again
with open('writeups.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over each item in the 'data' list
article_no = 74
for item in data['data']:
    title = item['Links'][0]['Title']
    link = item['Links'][0]['Link']  # Assuming there is always at least one link
    #authors = ", ".join(item['Authors'])  # Join authors with a comma for display
    bugs = ", ".join(f"#{bug.replace(' ', '_').lower()}" for bug in item['Bugs'])
    publication_date = item['PublicationDate']

    # Print the extracted information
    print(f"writeup Number #{article_no}")
    print(f"Title: {title}")
    #print(f"Authors: {authors}")
    print(f"Bugs: {bugs}")
    #print(f"Publication Date: {publication_date}")

    if "medium.com" in link or "infosecwriteups.com" in link:
        link = f"https://freedium.cfd/{link}"
        print(f'the new link is : {link}')
    print()
    webbrowser.open(link)
    time.sleep(20)
    """
    click on markdown icon plugin
    """
    # pyautogui.click(1078, 65, duration=0.5)
    # time.sleep(10)
    #click_on(markdown_extention,"20")

    """
    inject hashtags
    """
    #position: (744, 200)
    # pyautogui.click(744,200)
    # pyautogui.write(bugs)


    """
    click on Download markdown
    """
    time.sleep(3)
    #pyautogui.click(924, 563, duration=0.5)
    #click_on(download_markdown,"20")
    keyboard.send("ctrl+d")

    """
    click on save dialogue
    """
    time.sleep(10)
    # try:
    #     save_image_box = pyautogui.locateOnScreen(save_image, grayscale=False, confidence=0.6)
    #     if save_image_box:
    #         # copy writeup name
    #         keyboard.send('ctrl+c')
    #         time.sleep(0.5)
    #         pyautogui.click(save_image_box)
    # except pyautogui.ImageNotFoundException:
    #     print('Save image not found on screen')
    #click_on(save_image,"15")
    # position: (511, 446)
    time.sleep(3)
    keyboard.send('ctrl+c')
    time.sleep(3)
    pyautogui.click(717,670) #on chrome
    # #pyautogui.click(624, 703) # for firefox
    time.sleep(5)
    keyboard.send("ctrl+w")

    """
    insert hashtags
    """
    file_path = os.path.join(markdownload_path,pyperclip.paste()+".md")
    # Open the file in read mode to read its content
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
        # Insert the hashtags at the beginning
        content.insert(0, f"{bugs}\n")
        # Open the file in write mode to overwrite with the modified content
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(content)
        print("Hashtags added to the first line.")
    except FileNotFoundError:
        print("file not found!")
    article_no += 1
    print("********************************************************************")
    time.sleep(3)


# to do make it with cordinations not images

