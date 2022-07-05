from shop.models import Product
from abstract.serializers import BaseSerializer
from shop.serializers import ProductSerializer
cat 
obj1 = Product("iphone", 234, "...", 3)
obj2 = Product("RedMi", 200, "...", 6)
obj3 = Product("Samsung", 300, "...", 5)

res = BaseSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint
pprint(res)
