#!/usr/bin/env python
import cv2


def main():

    # # 2a)
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
    #???? pq q a imagem nao esta fluida?
    #
    # while(1):
    #     capture = cv2.VideoCapture(0)
    #     window_name = 'A5-Ex2'
    #     cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    #     _, image = capture.read()  # get an image from the camera
    #
    #     cv2.imshow(window_name, image)    # add code to show acquired image
    #
    #     if cv2.waitKey(31) & 0xFF == ord('q'):# add code to wait for a key press
    #         break
    #     # cv2.waitKey(1)
    #     # When everything done, release the capture
    #     capture.release()
    #
    # cv2.destroyAllWindows()

    #2b) 2nd try
    # -------------
    # initial setup
    # -------------
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    # -------------
    # Body cicle
    # -------------
    while (True):
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        _, img = capture.read()  # get an image from the camera
        cv2.imshow(window_name, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # -------------
    # When everything done, release the capture
    # -------------
    capture.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()