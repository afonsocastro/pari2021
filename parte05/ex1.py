#!/usr/bin/python

import cv2

def main():

    image_filename = '/home/ze/Desktop/aulas_20-21/aulas do prof/pari_20-21/Parte05/images/atlascar2.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()