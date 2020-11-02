#!/usr/bin/env python
import cv2


def main():

    # 2a)
    # # initial setup
    # capture = cv2.VideoCapture(0)
    # window_name = 'A5-Ex2'
    # cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    # _, image = capture.read()  # get an image from the camera
    #
    # cv2.imshow(window_name, image)
    # cv2.waitKey(0)
    #
    # # When everything done, release the capture
    # capture.release()
    # cv2.destroyAllWindows()

    # 2b)
    while(1):
        capture = cv2.VideoCapture(0)
        window_name = 'A5-Ex2'
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        _, image = capture.read()  # get an image from the camera

        cv2.imshow(window_name, image)
        cv2.waitKey(1000)

        # When everything done, release the capture
        capture.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()