from django.contrib import admin
from django.urls import path, re_path

from blog import views

urlpatterns = [
    path(r'show_time/', views.show_time),
    path('article/<int:year>/<int:month>', views.article_year),
    re_path(r're/(\d{3})', views.re_test),
    path(r'register', views.register),
    path(r'login', views.login)
]