import datetime
import simplejson
import pusher
from account.models import Seller
from account.models import Account, Client
from .forms import GestionProductosForm, editarProductosForm
from django.db.models import Count, Sum
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views import View

from django.views.generic.edit import FormView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm


def index(request):
    return render(request, 'main/map.html')


class FavoriteFilter(View):
    def get(self, request, id):
        profile = get_object_or_404(Client, id=id)
        if profile.only_favs:
            profile.only_favs = False
        else:
            profile.only_favs = True
        profile.save()
        return redirect('homepage:index')


def police_alert(request):
    pusher_client = pusher.Pusher(
        app_id='358820',
        key='9642b940d4a78fd8dd49',
        secret='65ff5b5b0f16b52dc8f7',
        cluster='us2',
        ssl=True
    )

    pusher_client.trigger('police_channel', 'police_alert', {'message': 'Policias cerca!'})
    return HttpResponse(status=204)
