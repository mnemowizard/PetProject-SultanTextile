from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Домой "/"
    path('', views.index, name='home'),

    # Каталог с фильтрацией: /catalog/men/jackets/
    path('catalog/<slug:gender_slug>/' , views.catalog, name='catalog'),
    path('catalog/<slug:gender_slug>/<slug:catalog_slug>/', views.catalog, name='catalog'),

    # Товары: /product/men-leather-jacket/
    path('good/<slug:good_slug>/', views.good, name='good'),

    # Контакты
    path('contacts/', views.contacts, name='contacts'),

    # Поиск
    path('search/', views.search, name='search'),

    # Корзина
    path('cart/', views.cart, name='cart'),

]