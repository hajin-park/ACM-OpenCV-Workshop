import keyboard as kb
import numpy as np
import cv2
from modules.windowcapture import WindowCapture

sct = WindowCapture()

#   Wait for 's' keypress to start the bot
kb.wait('s')

#   Initialize needle images and needle thresholds
dinosaur_needle = cv2.imread("images/dinosaur.png", cv2.IMREAD_UNCHANGED)
small_cactus_needle = cv2.imread(
    "images/small_cactus.png", cv2.IMREAD_UNCHANGED)
big_cactus_needle = cv2.imread("images/big_cactus.png", cv2.IMREAD_UNCHANGED)
bird_needle = cv2.imread("images/bird.png", cv2.IMREAD_UNCHANGED)

dinosaur_threshold = 0.98
small_cactus_threshold = 0.96
big_cactus_threshold = 0.96
bird_threshold = 0.97

needles = [dinosaur_needle, small_cactus_needle,
           big_cactus_needle, bird_needle]
thresholds = [dinosaur_threshold, small_cactus_threshold,
              big_cactus_threshold, bird_threshold]


def object_detect(haystack, needle, threshold, rects):
    '''Add bounding box rectangles of objects above the specific accuracy threshold'''

    width = needle.shape[1]
    height = needle.shape[0]
    result = cv2.matchTemplate(haystack, needle, cv2.TM_CCORR_NORMED)
    yloc, xloc = np.where(result >= threshold)

    for (x, y) in zip(xloc, yloc):
        rects.append([int(x),
                      int(y),
                      int(width),
                      int(height)])
        rects.append([int(x),
                      int(y),
                      int(width),
                      int(height)])

    return rects


def main():
    while True:
        #   Reset bounding boxes
        rects = []

        #   Grab a new haystack frame
        haystack = sct.get_screenshot()

        #   Template match each needle, gather bounding boxes of objects above the specified threshold
        for needle, threshold in zip(needles, thresholds):
            rects = object_detect(haystack, needle, threshold, rects)

        #   Merge clusters of bounding boxes into single bounding boxers per object
        rects, _ = cv2.groupRectangles(rects, 1, 0.2)

        #   Display the frame
        sct.update(rects)

        # terminate the bot with a "q" keypress
        if kb.is_pressed('q'):
            break


if __name__ == "__main__":
    main()
