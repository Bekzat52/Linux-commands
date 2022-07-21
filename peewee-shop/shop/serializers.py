from abstract.serializers import BaseSerializer
from .models import Product, Comment

class ProductSerializer(BaseSerializer):
    class Meta:
        feilds = ('id', 'catergory', 'title', 'price', 'description', 'comments')
        model = Product


class CommentSereializer(BaseSerializer):
    class Meta:
        fields = ('id', 'user', 'body', 'created_at')
        model = Comment

    def serialize_obj(self, obj):
        