from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from django.urls import reverse_lazy

from .models import Income, Payment


class ListIncomeView(ListView):
    template_name = 'mainapp/income_list.html'
    model = Income
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    '''


class ListPaymentView(ListView):
    template_name = 'mainapp/payment_list.html'
    model = Payment


class CreateIncomeView(CreateView):
    template_name = 'mainapp/income_create.html'
    model = Income
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-income')


class CreatePaymentView(CreateView):
    template_name = 'mainapp/payment_create.html'
    model = Payment
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-payment')
