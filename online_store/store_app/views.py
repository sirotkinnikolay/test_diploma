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

from .models import Product


class AuthorLogoutView(LogoutView):
    """Выход из учетной записи пользователя"""
    next_page = '/'


class AuthorLoginView(LoginView):
    """Страница входа в учетную запись пользователя"""
    template_name = 'account.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('account')


class AllProductCatalogView(LoginRequiredMixin, ListView):
    """Страница вывода списка товаров"""
    model = Product
    template_name = 'catalog.html'
    ordering = ['-title_product']


class ProductView(LoginRequiredMixin, DetailView):
    """Страница информации о товаре"""
    model = Product
    template_name = 'product.html'


class IndexView(View):
    """Список просмотренных товаров, популярных товаров и товаров ограниченной серии"""
    pass


class BuyProduct(View):
    """Добавление товара в корзину"""
    pass

class ReviewsAddView(View):
    """Добавление отзыва к товару"""
    pass

