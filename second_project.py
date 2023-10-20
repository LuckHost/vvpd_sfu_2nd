import numpy as np

def get_coorect_inp(list_of_values):
    while True:
        try:
            value = int(input("Введите значение.. "))
            if value in list_of_values:
                return value
            print("Ввод инкорректен, повторите")
            continue
        except ValueError:
            print("Ввод инкорректен, повторите")
    


def get_random_array(rows = 1, columns = 1):
    arr = np.random.randint(-10, 10, size=(rows, columns))
    return arr

def menu():
    """ user menu """
    while True:
        print("Выберете действие:\n",
              "1 - элементы только в A или только в B\n",
              "2 - несколько в A или несколько в B\n",
              "3 - уникальные в A, несколько в B\n")
        print(get_coorect_inp([1, 2, 3]))
        

def main():
    """the main function"""
    print("Вас приветствует программа 2й практики по ВВПД\n",
        "Выполнил Ходыкин Александр КИ23-17/2б")
    menu()

if __name__ == "__main__":
    main()