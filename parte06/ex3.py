#!/usr/bin/env python
import cv2
import numpy as np
import pyaudio
import math
import struct

Threshold = 850

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2

TIMEOUT_LENGTH = 1


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
        # initial setup

        window_name = 'pari_challenge'
        alpha = 0.3
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        _, img = capture.read()  # get an image from the camera

        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite('edges.jpg', edges)
        edges = cv2.imread('edges.jpg')
        output = img.copy()
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            overlay = img.copy()
            cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 255, 0), -1)

            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

        # edges[np.where((edges != [0, 0, 0]).all(axis=2))] = [0, 0, 255]
        edges[np.where((edges == [255, 255, 255]).all(axis=2))] = [0, 0, 255]

        cv2.addWeighted(edges, 1, output, 1 - alpha, 0, output)

        input = stream.read(chunk)
        rms_val = rms(input)
        if rms_val > Threshold:
            cv2.putText(output, "Someone is speaking".format(alpha),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
        else:
            cv2.putText(output, "Silence".format(alpha),
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 3)

        # Display the output
        cv2.imshow(window_name, output)
        # cv2.imshow('edges', edges)
        # cv2.imshow('edges_red', new)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()