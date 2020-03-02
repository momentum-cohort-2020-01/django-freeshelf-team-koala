"""BigFarma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from store import views

urlpatterns = [
    path('', views.store, name='index'),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # path('accounts/activate', views.activate, name = 'activate'),
    # path('accounts/activation-complete', views.activation_complete, name = 'activation_complete'),
    # path('accounts/login', views.login, name = 'login'),
    # path('accounts/logout', views.logout, name = 'logout'),
    # path('accounts/registration', views.registration, name = 'registration'),
    # path('accounts/registration-complete', views.registration-complete, name ='registration_complete'),
    path('store/<int:pk>/', views.book_details, name='book_details'),
    # path('store/add/<int:pk>/', views.add_to_cart, name = 'add_to_cart'),
    # path('store/remove/<int:pk>/', views.remove_from_cart, name = 'remove_from_cart'),
    # path('store/cart/', views.cart, name = 'cart'),

    path('store/<slug:slug>', views.books_by_category, name = 'books_by_category'),
    path('author', views.author, name = 'author'),
    path('admin/', admin.site.urls),
]
