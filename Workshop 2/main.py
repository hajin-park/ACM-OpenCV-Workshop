import keyboard as kb
import numpy as np
import cv2
from modules.windowcapture import WindowCapture

sct = WindowCapture()

#   Wait for 's' keypress to start the bot
kb.wait('s')


def main():
    while True:
        #   Reset bounding boxes
        rects = []

        #   Grab a new haystack frame
        haystack = sct.get_screenshot()

        # Your code here

        #   Display the frame
        sct.update(rects)

        # terminate the bot with a "q" keypress
        if kb.is_pressed('q'):
            break


if __name__ == "__main__":
    main()
