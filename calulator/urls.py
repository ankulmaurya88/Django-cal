from .views import CalculatorView
from django.urls import path

urlpatterns = [
    path('', CalculatorView.as_view(), name='calculator'),
]
