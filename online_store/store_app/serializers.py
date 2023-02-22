from rest_framework import serializers
from store_app.models import *


class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=50)
    image = serializers.DictField()
    href = serializers.CharField(max_length=50)
    subcategories = serializers.ListField()

