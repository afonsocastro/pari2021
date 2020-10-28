#!/usr/bin/python



import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Ler imagens')
    parser.add_argument('-img1', help='path para img1')
    parser.add_argument('-img2', help='path para img2')
    args = parser.parse_args()
    args=vars(args)
    print(args)

    #image_filename = '/images/atlascar2.png'

    img1=cv2.imread(args['img1'],1)
    img2=cv2.imread(args['img2'],1)

    window_name='window'
    flip_flop=False

    while True:
        if flip_flop:
            cv2.imshow(window_name, img1)  # Display the image
            flip_flop=False
        else:
            v2.imshow(window_name, img2)  # Display the image
            flip_flop=True

        cv2.waitKey(3000) # wait for a key press before proceeding

if __name__ == '__main__':
    main()