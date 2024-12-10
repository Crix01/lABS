number = int(input()) # ввод числа
def is_prime(number): # функция и аргумент number
    if number == 1:
        return False # возвращает фолз
    if number % 2 != 0 and number % 3 != 0 or number == 2 or number == 3: # огромное условие для определения простого числа
        return True # возвращает тру
    else: #если наоборот
        return False # возвращает фолз
print(is_prime(number)) # вывод результата выполнения функции