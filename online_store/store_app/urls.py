from django.urls import path, include
from .views import *

urlpatterns = [
    path('', StartView.as_view(), name='start'),

    path('logout/', AuthorLogoutView.as_view(), name='logout'),  # страница входа пользователя
    path('register/', Register.as_view(), name='register'),  # страница регистрации
    path('login/', AuthorLoginView.as_view(), name='login'),  # страница выхода из учетной записи

    path('office/', UserOffice.as_view(), name='office'),  # личный кабинет пользователя
    path('profile_edit/', ProfileEdit.as_view(), name='profile_edit'),  # редактирование профиля пользователя
    path('history_buy/', UserHistoryBuy.as_view(), name='history_duy'),  # история заказов пользователя

    path('products/', AllProductView.as_view(), name='products'),  # каталог товаров с фильтром и сортировкой
    path('products/<int:pk>/', OneProductBuy.as_view(), name='product_buy'),  # страница товара
    path('basket/', BasketView.as_view(), name='basket'),  # корзина пользователя
    path('buy/', BuyBasket.as_view(), name='buy'),  # оформление и оплата заказа
]
