a = input() # ввод
def read_this(a): # создание функции для чтения файла в зависимости от введенного параметра
    if a == "чтение":
        with open('example.txt', 'r') as file: # открытие файла в режиме чтения
            content = file.read() # считывание файла
            print(content) # вывод
    if a == "построчное":
        with open('example.txt', 'r') as file: # открытие файла в режиме чтения
            for line in file:
                print(line) # вывод каждой строки
read_this(a) # вызов функции