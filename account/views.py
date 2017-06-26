from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm
from account.models import Client


class AccountCreateView(TemplateView):
    template_name = 'account/register_base.html'


class ClientCreateView(CreateView):
    template_name = 'account/register_client.html'
    form_class = ClientCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


class ClientUpdateView(UpdateView):
    model = Client
    template_name_suffix = '_update_form'
    fields = ['first_name', 'last_name', 'email', 'image', 'favorite_peddlers', 'favorite_established']

    def get_success_url(self):
        return reverse('homepage:index')


class PeddlerCreateView(CreateView):
    template_name = 'account/register_peddler.html'
    form_class = PeddlerCreateForm

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(PeddlerCreateView, self).form_valid(form)


class EstablishedCreateView(CreateView):
    template_name = 'account/register_established.html'
    form_class = EstablishedCreateForm

    def get_success_url(self):
        return reverse('homepage:index')


def editarPerfilAlumno(request):
    avatar = request.session['avatar']
    id = request.session['id']
    nombre = request.session['nombre']
    favoritos = []
    nombres = []
    for fav in Favoritos.objects.all():
        if id == fav.idAlumno:
            favoritos.append(fav.idVendedor)
            vendedor = Usuario.objects.filter(id=fav.idVendedor).get()
            nombre = vendedor.nombre
            nombres.append(nombre)
    return render(request, 'main/edit-profile.html',
                  {"id": id, "avatarSesion": avatar, "nombre": nombre, "favoritos": favoritos, "nombres": nombres,
                   "nombresesion": request.session['nombre']})


def success(request, algo):
    messages.add_message(request, messages.SUCCESS, "¡Has sido registrado con éxito!")
    return redirect('homepage:index')
