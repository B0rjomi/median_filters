import numpy as np
from PIL import Image


def median_filter(image, size):
    temp = []
    pad = size // 2
    final_pic = []
    final_pic = np.zeros((len(image), len(image[0])))
    for i in range(len(image)):
        for j in range(len(image[0])):
            for z in range(size):
                if i + z - pad < 0 or i + z - pad > len(image) - 1:
                    for c in range(size):
                        temp.append(0)
                else:
                    if j + z - pad < 0 or j + pad > len(image[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(size):
                            temp.append(image[i + z - pad][j + k - pad])
            temp.sort()
            final_pic[i][j] = temp[len(temp) // 2]
            temp = []
    return final_pic


def show_res(path):
    global img
    try:
        img = Image.open(path).convert('L')
    except FileNotFoundError:
        print("файла по заданному пути не существует")
    arr = np.array(img)
    filtered_img = median_filter(arr, 7)
    img = Image.fromarray(filtered_img)
    img.show()



