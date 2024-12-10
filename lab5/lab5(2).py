class Circle:  # определение класса Circle
    def __init__(self, radius):  # конструктор класса Circle
        self.radius = radius  # инициализация атрибута radius
    def get_radius(self):  # метод для получения радиуса
        return self.radius  # возвращает значение атрибута radius
    def set_radius(self, new_radius):  # метод для изменения радиуса
        self.radius = new_radius  # изменяет значение атрибута radius
radius = input("Введите радиус: ")  # ввод радиуса от пользователя
a = Circle(radius)  # создание объекта класса Circle
print(f"Первоначальный радиус: {a.get_radius()}")  # вывод первоначального радиуса
new_radius = input("Введите новый радиус: ")  # ввод нового радиуса от пользователя
a.set_radius(new_radius)  # изменение радиуса a
print(f"Новый радиус: {a.get_radius()}")  # вывод нового радиуса