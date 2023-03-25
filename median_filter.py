import numpy as np
from PIL import Image


def median_filter(image, size):
    image = np.array(image)
    w, h, d = image.shape
    pad = size // 2
    padded_img = np.zeros((w + pad*2, h + pad*2, d), dtype=np.uint8)
    padded_img[pad:w+pad, pad:h+pad, :] = image
    filtered_image = np.zeros((w, h, d), dtype=np.uint8)
    for i in range(pad, w+pad):
        for j in range(pad, h+pad):
            for k in range(d):
                window = padded_img[i-pad:i+pad+1, j-pad:j+pad+1, k]
                filtered_image[i-pad, j-pad, k] = np.median(window)
    filtered_image = Image.fromarray(filtered_image)
    return filtered_image


try:
    img = Image.open('pictures/picture_1.jpg')
except FileNotFoundError:
    print("файла не существует")
filtered_img = median_filter(img, 9)
img.show()
filtered_img.show()

