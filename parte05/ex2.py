#!/usr/bin/python



import cv2
import argparse

def main():
    image_rgb=cv2.imread('./images/atlascar2.png',1)
    window_name='my_windows'

    image_gray=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)

    retval, image_threshold=cv2.threshold(image_gray,120,255,cv2.THRESH_BINARY)


    #alternativa2
    print(type(image_gray))


    cv2.imshow(window_name,image_threshold)
    cv2.waitKey(0)



if __name__ == '__main__':
    main()