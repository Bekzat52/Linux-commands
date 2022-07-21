from account.views import register
from shop.views import create_comment, product_list, create_product

urlpatterns = [
    ('register/', register),
    ('created-product/', create_product),
    ('product-list/', product_list), 

    ('create-comment/id', create_comment),
]