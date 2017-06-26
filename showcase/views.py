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
from django.views import View
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
        context['is_client'] = self.request.user.is_authenticated() and Client.objects.filter(
            pk=self.request.user.id).exists()
        context['is_favorite'] = self.object.client_set.filter(pk=self.request.user.id).exists()
        context['in_own_showcase'] = self.request.user.is_authenticated() and self.request.user.id == self.object.id
        context['dishes'] = self.object.dish_set.all()
        return context

    def get_object(self, queryset=None):
        seller_id = self.kwargs.get(self.pk_url_kwarg)
        if Peddler.objects.filter(pk=seller_id).exists():
            return Peddler.objects.get(pk=seller_id)
        else:
            return get_object_or_404(Established, pk=seller_id)


# class Favorite(View):
#     def get(self, request, pk):
#         client = get_object_or_404(Client, pk=pk)
#         if Peddler.objects.filter(pk=pk).exists():
#             seller = Peddler.objects.get(pk=pk)
#             if client.f_peddler.filter(id=seller.id).exists():
#                 client.f_peddler.remove(seller)
#             else:
#                 client.f_peddler.add(seller)
#         else:
#             seller = Established.objects.get(pk=pk)
#             if client.f_established.filter(id=seller.id).exists():
#                 client.f_established.remove(seller)
#             else:
#                 client.f_established.add(seller)
#         client.save()
#         return HttpResponse(status=204)
class FavoriteView(View):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=request.user.id)
        if Peddler.objects.filter(pk=pk).exists():
            seller = Peddler.objects.get(pk=pk)
            if client.f_peddler.filter(id=seller.id).exists():
                client.f_peddler.remove(seller)
            else:
                client.f_peddler.add(seller)
        else:
            seller = Established.objects.get(pk=pk)
            if client.f_established.filter(id=seller.id).exists():
                client.f_established.remove(seller)
            else:
                client.f_established.add(seller)
        client.save()
        return HttpResponse(status=204)

def favorite_seller(request, seller_id):
    # user = get_object_or_404(User, id=seller_id)
    # client = get_object_or_404(Client, user=request.user)
    # if Peddler.objects.filter(user=user).exists():
    #     seller = Peddler.objects.get(user=user)
    #     if client.f_peddler.filter(id=seller.id).exists():
    #         client.f_peddler.remove(seller)
    #     else:
    #         client.f_peddler.add(seller)
    # elif Established.objects.filter(user=user).exists():
    #     seller = Established.objects.get(user=user)
    #     if client.f_established.filter(id=seller.id).exists():
    #         client.f_established.remove(seller)
    #     else:
    #         client.f_established.add(seller)
    # client.save()
    return HttpResponse(status=204)


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

def statistics(request):
    return render(request, 'homepage/map.html')


def check_in(request, seller_id):
    seller_profile = get_object_or_404(Peddler, id=seller_id)
    if seller_profile.available:
        seller_profile.available = False
    else:
        seller_profile.available = True
    seller_profile.save()
    return HttpResponse(status=204)