import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

from django.views.generic.edit import FormView, CreateView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm


class AccountCreateView(TemplateView):
    template_name = 'account/register_base.html'


class ClientCreateView(CreateView):
    template_name = 'account/register_client.html'
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class PeddlerCreateView(CreateView):
    template_name = 'account/register_peddler.html'
    form_class = PeddlerCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class EstablishedCreateView(CreateView):
    template_name = 'account/register_established.html'
    form_class = EstablishedCreateForm

    def get_success_url(self):
        return reverse('homepage:index')
