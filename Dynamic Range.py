import cv2
import numpy as np
import os

#calculate the dynamic range of an image
def dynamic_range(img):
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    height, width, d = image.shape
    pixel_brightness = []
    #Find pixel brightness for each pixel
    for x in range(1, height):
        for y in range(1, weight):
            try:
                pixel = image[x, y]
                R, G, B = pixel
                brightness = sum([R, G, B]) / 3
                if(brightness==0):
                   brightness=1
                pixel_brightness.append(brightness)
            except IndexError:
                pass
    din_range = round(np.log2(max(pixel_brightness)) - np.log2(min(pixel_brightness)), 2)
    return din_range

def denoise(img):
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    denoised_image  = cv2.medianBlur(image, 5)
    return denoised_image

#calculate the percentage of specular reflection on an image
def calculate_reflection(img):
    image = cv2.imread(img)
    height, width, d = image.shape
    count_reflection = 0
    for i in range(height):
        for j in range(width):
            a, b, c = image[i, j]
            if a >= 229 and b >= 229 and c >= 229:
                image[i, j] = 0, 255, 0
                # Counting the specular reflection of the image
                count_reflection = count_reflection + 1
    return (count_pantulan*100)/(height*width)
