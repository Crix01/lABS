class Vehicle: # определение класса
    def __init__(self, make, model): # инициализация объекта класса   
        self.make = make # марка
        self.model = model # модель
    def get_info(self): # метод для указания марки и модели
        return f"Марка: {self.make}, Модель: {self.model}"
class Car(Vehicle): # определение класса 
    def __init__(self, make, model, fuel_type): # инициализация объекта 
        super().__init__(make, model) # вызов  init класса для инициализации марки и модели
        self.fuel_type = fuel_type # топливо
    def get_info(self): # метод для указания полной характеристики машины
        return f"{super().get_info()}, Тип топлива: {self.fuel_type}"
make = input("Введите марку машины: ") # ввод
model = input("Введите модель машины: ") # ввод
fuel_type = input("Введите тип топлива: ") # ввод
car = Car(make, model, fuel_type) # объект класса машина
print(car.get_info()) # вывод информации на экран