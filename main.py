def switch_methods():
    method = input("введите название метода фильтрации: ")
    match method:
        case 'медианный':
            print('1')
        case 'взвешенный':
            print('2')
        case 'адаптивный':
            print('3')
        case _:
            print('такого фильтра не существует, проверьте введенное выражение')


if __name__ == "__main__":
    switch_methods()

