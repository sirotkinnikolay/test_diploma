from django.urls import path
from store_app.views import *
from rest_framework import routers

urlpatterns = [
    path('logout/', AuthorLogoutView.as_view(), name='logout'),  # страница входа пользователя
    # path('register/', RegisterView.as_view(), name='register'),  # страница регистрации
    path('login/', AuthorLoginView.as_view(), name='login'),  # страница выхода из учетной записи
    path('', StartView.as_view(), name='index'),  # "frontend/index.html"
    path('about/', AboutShopView.as_view(), name='about'),  # about.html
    path('account/', UserOfficeView.as_view(), name='account'),  # account.html
    path('cart/', UserCartView.as_view(), name='cart'),  # cart.html
    path('catalog/', AllProductCatalogView.as_view(), name='catalog'),  # catalog.html
    path('catalog/<int:pk>', CatalogOneCategoryView.as_view(), name='catalog'),  # catalog.html
    path('history-order/', UserHistoryOrderView.as_view(), name='historyorder'),  # historyorder.html
    path('order-detail/<int:pk>', OneOrderView.as_view(), name='oneorder'),  # oneorder.html
    path('order/', OrderView.as_view(), name='order'),  # order.html
    path('payment/', PaymentView.as_view(), name='payment.html'),  # payment.html
    path('payment-someone/', PaymentSomeOneView.as_view(), name='paymentsomeone'),  # paymentsomeone.html
    path('product/<int:pk>', ProductView.as_view(), name='product'),  # product.html
    path('profile/', ProfileEditView.as_view(), name='profile'),  # profile.html
    path('progress-payment/', ProgressPaymentView.as_view(), name='progress_payment'),  # progressPayment.html
    path('sale/', SaleView.as_view(), name='sale'),  # sale.html
]

api_urlpatterns = [
    path("categories/", category_list, name='category_list'),
    # path("test/", CategoryProductView.as_view()),



]
