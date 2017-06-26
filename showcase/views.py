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

from django.views.generic.edit import FormView, CreateView

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
    template_name = 'showcase/dish_create.html'
    form_class = DishForm
    model = Dish

    # def get_form_kwargs(self):
    #     # pass "user" keyword argument with the current user to your form
    #     kwargs = super(DishCreateView, self).get_form_kwargs()
    #     kwargs['seller'] = get_object_or_404(Seller, pk=self.kwargs.get(self.pk_url_kwarg))
    #     return kwargs

    def form_valid(self, form):
        form.instance.seller = get_object_or_404(Seller, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.icon = "static/img/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
        return super(DishCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('showcase:seller_detail', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


def create_dish(request, seller_id):
    form = DishForm(request.POST or None, request.FILES or None)
    user = get_object_or_404(User, id=seller_id)
    if form.is_valid():
        dishes = user.dish_set.all()
        for dish in dishes:
            if dish.name == form.cleaned_data['name']:
                context = {
                    'form': form,
                    'error_message': 'Ya tienes un plato con este nombre',
                }
                return render(request, 'create_dish.html', context)
        dish = form.save(commit=False)
        dish.icon = "default/" + dict(form.fields['choices'].choices)[form.cleaned_data['choices']]
        dish.user = user
        dish.image = request.FILES['image']
        dish.save()
        return redirect('showcase:showcase', seller_id)
    context = {
        'form': form,
    }
    return render(request, 'create_dish.html', context)


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
