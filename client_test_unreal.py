import zmq
import time
import random
import numpy as np
import cv2

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:12345")
while True:
 frame = socket.recv()
 source = np.load(io.BytesIO(frame))
 cv2.imshow(source)
 cv2.waitKey(1)
