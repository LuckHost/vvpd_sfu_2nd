import numpy as np

def get_random_array(rows = 1, columns = 1):
    arr = np.random.randint(-10, 10, size=(rows, columns))
    return arr

def main():
    """the main function"""
    print(get_random_array(2, 4))

if __name__ == "__main__":
    main()