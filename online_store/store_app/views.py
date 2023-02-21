import os

from django.shortcuts import render
from store_app.models import Product, CategoryProduct
from django.views import View
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Count, Avg, Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
import random
import string
import json
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import renderers, serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

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

    def get(self, request):
        return render(request, 'frontend/sale.html')


class AllProductCatalogView(LoginRequiredMixin, ListView):
    """Страница вывода списка товаров"""
    pass


class ProductView(LoginRequiredMixin, DetailView):
    """Страница информации о товаре"""
    pass


class StartView(View):
    """Стартовая страница, просмотренные товары, популярные товары"""

    def get(self, request):
        return render(request, 'frontend/index.html')


class BuyProduct(View):
    """Добавление товара в корзину"""
    pass


class ReviewsAddView(View):
    """Добавление отзыва к товару"""
    pass


class PaymentSomeOneView(View):
    """Страница оплаты"""
    pass


#  ================= API ======================

class One(APIView):
    def get(self, request):
        item = CategoryProduct.objects.all()
        serializer = CategoryProductSerializer(item, many=True)
        return Response(serializer.data)


class CategoryProductView(View):
    def get(self, request):
        categories = CategoryProduct.objects.all()
        categories_serialized_data = []

        for category in categories:
            categories_serialized_data.append({
                'id': str(category.id),
                'title': category.title,
                'image': {"src": str(category.image), "alt": os.path.basename(category.image.name)},
                'href': '/catalog/' + str(category.id),
                'subcategories': [{'id': str(category.id),
                                   'title': category.title,
                                   'image': {"src": str(category.image), "alt": os.path.basename(category.image.name)},
                                   'href': '/catalog/' + str(category.id), }]
            })

        return JsonResponse(categories_serialized_data, safe=False)


