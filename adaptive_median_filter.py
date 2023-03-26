from PIL import Image
import numpy as np


def level_A(z_min, z_med, z_max, z_xy, S_xy, S_max):
    if (z_min < z_med < z_max):
        return level_B(z_min, z_med, z_max, z_xy, S_xy, S_max)
    else:
        S_xy += 2  # increase the size of S_xy to the next odd value.
        if (S_xy <= S_max):  # repeat process
            return level_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
        else:
            return z_med


def level_B(z_min, z_med, z_max, z_xy, S_xy, S_max):
    if (z_min < z_xy < z_max):
        return z_xy
    else:
        return z_med


def adaptive_median_filter(image, initial_window, max_window):
    xlength, ylength = image.shape  # get the shape of the image.
    S_max = max_window
    S_xy = initial_window

    output_image = image.copy()

    for row in range(S_xy, xlength - S_xy - 1):
        for col in range(S_xy, ylength - S_xy - 1):
            filter_window = image[row - S_xy: row + S_xy + 1, col - S_xy: col + S_xy + 1]  # filter window
            target = filter_window.reshape(-1)
            z_min = np.min(target)
            z_max = np.max(target)
            z_med = np.median(target)
            z_xy = image[row, col]
            new_intensity = level_A(z_min, z_med, z_max, z_xy, S_xy, S_max)
            output_image[row, col] = new_intensity
    return output_image


def show_adaptive(path):
    global img
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print('файла по заданному не существует')
    gray = img.convert('L')
    image = np.array(gray)
    filtered_img = adaptive_median_filter(image, 3, 17)
    Image.fromarray(filtered_img).show()
