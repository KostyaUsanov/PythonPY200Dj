from django.urls import path
from .views import TemplView


app_name = 'landing'

urlpatterns = [
    path('landing/', TemplView.as_view(), name='landing'),
]

    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing