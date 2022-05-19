from unicodedata import category
from django.db import models
import datetime

INCOME_CATEGORY = (('salary', '給料'), ('sideline', '副業'))
PAYMENT_CATEGORY = (('Food expenses', '食費'),
                    ('Utility bills', '水道光熱費'),
                    ('Hobbies / Entertainment', '趣味・娯楽'))
MONTH = (('1', '1月'), ('2', '2月'), ('3', '3月'), ('4', '4月'),
         ('5', '5月'), ('6', '6月'), ('7', '7月'), ('8', '8月'),
         ('9', '9月'), ('10', '10月'), ('11', '11月'), ('12', '12月'))


def month_get():
    dt_mon = datetime.datetime.now().month
    # print(MONTH[dt_mon-1][1])
    return MONTH[dt_mon-1][1]


class Income(models.Model):
    month_get()
    month = models.CharField(
        max_length=100, choices=MONTH)
    price = models.IntegerField('金額')
    category = models.CharField(max_length=100, choices=INCOME_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)


class Payment(models.Model):
    month = models.CharField(max_length=100, choices=MONTH)
    price = models.IntegerField('金額')
    category = models.CharField(max_length=100, choices=PAYMENT_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)
