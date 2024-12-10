a = input() # ввод
def read_this(a): # создание функции для чтения файла в зависимости от введенного параметра
    try: # блок try
        if a == "чтение":
            with open('exampl33e.txt', 'r') as file: # открытие файла в режиме чтения
                content = file.read() # считывание файла
            print(content) # вывод
        if a == "построчное":
            with open('example.txt', 'r') as file: # открытие файла в режиме чтения
                for line in file:
                    print(line) # вывод каждой строки
    except FileNotFoundError: # обработка исключения если файл не найден
        print("Файл не найден") # сообщение
read_this(a) # вызов функции