from django.db import models
from account.models import Seller
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    icon = models.ImageField()
    image = models.ImageField()
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.CharField(max_length=300)
    stock = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    visible = models.BooleanField(default=True)
    sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Statistics(models.Model):
    transactions = models.ManyToManyField(Transaction, blank=True)

    def __init__(self, *args, **kwargs):
        super(Statistics, self).__init__(*args, **kwargs)

    def get(self):
        return None


class MonthlyStatistics(Statistics):
    MonthlyRevenue = models.PositiveIntegerField(default=0)
    Month = models.PositiveSmallIntegerField()

    def __init__(self, *args, **kwargs):
        super(MonthlyStatistics, self).__init__(*args, **kwargs)
        self.MonthlyRevenue = 0
        for item in self.transactions.all():
            print(item.date.month)
            if self.Month == str(item.date.month):
                self.MonthlyRevenue += item.price * item.quantity

    def __unicode__(self):
        return u'%d %s' % (self.MonthlyRevenue, self.Month)


