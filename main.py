import time
import pyautogui
import subprocess
import cv2
import numpy as np

while True:
    promptAsk = pyautogui.prompt(text='Type Your FUNC Here (MS Rewards Program func) -->', title='MS Rewards Program Prompt Window')
    print(promptAsk)
    if promptAsk == "1":
        break
    elif promptAsk == "0":
        raise SystemExit
    else:
        continue


# Command to run in the Command Prompt
command_1 = r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="Profile 5"'
command_2 = r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="Profile 6"'
command_3 = r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="Profile 1"'
command_4 = r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --profile-directory="Profile 7"'




# A Method To Do The Searches
def searches():
    time.sleep(20)
    pyautogui.hotkey('alt', 't')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(210)

    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)





# A Method To Do The Activities
def activities():

    # This Opens The  Microsoft Rewards Website And Scrolls Down
    pyautogui.moveTo(779, 63)
    pyautogui.click()
    pyautogui.press('backspace')
    pyautogui.write('https://rewards.bing.com/')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.moveTo(940, 653)
    time.sleep(1)
    pyautogui.press('down', presses=13)


    # To Detect The Uncompleted And Task And Click On It

    
    # Load the template image (PNG) you want to detect
    template_path = "C:/Users/cmash/Desktop/Coding/Python/ms_reward/template.png"
    try:
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            raise Exception("Error loading the template image.")
    except Exception as e:
        print(f"Error: {e}")
        return

    # Get the width and height of the template
    template_height, template_width = template.shape

    # Define the threshold for template matching
    threshold = 0.8

    # Set the maximum time to search for the picture (in seconds)
    max_search_time = 40
    start_time = time.time()

    picture_found = False

    while time.time() - start_time < max_search_time:
        # Take a screenshot of the screen
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

        # Perform template matching
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        if loc[0].any():
            pt = (loc[1][0], loc[0][0])
            center_x = pt[0] + template_width // 2
            center_y = pt[1] + template_height // 2

            # Move the mouse pointer to the detected location, click, and then close it
            pyautogui.moveTo(center_x, center_y, duration=0.4)
            pyautogui.click()
            time.sleep(4)
            pyautogui.moveTo(635, 14)
            pyautogui.click()

            picture_found = True
            # Continue the loop if the picture is found
            continue

    if not picture_found:
        print("Picture not found within the time limit.")
        time.sleep(.5)
        pyautogui.press('down', presses=1)

    # Release resources
    cv2.destroyAllWindows()

 










# The Place Where all the FUNCTIONS and PROCESSES work!!! -->

# 1st Profile
subprocess.run(command_1, shell=True)
searches()
time.sleep(5)
activities()

# 2nd Profile
subprocess.run(command_2, shell=True)
searches()
time.sleep(5)
activities()

# 3rd Profile
subprocess.run(command_3, shell=True)
searches()
time.sleep(5)
activities()

# 4th Profile
subprocess.run(command_4, shell=True)
searches()
time.sleep(5)
activities()




# ig it will work :)

pyautogui.alert(text = 'Ms Rewards Done!!!', button = ['Ok', "GGs Bro, Well Done!!!"])
