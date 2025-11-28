# mnemowizard
# mnemowizard@gmail.com
# My1Python!Guards23Rooms

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'set_image' ,'slug', 'id')  # что показывать в списке
    list_display_links = ('name', 'id')  # кликабельные поля
    list_filter = ('gender',)  # фильтры справа
    search_fields = ('name',)  # поиск по названию
    prepopulated_fields = {'slug': ('name',)}  # авто-заполнение slug
    ordering = ('name',)  # сортировка
    save_on_top = True
    list_per_page = 5

    @admin.display(description="Изоброжение" , ordering='price')
    def set_image(self, sultan: Category):
        return mark_safe(f"<img src='{sultan.image.url}' width='100' height='100' />")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'set_image', 'price', 'is_published', 'created_at')
    list_display_links = ('name',)
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('name', 'description', 'material')
    list_editable = ('price', 'is_published')  # можно редактировать прямо в списке
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    save_on_top = True
    list_per_page = 5

    actions = ['set_published', 'set_draft']

    @admin.display(description="Изоброжение" , ordering='price')
    def set_image(self, sultan: Product):
        return mark_safe(f"<img src='{sultan.main_image.url}' width='100' height='100' />")

    @admin.action(description='Выставить на продажу')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Выставлено {count} товаров')

    @admin.action(description='Снять с продаж')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Снято {count} товаров')

    # Группировка полей в форме редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Цены и детали', {
            'fields': ('set_image','price', 'old_price', 'material', 'color')
        }),
        ('Статус', {
            'fields': ('is_published',)
        }),
    )

