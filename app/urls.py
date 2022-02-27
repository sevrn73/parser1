from django.urls import path
from app.views import main

urlpatterns = [
    # Основные представления
    path('', main, name='main'),                                            # Главная
]
