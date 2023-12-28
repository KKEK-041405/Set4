import cv2

from matplotlib import pyplot as plt

import imghdr

import os.path, time

image =

cv2.imread('C:/Users/DELL/Pictures/Screenshots/Screenshot.png',cv2.IMREAD_COLOR)

plt.figure(figsize=(15,10))

plt.subplot(3,1,1)

plt.imshow(ima

ge)

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.subplot(3,1,2)

plt.imshow(image)

image1 = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

plt.subplot(3,1,3)

plt.imshow(image1)
plt.imshow(img_rotation)

img_shrinked = cv2.resize(image,(350, 300)

, interpolation = cv2.INTER_AREA)

plt.subplot(514)

plt.title('Shrinked Image')

plt.imshow(img_shrinked)

src_points = np.float32([[0,0], [num_cols-1,0], [0,num_rows-1]])

dst_points = np.float32([[num_cols-1,0], [0,0], [num_cols-1,num_rows-1]])

matrix = cv2.

getAffineTransform(src_points, dst_points)

img_afftran = cv2.warpAffine(image, matrix, (num_cols,num_rows))

plt.subplot(515)

plt.title('Reverse Image')

plt.imshow(img_afftran)
