import permissions
class Category:
    object = []
    def __init__(self, title):
        self.title = title
        Category.object.append(self)

    def __str__(self):
        return self.title

class Product:
    object = []
    __id = 0
    def __init__(self,title,price,description,quantity, category):
        self.id = Product.__id
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
        self.category = category
        Product.object.append(self)
        Product.__id +=1

    def __str__(self):
        return f'{self.title} [{self.quantity}] - ${self.price}\n({self.desc[:20]})'

class Comment:
    object = []
    def __init__(self, user, body, product):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.object.append(self)

    def __str__(self):
        return f'{self.user.email} [{self.created_at}] - {self.body}'
