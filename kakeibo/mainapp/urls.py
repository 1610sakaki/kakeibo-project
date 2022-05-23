from django.urls import path
from . import views

urlpatterns = [
    path('kakeibo/', views.ListIncomeView.as_view(), name='kakeibo-main'),
    # income
    path('kakeibo/income/list', views.ListIncomeView.as_view(), name='list-income'),
    path('kakeibo/income/<int:pk>/detail',
         views.DetailIncomeView.as_view(), name='detail-income'),
    path('kakeibo/income/create',
         views.CreateIncomeView.as_view(), name='create-income'),
    path('kakeibo/income/<int:pk>/update',
         views.UpdateIncomeView.as_view(), name='update-income'),
    path('kakeibo/income/<int:pk>/delete',
         views.DeleteIncomeView.as_view(), name='delete-income'),
    # payment
    path('kakeibo/payment/list',
         views.ListPaymentView.as_view(), name='list-payment'),
    path('kakeibo/payment/<int:pk>/detail',
         views.DetailPaymentView.as_view(), name='detail-payment'),
    path('kakeibo/payment/create',
         views.CreatePaymentView.as_view(), name='create-payment'),
    path('kakeibo/payment/<int:pk>/update',
         views.UpdatePaymentView.as_view(), name='update-payment'),
    path('kakeibo/payment/<int:pk>/delete',
         views.DeletePaymentView.as_view(), name='delete-payment'),
]
