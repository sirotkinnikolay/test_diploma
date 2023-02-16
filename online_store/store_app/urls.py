from django.urls import path, include
from .views import *

urlpatterns = [
    path('', StartView.as_view(), name='start'),

    path('logout/', AuthorLogoutView.as_view(), name='logout'),  # страница входа пользователя
    path('register/', RegisterView.as_view(), name='register'),  # страница регистрации
    path('login/', AuthorLoginView.as_view(), name='login'),  # страница выхода из учетной записи

    path('about/', AboutShopView.as_view(), name='about'),  # страница с информацией о магазине
    path('account/', UserOfficeView.as_view(), name='account'),  # личный кабинет пользователя
    path('cart/', UserCartView.as_view(), name='cart'),  # корзина пользователя
    path('catalog/', AllProductCatalogView.as_view(), name='catalog'),  # каталог товаров с фильтром и сортировкой
    path('history_order/', UserHistoryOrderView.as_view(), name='history_order'),  # история заказов пользователя
    path('index/', IndexView.as_view(), name='index'),  # страница с популярными товарами
    path('one_order/', OneOrderView.as_view(), name='one_order'),  # страница  заказа
    path('order/', OrderView.as_view(), name='order'),  # страница оформления заказа
    path('payment/', PaymentView.as_view(), name='payment'),  # страница оплаты(ввода карты) заказа
    path('payment_some_one/', PaymentSomeOneView.as_view(), name='payment_some_one'),
    # страница оплаты(генерация счета) заказа

    path('products/<int:pk>/', ProductView.as_view(), name='product'),  # страница товара
    path('profile_edit/', ProfileEditView.as_view(), name='profile_edit'),  # редактирование профиля пользователя
    path('profile_avatar/', ProfileEditAvatarView.as_view(), name='profile_avatar'),
    # редактирование профиля(с загруженным аватаром) пользователя

    path('progress_payment/', ProgressPaymentView.as_view(), name='progress_payment'),
    # страница ожидания (загрузки) оплаты

    path('sale/', SaleView.as_view(), name='sale'),  # страница с товарами со скидкой
]
