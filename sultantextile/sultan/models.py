from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    gender = models.CharField(max_length=10, choices=[
        ('men', 'Мужская'),
        ('women', 'Женская'),
        ('kids', 'Детская')
    ], verbose_name='Пол')
    image = models.ImageField(upload_to='categories/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение', default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'gender_slug': self.gender, 'category_slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Старая цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    material = models.CharField(max_length=100, verbose_name='Материал')
    color = models.CharField(max_length=50, verbose_name='Цвет')

    # Размеры (можно сделать отдельной моделью для сложных случаев)
    # sizes = models.CharField(max_length=100, help_text='S,M,L,XL или 42,44,46 и т.д.', verbose_name='Доступные размеры')

    # Изображения
    main_image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Главное изображение', default='', blank=True, null=True)
    # image_2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True,
    #                             verbose_name='Доп. изображение 2')
    # image_3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True,
    #                             verbose_name='Доп. изображение 3')

    # Статусы
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # is_available = models.BooleanField(default=True, verbose_name='В наличии')
    # is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемый товар')

    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('good', kwargs={'good_slug': self.slug})

    # @property
    # def has_discount(self):
    #     """Есть ли скидка на товар"""
    #     return self.old_price and self.old_price > self.price

