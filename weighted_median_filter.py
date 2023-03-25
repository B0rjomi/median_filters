import numpy as np
from PIL import Image


def weighted_median_filter(image, kernel_size, weights):
    img = np.array(image)
    filtered_img = np.zeros_like(img)
    # находим половину размера ядра
    pad = kernel_size // 2
    # проходим по каждому пикселю в изображении
    for i in range(pad, img.shape[0] - pad):
        for j in range(pad, img.shape[1] - pad):
            # выделяем окно размера ядра вокруг текущего пикселя
            window = img[i - pad:i + pad + 1, j - pad:j + pad + 1]
            # сортируем значения пикселей в окне
            sorted_pixels = np.sort(window.reshape(-1))
            # вычисляем взвешенную медиану
            cumsum = np.cumsum(sorted_pixels)
            med_index = np.searchsorted(cumsum, 0.5 * np.sum(weights))
            median_value = sorted_pixels[med_index]
            # сохраняем медианное значение в массиве с результатом
            filtered_img[i, j] = median_value
    filtered_img = Image.fromarray(filtered_img)
    return filtered_img


img = Image.open('pictures/asta.jpg')

weights = np.array([[1, 1, 1, 1, 1],
[1, 2, 2, 2, 1],
[1, 2, 3, 2, 1],
[1, 2, 2, 2, 1],
[1, 1, 1, 1, 1]])
filtered_img = weighted_median_filter(img, 5, weights)

img.show()
filtered_img.show()