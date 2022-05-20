from unicodedata import category
from django.db import models
import datetime

INCOME_CATEGORY = (('salary', '給料'), ('sideline', '副業'))
PAYMENT_CATEGORY = (('Food expenses', '食費'),
                    ('Utility bills', '水道光熱費'),
                    ('Hobbies / Entertainment', '趣味・娯楽'))
MONTH = (('January', '1月'), ('February', '2月'), ('March', '3月'), ('April', '4月'),
         ('May', '5月'), ('June', '6月'), ('July', '7月'), ('August', '8月'),
         ('Semptember', '9月'), ('October', '10月'), ('November', '11月'), ('December', '12月'))


def month_get():
    dt_mon = datetime.datetime.now().month
    # print(MONTH[dt_mon-1][1])
    return MONTH[dt_mon-1][1]


class Income(models.Model):
    date = models.DateField('月')
    price = models.IntegerField('金額')
    category = models.CharField(max_length=100, choices=INCOME_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)

    def __str__(self):
        return str(self.date) + str(' ') + str(self.category)


class Payment(models.Model):
    date = models.DateField('月')
    price = models.IntegerField('金額')
    category = models.CharField(max_length=100, choices=PAYMENT_CATEGORY)
    description = models.TextField('摘要', null=True, blank=True)

    def __str__(self):
        return str(self.date) + str(' ') + str(self.category)
