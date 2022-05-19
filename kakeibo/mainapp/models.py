from django.db import models


class PaymentCategory(models.Model):
    name = models.CharField('カテゴリ名', max_length=32)
