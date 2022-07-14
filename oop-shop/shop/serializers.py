from abstract.serializers import BaseSerializer
from .models import Category, Product, Comment

class CateogrySerializer(BaseSerializer):
    class Meta:
        fields = ['title']
        queryset = Category.object

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ['id', 'title', 'price', 'desc', 'quantity', 'category', 'comments']
        queryset = Product.object

    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_['category'] = obj.category.title
        dict_['comment'] = CommentSerializer().serialize_queryset(obj)
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body", "created_at"]
        queryset = Comment.object

    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_['user'] = obj.user.email
        dict_['created_at'] = obj.created_at.strftime('%d.%m.%Y %H:%M:%S')

        