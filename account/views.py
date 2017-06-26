from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm
from account.models import Client, Peddler, Established


class AccountCreateView(TemplateView):
    template_name = 'account/register_base.html'


class ClientCreateView(CreateView):
    template_name = 'account/register_client.html'
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'account/edit-client.html'
    fields = ['first_name', 'last_name', 'email', 'f_peddler', 'f_established', 'image']

    def form_valid(self, form):
        self.object = form.save()
        self.object.image = form.cleaned_data['image']
        print(form.cleaned_data)
        print(super(ClientUpdateView, self).get_form_class())
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('homepage:index')


class PeddlerCreateView(CreateView):
    template_name = 'account/register_peddler.html'
    form_class = PeddlerCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class PeddlerUpdateView(UpdateView):
    model = Peddler
    template_name = 'account/edit-peddler.html'
    fields = ['first_name', 'last_name', 'email', 'image', 'cash', 'credit', 'debit', 'social']

    def get_success_url(self):
        return reverse('homepage:index')


class EstablishedCreateView(CreateView):
    template_name = 'account/register_established.html'
    form_class = EstablishedCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class EstablishedUpdateView(UpdateView):
    model = Established
    template_name = 'account/edit-established.html'
    fields = ['first_name', 'last_name', 'email', 'image', 'cash', 'credit', 'debit', 'social', 'start', 'end']

    def get_success_url(self):
        return reverse('homepage:index')


@login_required(login_url='/account/login')
def edit_user(request, pk):
    if Peddler.objects.filter(id=pk).exists():
        return redirect('account:edit-peddler', pk)
    elif Client.objects.filter(id=pk).exists():
        return redirect('account:edit-client', pk)
    elif Established.objects.filter(id=pk).exists():
        return redirect('account:edit-established',pk)
    else:
        return redirect('homepage:index')


def success(request, algo):
    messages.add_message(request, messages.SUCCESS, "¡Has sido registrado con éxito!")
    return redirect('homepage:index')


@login_required(login_url='/account/login')
def delete_user(request):
    return render(request, 'account/delete.html')


@login_required(login_url='/account/login')
def confirm_deleted(request):
    request.user.delete()
    messages.add_message(request, messages.SUCCESS, "Usuario eliminado exitosamente")
    return render(request, 'account/deleted_confirmation.html')
