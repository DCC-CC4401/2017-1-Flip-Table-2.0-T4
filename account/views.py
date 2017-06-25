import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm



class AccountCreateView(TemplateView):
    template_name = 'account/register_base.html'


class ClientCreateView(FormView):
    template_name = 'account/register_client.html'
    form_class = ClientCreateForm
    success_url = 'success'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(ClientCreateView, self).form_valid(form)


class PeddlerCreateView(FormView):
    template_name = 'account/register_peddler.html'
    form_class = PeddlerCreateForm
    success_url = 'success'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(PeddlerCreateView, self).form_valid(form)


class EstablishedCreateView(FormView):
    template_name = 'account/register_established.html'
    form_class = EstablishedCreateForm
    success_url = 'success'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super(EstablishedCreateView, self).form_valid(form)

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