from rest_framework import serializers
from store_app.models import *


class CategoryProductSerializer(serializers.ModelSerializer):
    """Создание и настройка сериалайзер класса для модели Book с необходимыми полями"""
    class Meta:
        model = CategoryProduct
        fields = ['title', 'image']