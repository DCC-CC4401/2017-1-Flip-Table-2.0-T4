from django.db import models
from django.contrib.auth.models import User


class Account(User):
    image = models.ImageField()
    lt = models.FloatField(default=False)
    lng = models.FloatField(default=False)

    def __str__(self):
        return "Account - " + self.username


class Seller(Account):
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    social = models.BooleanField(default=False)

    def __str__(self):
        return "Seller - " + self.username


class Peddler(Seller):
    available = models.BooleanField(default=False)

    def __str__(self):
        return "Peddler - " + self.username

    class Meta:
        verbose_name = 'Peddler'
        verbose_name_plural = 'Peddlers'

    def is_available(self):
        return self.available


class Established(Seller):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return "Established - " + self.username

    class Meta:
        verbose_name = 'Established'
        verbose_name_plural = 'Established'

    def is_available(self):
        return


class Client(Account):
    f_peddler = models.ManyToManyField(Peddler, blank=True)
    f_established = models.ManyToManyField(Established, blank=True)

    def __str__(self):
        return "Client - " + self.username

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
