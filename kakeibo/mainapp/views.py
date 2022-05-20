from django.shortcuts import render
from django.views.generic import ListView

from .models import Income


class ListIncomeView(ListView):
    template_name = 'mainapp/income_list.html'
    model = Income
