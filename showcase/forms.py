from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from pip._vendor.requests.api import request

from account.models import Client, Peddler, Established
from showcase.models import Dish


class DishForm(forms.ModelForm):
    CHOICES = (
        ('1', 'bread.png',),
        ('2', 'breakfast.png',),
        ('3', 'burger.png',),
        ('4', 'chicken.png',),
        ('5', 'chicken2.png',),
        ('6', 'chocolate.png',),
        ('7', 'coke.png',),
        ('8', 'cupcake.png',),
        ('9', 'donut.png',),
        ('10', 'jelly.png',),
        ('11', 'fish.png',),
        ('12', 'fries.png',),
        ('13', 'hot-dog.png',),
        ('14', 'icecream.png',),
        ('15', 'juice.png',),
        ('16', 'lettuce.png',),
        ('17', 'pizza.png',),
        ('18', 'spaguetti.png',),
        ('19', 'rice.png',))
    choices = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)

    class Meta:
        model = Dish
        fields = ['name', 'image', 'description', 'stock', 'price']
