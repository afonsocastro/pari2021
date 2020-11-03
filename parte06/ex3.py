#!/usr/bin/env python
import cv2
import numpy as np
import copy


def main():

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    capture = cv2.VideoCapture(0)

    while (True):
        # initial setup

        window_name = 'pari_challenge'
        window_name2 = 'teste'
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        _, img = capture.read()  # get an image from the camera

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), -1)

            # esverdeamento da face
            roi=img[y:y+h,x:x+w] #nao fazendo copia, modifico diretamente esta zona da imagem original
            roi[:, :, 0] = 0
            roi[:, :, 2] = 0

            # cv2.imshow(window_name2, roi)


            #deteccao de arestas


        # Display the output
        cv2.imshow(window_name,img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()