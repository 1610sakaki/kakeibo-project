from unicodedata import category
from django.db import models
import datetime

INCOME_CATEGORY = (('給料', '給料'), ('賞与', '賞与'), ('副業', '副業'), ('臨時収入', '臨時収入'))
PAYMENT_CATEGORY = (('食費', '食費'),
                    ('外食費', '外食費'),
                    ('水道光熱費', '水道光熱費'),
                    ('通信費', '通信費'),
                    ('日用品費', '日用品費'),
                    ('住居備品費', '住居備品費'),
                    ('衣服', '衣服費'),
                    ('教養費', '教養費'),
                    ('趣味・娯楽', '趣味・娯楽'),
                    ('美容', '美容'),
                    ('医療費', '医療費'),
                    ('交際費', '交際費'),
                    ('交通費', '交通費'),
                    ('サブスクリプション費', 'サブスクリプション費'),
                    ('郵便・宅配・その他雑費', '郵便・宅配・その他雑費'),
                    ('保険代', '保険代'),)


class IncomeCategory(models.Model):
    name = models.CharField('カテゴリ名', max_length=32)

    def __str__(self):
        return self.name


class Income(models.Model):
    date = models.DateField('月')
    price = models.IntegerField('金額')
    category = models.CharField(
        'カテゴリー', max_length=100, choices=INCOME_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)

    def __str__(self):
        return str(self.date.strftime('%Y-%m')) + str(' ') + str(self.category)


class PaymentCategory(models.Model):
    name = models.CharField('カテゴリ名', max_length=32)

    def __str__(self):
        return self.name


class Payment(models.Model):
    date = models.DateField('月')
    price = models.IntegerField('金額')
    category = models.CharField(
        'カテゴリー', max_length=100, choices=PAYMENT_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)

    def __str__(self):
        return str(self.date) + str(' ') + str(self.category)
