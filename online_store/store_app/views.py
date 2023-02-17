from django.shortcuts import render
from store_app.models import Product
from .forms import *
from django.views import View
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Count, Avg, Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
import random
import string



class AuthorLogoutView(LogoutView):
    """Выход из учетной записи пользователя"""
    next_page = '/'


class AuthorLoginView(LoginView):
    """Страница входа в учетную запись пользователя"""
    template_name = 'account.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account')


class AboutShopView(View):
    """Информация о магазине"""
    pass


class CatalogOneCategoryView(View):
    """Одна категория товаров"""
    pass


class UserHistoryOrderView(View):
    """История заказов пользователя"""
    pass


class OrderView(View):
    """Оформление заказа(первый этап)"""
    pass


class OneOrderView(View):
    """Страница детальной информации о заказе"""
    pass


class PaymentView(View):
    """Оплата заказа, ввод номера карты"""
    pass


class UserOfficeView(View):
    """Личный кабинет пользователя"""
    pass


class UserCartView(View):
    """Корзина пользователя"""
    pass


class ProfileEditView(View):
    """Профиль пользователя и изменение данных профиля"""
    pass


class ProgressPaymentView(View):
    """Страница загрузки оплаты"""
    pass


class SaleView(View):
    """Страница распродажи товаров"""
    pass


class AllProductCatalogView(LoginRequiredMixin, ListView):
    """Страница вывода списка товаров"""
    model = Product
    template_name = 'catalog.html'
    ordering = ['-title_product']


class ProductView(LoginRequiredMixin, DetailView):
    """Страница информации о товаре"""
    model = Product
    template_name = 'product.html'


class StartView(View):
    """Стартовая страница, просмотренные товары, популярные товары"""
    pass


class BuyProduct(View):
    """Добавление товара в корзину"""
    pass


class ReviewsAddView(View):
    """Добавление отзыва к товару"""
    pass


class PaymentSomeOneView(View):
    """Страница оплаты"""
    pass
