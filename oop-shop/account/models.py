import permissions
class User:
    object = []
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        # в objects добавляем обьект
        User.object.append(self)
    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception('Пароли не совпадают')
        self.__password = password # __password - __ скрываает пароль
        print(f'Успешно зарегистрирован юзер {self.email}')

    def login(self, password):
        if self.__password != password:
            raise Exception('Пароль не верный')
        self.is_authenticated = True
        print(f'Успешно залогинился юзер  {self.email}')
    
    def logout(self):
        permissions.login_required(self)
        self.is_authenticated = False
        print(f'Успешно вышел юзер {self.email}')
    
