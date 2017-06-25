import datetime
from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic.edit import FormView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm


class AccountCreateView(TemplateView):
    template_name = 'account/register_base.html'


class ClientCreateView(FormView):
    template_name = 'account/register_client.html'
    form_class = ClientCreateForm
    success_url = 'mainpage/'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(ClientCreateView, self).form_valid(form)


class PeddlerCreateView(FormView):
    template_name = 'account/register_peddler.html'
    form_class = PeddlerCreateForm
    success_url = 'mainpage/'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(PeddlerCreateView, self).form_valid(form)


class EstablishedCreateView(FormView):
    template_name = 'account/register_established.html'
    form_class = EstablishedCreateForm
    success_url = 'mainpage/'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(EstablishedCreateView, self).form_valid(form)
