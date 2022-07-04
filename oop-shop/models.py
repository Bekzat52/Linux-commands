import permissions
class Category:
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return self.title

class Product:
    def __init__(self,title,price,description,quantity, sex):
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
        self.sex = sex
    
    def __str__(self):
        return f'{self.title} [{self.quantity}] - ${self.price}\n({self.desc[:20]})'

class Comment:
    def __init__(self, user, body, product):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()

    def __str__(self):
        return f'{self.user.email} [{self.created_at}] - {self.body}'


class User:
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False

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
    
    def 



