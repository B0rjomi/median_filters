from median_filter import show_res
from adaptive_median_filter import show_adaptive
from weighted_median_filter import show_weighted

def switch_methods():
    method = input("введите название метода фильтрации: ")
    match method:
        case 'медианный':
            show_res('pictures/asta.jpg')
        case 'взвешенный':
            show_weighted('pictures/asta.jpg')
        case 'адаптивный':
            show_adaptive('pictures/asta.jpg')
        case _:
            print('такого фильтра не существует, проверьте введенное выражение')


if __name__ == "__main__":
    switch_methods()

