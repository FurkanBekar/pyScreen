import cv2
import numpy as np
import pyautogui
import optparse

def banner():
    print("\n                ________                        _________                ")
    print("_____________  ____  __ \_____________________________  /____________    ")
    print("___  __ \_  / / /_  /_/ /  _ \  ___/  __ \_  ___/  __  /_  _ \_  ___/    ")
    print("__  /_/ /  /_/ /_  _, _//  __/ /__ / /_/ /  /   / /_/ / /  __/  /        ")
    print("_  .___/_\__, / /_/ |_| \___/\___/ \____//_/    \__,_/  \___//_/         ")
    print("/_/     /____/                                                           ")

    print("\n" + "*" * 70)
    print("\t\t  Author  : Furkan BEKAR\n\t\t  Version : 1.0\n\t\t  GitHub  : https://github.com/FurkanBekar")
    print("*" * 70)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-n","--name",dest="name",help="Enter the name of the video to record.",nargs=1)
    parse_object.add_option("-t","--time",dest="time",help="Enter how many seconds the screen recording will take",nargs=1)
    parse_object.add_option("-r","--region",dest="region",help="Saves the desired part of the screen only. top, left, width and height of the region to capture for example (0,0,300,400)",nargs=1)

    return parse_object.parse_args()


def video_settings(file_name):
    screen_size = pyautogui.size()

    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = (screen_size.width, screen_size.height)
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter(file_name, fourcc, 11.0, (SCREEN_SIZE))

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)

    return out

def screen_shots(out, region):
    # make a screenshot
    img = pyautogui.screenshot(region=region)
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the frame
    cv2.imshow("Live", frame)

def closing(out):
    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()

def limitless_record(out, region):
    while True:
        screen_shots(out, region)
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break
    closing(out)


def unlimitless_record(out,time,region):
    for i in range(time*11):
        screen_shots(out, region)

    closing(out)


banner()

(user_input,arguments) = get_user_input()

if user_input.region != None:
    str = user_input.region
    array = str.split(",")
    region = (int(array[0]),int(array[1]),int(array[2]),int(array[3]))

else:
    screen_size = pyautogui.size()
    region = (0, 0, screen_size.width, screen_size.height)

if user_input.time != None:
    time = int(user_input.time)

out = video_settings(user_input.name)

if user_input.time == None:
    limitless_record(out,region)
else:
    unlimitless_record(out,time,region)





