#!/usr/bin/python

import cv2
import argparse


def main():
    # help context and input args
    parser = argparse.ArgumentParser(description='You will see magic')

    parser.add_argument('-img1', help="insert full path of image1", action="store", type=str)

    parser.add_argument('-img2', help="insert full path of image2", action="store", type=str)

    args = parser.parse_args()
    args = vars(args)
    print(args)

    # image_filename = '/home/ze/Desktop/aulas_20-21/aulas do prof/pari_20-21/Parte05/images/atlascar2.png'
    # image_filename = './images/atlascar2.png'
    # image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    image1 = cv2.imread(args['img1'], 1) # Load an image
    image2 = cv2.imread(args['img2'], 1) # Load an image

    window_name = 'window'
    flip_flop=False

    while True:
        if flip_flop:
            cv2.imshow(window_name, image1)
            flip_flop = False
        else:
            cv2.imshow(window_name, image2)
            flip_flop = True

        cv2.waitKey(3000)


    # cv2.imshow('window', image)  # Display the image
    # cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()