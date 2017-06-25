import datetime
import simplejson
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from account.models import Client, Peddler, Established
from showcase.models import Dish


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
