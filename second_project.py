import numpy as np

def get_correct_inp(list_of_values, menu_str = "Введите значение.. ") :
    while True:
        try:
            value = int(input(menu_str))
            if value in list_of_values:
                return value
            print("Ввод инкорректен, повторите")
            continue
        except ValueError:
            print("Ввод инкорректен, повторите")

def get_random_array(len = 1):
    arr = np.random.randint(-10, 10, size=(len))
    return arr

def first_task():
    """ returns first task answer """
    arr_len = get_correct_inp(range(1, 10)
                              , "Введите длину массивов: ")
    arr_a = get_random_array(arr_len)
    arr_b = get_random_array(arr_len)
    print("Массивы: \n",
          arr_a, "\n",
          arr_b)
    arr_a = set(arr_a)
    arr_b = set(arr_b)
    answer = [i for i in arr_a if i not in arr_b] + \
    [i for i in arr_b if i not in arr_a]
    print("Ответ: ", 
          sorted(answer))

def menu():
    """ user menu """
    while True:
        print("Выберете действие:\n",
              "1 - элементы только в A или только в B\n",
              "2 - несколько в A или несколько в B\n",
              "3 - уникальные в A, несколько в B\n")
        return get_correct_inp([1, 2, 3],
                                "Введите номер действия: ")
        

def main():
    """the main function"""
    print("Вас приветствует программа 2й практики по ВВПД\n",
        "Выполнил Ходыкин Александр КИ23-17/2б")
    task = menu()
    if task == 1:
        first_task()

if __name__ == "__main__":
    main()