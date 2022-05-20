from django.urls import path
from . import views

urlpatterns = [
    path('kakeibo/income', views.ListIncomeView.as_view()),
]
