from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

from .models import Income, Payment


class ListIncomeView(ListView):
    template_name = 'mainapp/income_list.html'
    model = Income


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


class DetailIncomeView(DetailView):
    template_name = 'mainapp/income_detail.html'
    model = Income


class DetailPaymentView(DetailView):
    template_name = 'mainapp/payment_detail.html'
    model = Payment


class UpdateIncomeView(UpdateView):
    template_name = 'mainapp/income_update.html'
    model = Income
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-income')


class UpdatePaymentView(UpdateView):
    template_name = 'mainapp/payment_update.html'
    model = Payment
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-payment')


class DeleteIncomeView(DeleteView):
    template_name = 'mainapp/income_delete.html'
    model = Income
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-income')


class DeletePaymentView(DeleteView):
    template_name = 'mainapp/payment_delete.html'
    model = Payment
    fields = ('date', 'category', 'price', 'description')
    success_url = reverse_lazy('list-payment')
