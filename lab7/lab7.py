class Employee: # класс
    def __init__(self, name, id): # инициализация сотрудника с именем и id
        self.name = name
        self.id = id

    def get_info(self): # метод для получения информации о сотруднике
        return f"Имя: {self.name}, ID: {self.id}" # сообщение


class Manager(Employee): # класс
    def __init__(self, name, id, department): # инициализация менеджера с сотрудником и отделом
        super().__init__(name, id)
        self.department = department

    def manage_project(self): # метод для получения информации о проекте, которым управляет менеджер
        return f"Менеджер {self.name} управляет проектом в отделе {self.department}." # сообщение

class Technician(Employee): # класс
    def __init__(self, name, id, specialization): # инициализация техника с сотрудником и специализацией
        super().__init__(name, id)
        self.specialization = specialization

    def perform_maintenance(self): # метод для получения информации о технике
        return f"Техник {self.name} имеет специализацию ({self.specialization})." # сообщение

class TechManager(Manager, Technician):  # множественное наследование
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id) # вызываем Employee.__init__ только один раз
        self.department = department
        self.specialization = specialization        
        self.subordinates = [] # список сотрудников 

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        print(f"Информация о команде тех. менеджера {self.name}:") # сообщение
        for emp in self.subordinates: # перебирает подчиненных
            if isinstance(emp, Manager): # если подчиненный - менеджер
                print(emp.manage_project()) # выводит информацию о его проекте
            elif isinstance(emp, Technician): # если подчиненный - техник
                print(emp.perform_maintenance()) # выводит информацию о его специализации
            else:
                print(emp.get_info()) # вывод информации о сотруднике
def create_employee(employee_type): # создание сотрудника 
    
    name = input("Введите имя: ") # ввод
    id_input = input("Введите ID: ") # ввод          
    if employee_type == "Manager": # если менеджер
        department = input("Введите отдел: ") # ввод
        return Manager(name, id_input, department) # возврат
    elif employee_type == "Technician": # если менеджер если техник 
        specialization = input("Введите специализацию: ") # ввод
        return Technician(name, id_input, specialization)
    else:
        return Employee(name, id_input) # возврат объекта сотрудника         
techmanager1 = TechManager("Степан Афанасьеф", 4, "Разработка", "Программирование") # сообщение 
while True:
    add_more = input("Добавить ещё сотрудника? (да/нет): ") # ДОБАВИТЬ ЕЩЁ СОТРУДНИКА?!??!!?!?
    if add_more.lower() == "нет": # если нет 
        break # конец программы 
    employee_type = input("Введите тип сотрудника (Employee, Manager, Technician): ") # выбор типа сотрудника
    new_employee = create_employee(employee_type) # создание нового сотрудника 
    if new_employee: # если сотрудник создан
        techmanager1.add_employee(new_employee) # добавление сотрудника к техническому менеджеру      
techmanager1.get_team_info() # вывод инфы о команде