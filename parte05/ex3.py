#!/usr/bin/python

import cv2
import argparse
import numpy as np
from functools import partial


# Global variables
# window_name = 'window - Ex3a'
# image_gray = None


def onTrackbar(threshold, image_gray, window_name):

    _, i_bin = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, i_bin)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    window_name = 'window - Ex3a'

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    # global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    trackbar_name = 'Threshold'

    myOnTrackBar = partial(onTrackbar, image_gray=image_gray, window_name=window_name)

    # cv2.createTrackbar(trackbar_name, window_name, 0, 255, onTrackbar)
    cv2.createTrackbar(trackbar_name, window_name, 0, 255, myOnTrackBar)

    # onTrackbar(128)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()