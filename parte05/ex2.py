#!/usr/bin/python



import cv2
import argparse
import numpy as np

def main():
    image_rgb=cv2.imread('./images/atlascar2.png',1)
#    Ex 2a e 2b
#     window_name='my_windows'
#
#     image_gray=cv2.cvtColor(image_rgb,cv2.COLOR_RGB2GRAY)
#
#     retval, image_threshold=cv2.threshold(image_gray,120,255,cv2.THRESH_BINARY)
#
#
#     #alternativa2
#     print(type(image_gray))
#     print(image_gray.shape)
#     print(image_gray.dtype)
#     image_np_threshold =image_gray>128
#
#
#     image_np_threshold=image_np_threshold.astype(np.uint8)*255
#
# #Display image
#     window_name='my_window'
#     cv2.imshow(window_name,image_threshold)
#
#     window_name2 = 'my_window2'
#     cv2.imshow(window_name2, image_np_threshold)
#
#     cv2.waitKey(0)


    #ex 2c
    image_b , image_g , image_r = cv2.split(image_rgb) #desempacotamento direto de cada um dos tres canais
    _, image_b_threshold = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    _, image_g_threshold = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    _, image_r_threshold = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)

    # cv2.imshow('my_windowb',image_b_threshold)
    # cv2.imshow('my_windowg',image_g_threshold)
    # cv2.imshow('my_windowr',image_r_threshold)

    image_output=cv2.merge((image_b_threshold,image_g_threshold,image_r_threshold))
    cv2.imshow('my_window_out', image_output)
    cv2.waitKey(0)


    # Ex 2D
if __name__ == '__main__':
    main()