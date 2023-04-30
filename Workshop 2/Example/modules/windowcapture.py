from mss import mss
import win32gui as win32
import numpy as np
import cv2


class WindowCapture:
    stopped = True
    screenshot = None
    temp_sct = None
    window_rect = None
    sct_rect = None
    sct = mss()

    def __init__(self):
        window_handle = win32.FindWindow(
            None, "Dinosaur Game - Play Online Free - Google Chrome")
        client_rect = win32.GetClientRect(window_handle)
        window_location = win32.ClientToScreen(
            window_handle, (client_rect[1], client_rect[0]))
        self.win_rect = {
            'left': window_location[0],
            'top': window_location[1],
            'width': client_rect[2],
            'height': client_rect[3]
        }
        self.sct_rect = {
            'left': self.win_rect['left'],
            'top': self.win_rect['top'],
            'width': self.win_rect['width'],
            'height': self.win_rect['height']
        }
        self.sct_x_loc = self.win_rect['left']+self.win_rect['width']
        self.sct_y_loc = self.win_rect['top']

    def get_screenshot(self):
        self.screenshot = np.array(self.sct.grab(self.sct_rect))
        return self.screenshot

    def draw_rectangles(self, rects):
        self.temp_sct = self.screenshot
        for x, y, w, h in rects:
            cv2.rectangle(
                self.temp_sct,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

    def show_window(self, location) -> None:
        cv2.imshow('Game Window', self.temp_sct)
        cv2.moveWindow('Game Window', location[0], location[1])
        cv2.waitKey(1)

    def update(self, rects):
        self.draw_rectangles(rects)
        self.show_window([self.sct_x_loc, self.sct_y_loc])
