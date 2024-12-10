class UserAccount: #определение класса
    def __init__(self, username, email, password): # инициализация объекта класса UserAccount
        self.username = username # имя 
        self.emale = email # почта
        self.password = password #пароль
    def set_password(self, new_password): # метод для установки нового пароля 
        self.password = new_password # обновление пароля
    def check_password(self, password): # проверка пароля
        return password == self.password # сравнение введённого пароля с сохранённым
user = UserAccount("Bogdan", "dwadawd@mail.ru", "???") # объект класса
new_password = input("Введите новый пароль: ") # ввод пароля
user.set_password(new_password) # установление нового пароля для юзера
check_password = input("Введите пароль для проверки: ") # подтверждение пароля
print(user.check_password(check_password)) # тру или фолз в зависимости от правильности пароля