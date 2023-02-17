from django.db import models
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
    full_name = models.CharField(default='не указано', max_length=50, verbose_name='ФИО пользователя', blank=True)
    phone = models.CharField(default='Не указано', max_length=30, verbose_name='номер телефона', blank=True, null=True,
                             unique=True)
    email = models.EmailField(default='Не указано', verbose_name='email пользователя', blank=True, unique=True)
    avatar = models.ImageField(upload_to='files/', null=True, validators=[validate_image], default='')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and instance.is_superuser:
            UserProfile.objects.create(user=instance)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name


class CategoryProduct(models.Model):  # категория товаров
    title_category = models.TextField(max_length=50, verbose_name='название категории')
    category_image = models.ImageField(upload_to='files/', null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title_category


class Product(models.Model):  # товар
    category = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, verbose_name='категория товара')
    specifications = models.ForeignKey('Specifications', on_delete=models.CASCADE, verbose_name='спецификация товара')
    price = models.IntegerField(default=0, verbose_name='цена товара')
    count = models.IntegerField(default=0, verbose_name='количество ')
    date = models.DateField(auto_now_add=True)
    title_product = models.TextField(max_length=50, verbose_name='название товара')
    description = models.TextField(max_length=100, verbose_name='описание товара')
    free_delivery = models.BooleanField(default=True)
    product_picture = models.ImageField(upload_to='files/', null=True)
    rating = models.IntegerField(default=0, verbose_name='счетчик покупок данного товара')
    reviews = models.IntegerField(default=0, verbose_name='счетчик просмотров данного товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title_product


class FilesImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    picture = models.ImageField(upload_to='files/', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.product


class TagsFile(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    tags_name = models.TextField(max_length=50, verbose_name='тэг товара')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tags_name


class Reviews(models.Model):  # отзыв
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар',
                                related_name='product_title_product_set')
    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.CharField(default='Не указано', max_length=100, verbose_name='текст отзыва', blank=True)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Specifications(models.Model):
    name = models.TextField(max_length=50, verbose_name='название')
    value = models.TextField(max_length=50, verbose_name='значение')

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'

    def __str__(self):
        return self.name


class OrderHistory(models.Model):  # история покупок пользователя
    user_order = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='пользователь', null=True)
    product_order = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    payment_date = models.DateField(auto_now_add=True)
    delivery_type = models.TextField(max_length=30, default='не указан', verbose_name='способ доставки')
    payment_type = models.TextField(max_length=30, default='не указан', verbose_name='способ оплаты')
    total_cost = models.IntegerField(default=0, verbose_name='общая стоимость заказа')
    status = models.TextField(max_length=30, default='не указан', verbose_name='статус оплаты')
    city = models.TextField(max_length=30, default='не указан', verbose_name='город доставки')
    address = models.TextField(max_length=30, default='не указан', verbose_name='адрес доставки')

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'Истории покупок'

    def __str__(self):
        return self.user_order.name


class Order(models.Model):  # покупка товаров из корзины
    product_order = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    count = models.IntegerField(default=0, verbose_name='колличество  товаров в корзине')
    price = models.IntegerField(default=0, verbose_name='общая стоимость  товаров в корзине')
    date = models.DateField(auto_now_add=True)
    free_delivery = models.BooleanField(default=False, verbose_name='наличие бесплатной доставки')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.product_order


class Basket(models.Model):  # корзина пользователя
    username = models.OneToOneField('UserProfile', unique=True, on_delete=models.CASCADE, related_name='profile')
    product = models.ManyToManyField('Product', related_name='product', through='Enrollment')
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.username.name


class Payment(models.Model):
    number = models.IntegerField(default=0, verbose_name='номер счета')
    name = models.TextField(max_length=30, default='не указан')
    month = models.DateField(auto_now_add=True)
    year = models.DateField(auto_now_add=True)
    code = models.IntegerField(default=0, verbose_name='код оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'

    def __str__(self):
        return self.name


class Enrollment(models.Model):  # промежуточная таблица корзины
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)



