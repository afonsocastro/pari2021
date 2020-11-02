#!/usr/bin/python

import cv2
import numpy as np
from functools import partial


def click(event, x, y, flags, param, image, color=(0,0,0)):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image,(x-2,y-2),(x+2,y+2),color,-1)


def main():

    # 1a) and 1b)
    # image = cv2.imread('./images/atlascar2.png', 1)
    # cv2.circle(image, center=(image.shape[1] / 2, image.shape[0] / 2), radius=20, thickness=2, color=(255, 0, 0))
    # cv2.putText(image, "PARI", (50, 50), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
    # cv2.imshow('window', image)
    # cv2.waitKey(0)


    # # 1c)
    board = 255 * np.ones(shape=[400, 600, 3], dtype=np.uint8)
    my_click = partial(click, image=board)

    cv2.namedWindow("board")
    cv2.setMouseCallback("board", my_click)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("board", board)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            my_click = partial(click, image=board, color=(0,0,255))
            cv2.namedWindow("board")
            cv2.setMouseCallback("board", my_click)

        elif key == ord("g"):
            my_click = partial(click, image=board, color=(0, 255, 0))
            cv2.namedWindow("board")
            cv2.setMouseCallback("board", my_click)
        elif key == ord("b"):
            my_click = partial(click, image=board, color=(255, 0, 0))
            cv2.namedWindow("board")
            cv2.setMouseCallback("board", my_click)

        elif key == ord("q"):
            break

    # close all open windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
