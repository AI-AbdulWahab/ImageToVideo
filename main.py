import cv2
import argparse
import os
import time
# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='jpg', help="extension name. default is 'jpg'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Arguments
# dir_path = 'D:\Slosh AI\ImageToVideo\images'
# ext = args['extension']
# output = args['output']
#
# images = []
# for f in os.listdir(dir_path):
#     if f.endswith(ext):
#         images.append(f)
#
# # Determine the width and height from the first image
# image_path = os.path.join(dir_path, images[0])
# frame = cv2.imread(image_path)
# cv2.imshow('video',frame)
# height, width, channels = frame.shape
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
# out = cv2.VideoWriter(output, fourcc, 1.0, (width, height))
#
# for image in images:
#
#     image_path = os.path.join(dir_path, image)
#     frame = cv2.imread(image_path)
#     out.write(frame) # Write out frame to video
#     time.sleep(0.09)
#     cv2.imshow('video', frame)
#
# print("The output video is {}".format(output))
#
# import cv2
# import numpy as np
# import glob
# img_array = []
# for filename in glob.glob("D:\Slosh AI\ImageToVideo\images\*.jpg"):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
import cv2
cam = cv2.VideoCapture(0)

target = 5
counter = 0
while ret:
  if counter == target:
    ret, frame = cam.read()
    # display and stuff
    counter = 0
  else:
    ret = cam.grab()
    counter += 1