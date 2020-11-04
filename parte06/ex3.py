#!/usr/bin/env python
import cv2
import numpy as np
import pyaudio
import math
import struct

# Threshold for detected sound
Threshold = 85


# just some parameters for sound input devices - tooked from www
SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2


# Don't know what it is - tooked from the www'
def rms(frame):
    count = len(frame) / swidth
    format = "%dh" % (count)
    shorts = struct.unpack(format, frame)

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n * n
    rms = math.pow(sum_squares / count, 0.5)

    return rms * 1000


def main():
    # Making my sound input device ready
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                              channels=CHANNELS,
                              rate=RATE,
                              input=True,
                              output=True,
                              frames_per_buffer=chunk)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    capture = cv2.VideoCapture(0)

    while True:

        window_name = 'pari_challenge'

        alpha = 0.3 # transparency factor for the green rectangle (technically, for all overlay image)

        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        _, img = capture.read()  # get an image from the camera

        # Detect edges in original image
        edges = cv2.Canny(img, 100, 200)

        # Just to homogenize the shape of edges with img (for adding one on top of the other, later)
        cv2.imwrite('edges.jpg', edges)
        edges = cv2.imread('edges.jpg')

        # Copy the original image to set as background at the end
        output = img.copy()

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            x,y,w,h = faces[0]
            # for (x,y,w,h) in faces[0]:
            # Copy original image with the blue face rectangle
            overlay = img.copy()
            cv2.circle(overlay, (x, y), 50, (0, 0, 255), thickness=10)
            cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Taking off the edges inside the face recognized square
            cv2.rectangle(edges, (x, y), (x + w, y + h), (0, 0, 0), -1)

            # Create green rectangle in overlay image
            cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), -1)

            # Adding the image with the green rectangle but with the alpha factor to the output image
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

        # Turn all the white edges into red
        # edges[np.where((edges != [0, 0, 0]).all(axis=2))] = [0, 0, 255]
        edges[np.where((edges == [255, 255, 255]).all(axis=2))] = [0, 0, 255]

        # Adding the edges to the final (output) image
        cv2.addWeighted(edges, 1, output, 1 - alpha, 0, output)


        # SOUND RECOGNI
        # I dont know what this is - www
        input = stream.read(chunk)
        rms_val = rms(input)
        # print(rms_val)

        if rms_val > Threshold:
            cv2.putText(output, "Someone is speaking".format(alpha),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
        else:
            cv2.putText(output, "Silence".format(alpha),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 3)

        # Display the output
        cv2.imshow(window_name, output)
        # cv2.imshow(window_name, overlay)
        # cv2.imshow('edges', edges)
        # cv2.imshow('edges_red', new)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()