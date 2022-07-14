from urls import urlpatterns
from pprint import pprint


while True:
    url, arg = input ('Введите аддрес: ').split("/")
    found = False
    for uri, view, in urlpatterns:
        if uri.split("/")[0] == url:
            found = True
            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)
    if not found :
        print('404 Url Not Found')