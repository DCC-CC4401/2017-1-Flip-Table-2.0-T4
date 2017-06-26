import datetime
import simplejson
from django.shortcuts import get_object_or_404
from django.shortcuts import render, reverse
from django.utils import timezone
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from account.models import Client, Peddler, Established, Seller
from showcase.models import Dish

from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from showcase.forms import DishForm


class SellerDetailView(DetailView):
    template_name = 'showcase/showcase.html'
    context_object_name = 'seller'

    def get_context_data(self, **kwargs):
        context = super(SellerDetailView, self).get_context_data(**kwargs)
        context['is_peddler'] = hasattr(self.object, 'peddler')
        context['dishes'] = self.object.dish_set.all()
        return context

    def get_object(self, queryset=None):
        id = self.kwargs.get(self.pk_url_kwarg)
        if Peddler.objects.filter(pk=id).exists():
            return Peddler.objects.get(pk=id)
        else:
            return get_object_or_404(Established, pk=id)


class DishCreateView(CreateView):
    template_name = 'showcase/dish.html'
    form_class = DishForm
    model = Dish
    context_object_name = 'dish'

    def form_valid(self, form):
        form.instance.seller = get_object_or_404(Seller, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.icon = "img/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
        return super(DishCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('showcase:seller_detail', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        context['can_delete'] = False
        return context


class DishUpdateView(UpdateView):
    template_name = 'showcase/dish.html'
    form_class = DishForm
    model = Dish
    context_object_name = 'dish'

    def get_object(self, queryset=None):
        return Dish.objects.get(pk=self.kwargs['dish_id'])

    def form_valid(self, form):
        form.instance.seller = get_object_or_404(Seller, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.icon = "img/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
        return super(DishUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('showcase:seller_detail', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def get_context_data(self, **kwargs):
        context = super(DishUpdateView, self).get_context_data(**kwargs)
        context['can_delete'] = True
        return context


class DishDeleteView(DeleteView):
    model = Dish

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_object(self, queryset=None):
        return Dish.objects.get(pk=self.kwargs['dish_id'])

    def get_success_url(self):
        return reverse('showcase:seller_detail', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


def favorite_seller(request, seller_id):
    if Peddler.objects.filter(pk=seller_id).exists():
        seller = Peddler.objects.filter(pk=seller_id)
        is_peddler = True
    else:
        seller = get_object_or_404(Established, pk=seller_id)
        is_peddler = False
    client = get_object_or_404(Client, pk=request.user.id)
    if is_peddler:
        if seller in client.f_peddler.all():
            client.f_peddler.remove(seller)
        else:
            client.f_peddler.add(seller)
    else:
        if seller in client.f_established.all():
            client.f_established.remove(seller)
        else:
            client.f_established.add(seller)
    client.save()
    return HttpResponse(status=204)


def statistics(request):
    return render(request, 'homepage/map.html')
