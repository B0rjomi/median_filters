from PIL import Image
import numpy as np


def adaptive_median_filter_color(img, window_size_max):
    img_arr = np.array(img)
    h, w, c = img_arr.shape
    window_size = 3

    out_arr = np.zeros_like(img_arr)

    for j in range(h):
        for i in range(w):
            while window_size <= window_size_max:
                # Get current window
                window = img_arr[max(0, j - window_size//2):min(h, j + window_size//2 + 1),
                max(0, i - window_size//2):min(w, i + window_size//2 + 1), :]
                # Calculate median and max/min pixel value in each channel of the window
                med = np.median(window, axis=(0,1))
                max_val = np.max(window, axis=(0,1))
                min_val = np.min(window, axis=(0,1))

                # Check if pixel value is within the allowed range in each channel
                if np.all(min_val < med) and np.all(med < max_val):
                    out_arr[j, i, :] = med
                    break
                else:
                    window_size += 2
            else:
                out_arr[j, i, :] = med

            window_size = 3

    return Image.fromarray(out_arr)


img = Image.open('pictures/picture_1.jpg')
filtered_img = adaptive_median_filter_color(img, 17)
img.show()
filtered_img.show()
