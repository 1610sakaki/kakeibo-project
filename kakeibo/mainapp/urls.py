from django.urls import path
from . import views

urlpatterns = [
    path('kakeibo/', views.ListIncomeView.as_view()),
]
