from models import User, Product, Comment

user1 = User("test@gmail.com", 'hello', 'male')

user1.register('123456789', '123456789')
user1.login('1234')
print(user1.is_authenticated)

product1 = Product("Iphone10", 121343, '...', 10)
comment1 = Comment(user1, product1)

