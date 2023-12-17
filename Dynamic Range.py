import cv2
import numpy as np
import os

def dynamic_range(img):
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    tinggi, lebar, d = image.shape
    pixel_brightness = []
    for x in range(1, tinggi):
        for y in range(1, lebar):
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

def hitung_pantulan(img):
    image = cv2.imread(img)
    tinggi, lebar, d = image.shape
    count_pantulan = 0
    for i in range(tinggi):
        for j in range(lebar):
            a, b, c = image[i, j]
            if a >= 229 and b >= 229 and c >= 229:
                image[i, j] = 0, 255, 0
                # Counting the specular reflection of the image
                count_pantulan = count_pantulan + 1
    print("{} memiliki pantulan cahaya sebanyak : {}%".format(img, (count_pantulan*100)/(tinggi*lebar)))

Lesi_Hidup = 'static/Dokumentasi Pengujian/Lesi_Hidup/'
Lesi_Mati = 'static/Dokumentasi Pengujian/Lesi_Mati/'
NonLesi_Hidup = 'static/Dokumentasi Pengujian/NonLesi_Hidup/'
NonLesi_Mati = 'static/Dokumentasi Pengujian/NonLesi_Mati/'
print("Ada Lesi, Lampu Hidup")
for file in os.listdir(Lesi_Hidup):
    hitung_pantulan("{}{}".format(Lesi_Hidup, file))
print("Ada Lesi, Lampu Mati")
for file in os.listdir(Lesi_Mati):
    hitung_pantulan("{}{}".format(Lesi_Mati, file))
print("Tidak Ada Lesi, Lampu Hidup")
for file in os.listdir(NonLesi_Hidup):
    hitung_pantulan("{}{}".format(NonLesi_Hidup, file))
print("Tidak Ada Lesi, Lampu Mati")
for file in os.listdir(NonLesi_Mati):
    hitung_pantulan("{}{}".format(NonLesi_Mati, file))
# Destroy all the windows
