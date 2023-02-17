from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class UserProfile(models.Model):  # профиль пользователя
    def validate_image(fieldfile_obj):
        file_size = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError("Максимальный размер файла {}MB".format(str(megabyte_limit)))

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(default='не указано', max_length=50, verbose_name='имя пользователя', blank=True)
    surname = models.CharField(default='Не указано', max_length=50, verbose_name='фамилия пользователя', blank=True)
    patronymic = models.CharField(default='Не указано', max_length=50, verbose_name='отчество пользователя', blank=True)
    phone = models.CharField(default='Не указано', max_length=30, verbose_name='номер телефона', blank=True, null=True,
                             unique=True)
    email = models.EmailField(default='Не указано', verbose_name='email пользователя', blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='files/', null=True, validators=[validate_image])

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and instance.is_superuser:
            UserProfile.objects.create(user=instance)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class CategoryProduct(models.Model):  # категория товаров
    title_category = models.TextField(max_length=50, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):  # товар
    title_product = models.TextField(max_length=50, verbose_name='название товара')
    description = models.TextField(max_length=100, verbose_name='описание товара')
    count = models.IntegerField(default=0, verbose_name='количество')
    price = models.IntegerField(default=0, verbose_name='цена товара')
    category = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, verbose_name='товар')
    limited_edition = models.BooleanField(default=False)
    popular_product_count = models.IntegerField(default=0, verbose_name='счетчик покупок данного товара')
    product_picture = models.ImageField(upload_to='files/', null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title_product


class Basket(models.Model):  # корзина пользователя
    username = models.OneToOneField('UserProfile', unique=True, on_delete=models.CASCADE, related_name='profile')
    product = models.ManyToManyField('Product', related_name='product', through='Enrollment')
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.username.name


class Enrollment(models.Model):  # промежуточная таблица корзины
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Reviews(models.Model):  # отзыв
    text = models.CharField(default='Не указано', max_length=100, verbose_name='текст отзыва', blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    user_name = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='пользователь')
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.product.title_product


class UserHistory(models.Model):  # история заказов пользователя
    user_history = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='пользователь', null=True)
    product_history = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт', null=True)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.TextField(max_length=30, default='не указан', verbose_name='способ оплаты заказа')
    payment_delivery = models.TextField(max_length=50, default='не указан', verbose_name='способ доставки заказа')
    mistake_text = models.TextField(default='None', max_length=100, verbose_name='текст ошибки оплаты')

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'Истории покупок'

    def __str__(self):
        return self.user_history
