from asyncio.format_helpers import _format_callback
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import PaymentSearchForm, PaymentCreateForm, IncomeCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Income, Payment


class ListIncomeView(ListView):
    template_name = 'mainapp/income_list.html'
    model = Income


class ListPaymentView(ListView):
    template_name = 'mainapp/payment_list.html'
    model = Payment

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        self.form = form = PaymentSearchForm(self.request.GET or None)

        if form.is_valid():
            year = form.cleaned_data.get('year')
            # 何も選択されていないときは0の文字列が入るため、除外
            if year and year != '0':
                queryset = queryset.filter(date__year=year)

            # 何も選択されていないときは0の文字列が入るため、除外
            month = form.cleaned_data.get('month')
            if month and month != '0':
                queryset = queryset.filter(date__month=month)

            # 〇〇円以上の絞り込み
            greater_than = form.cleaned_data.get('greater_than')
            if greater_than:
                queryset = queryset.filter(price__gte=greater_than)

            # 〇〇円以下の絞り込み
            less_than = form.cleaned_data.get('less_than')
            if less_than:
                queryset = queryset.filter(price__lte=less_than)

            # キーワードの絞り込み
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                # 空欄で区切り、順番に絞る、and検索
                if key_word:
                    for word in key_word.split():
                        queryset = queryset.filter(description__icontains=word)

            # カテゴリでの絞り込み
            category = form.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # search formを渡す
        context['search_form'] = self.form

        return context


class CreateIncomeView(CreateView):
    template_name = 'mainapp/register.html'
    model = Income
    form_class = IncomeCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = '収入登録'
        return context

    def get_success_url(self):
        return reverse_lazy('list-income')

     # バリデーション時にメッセージを保存
    def form_valid(self, form):
        self.object = income = form.save()
        messages.info(self.request,
                      f'収入を登録しました\n'
                      f'日付:{income.date}\n'
                      f'カテゴリ:{income.category}\n'
                      f'金額:{income.price}円')
        return redirect(self.get_success_url())


class CreatePaymentView(CreateView):
    template_name = 'mainapp/register.html'
    model = Payment
    form_class = PaymentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = '支出登録'
        return context

    def get_success_url(self):
        return reverse_lazy('list-payment')

     # バリデーション時にメッセージを保存
    def form_valid(self, form):
        self.object = payment = form.save()
        messages.info(self.request,
                      f'支出を登録しました\n'
                      f'日付:{payment.date}\n'
                      f'カテゴリ:{payment.category}\n'
                      f'金額:{payment.price}円')
        return redirect(self.get_success_url())


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
