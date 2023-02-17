from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'patronymic', 'surname', 'phone', 'email', 'profile_picture']


class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ['title_category']
    search_fields = ['title_category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_product', 'description', 'count', 'price', 'category', 'limited_edition', 'product_picture']
    search_fields = ['title_product']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['username', 'product']
    search_fields = ['username']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['text', 'product', 'user_name', 'create_at']
    search_fields = ['user_name']


class UserHistoryAdmin(admin.ModelAdmin):
    list_display = ['user_history', 'product_history', 'payment_date',
                    'payment_method', 'payment_delivery', 'mistake_text']
    search_fields = ['user_history']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
