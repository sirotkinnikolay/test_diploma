from rest_framework import serializers
from store_app.models import *


class CategoryProductSerializer(serializers.ModelSerializer):
    """Создание и настройка сериалайзер класса для модели CategoryProduct с необходимыми полями"""

    class Meta:
        model = CategoryProduct
        fields = ['title', 'image']


class ProductSerializer(serializers.ModelSerializer):
    """Создание и настройка сериалайзер класса для модели Product с необходимыми полями"""

    class Meta:
        model = Product
        fields = ['title', 'price']
