import numpy as np
from PIL import Image

def weighted_median_filter(image, window_size, weights):
    # Получаем размеры изображения
    width, height = image.size
    # Преобразуем изображение в массив numpy
    img_arr = np.asarray(image)
    # Размер окна
    window_half = window_size // 2
    # Создаем выходной массив
    result = np.zeros((height, width, 3), dtype=np.uint8)
    # Проходим по всем пикселям
    for y in range(height):
        for x in range(width):
            # Определяем границы окна
            x_min = max(x - window_half, 0)
            x_max = min(x + window_half + 1, width)
            y_min = max(y - window_half, 0)
            y_max = min(y + window_half + 1, height)
            # Получаем срез окна
            window = img_arr[y_min:y_max, x_min:x_max, :]
            # Распаковываем в одномерный массив
            window_flat = window.reshape((-1, 3))
            # Вычисляем веса пикселей
            pixel_weights = np.prod(np.power(window_flat - img_arr[y, x], weights), axis=1)
            # Находим медиану по взвешенным значениям
            median_index = np.argsort(pixel_weights)[len(pixel_weights) // 2]
            median_color = window_flat[median_index]
            # Записываем медианный цвет в выходной массив
            result[y, x, :] = median_color
    # Создаем выходное изображение с использованием исходной палитры
    result_img = Image.fromarray(result)
    return result_img


weights = [0.1, 0.2, 0.1]

img = Image.open('pictures/asta.jpg')
filtered_img = weighted_median_filter(img, 5, weights)
img.show()
filtered_img.show()
