from account.models import Account, Peddler, Established, Client
from account.models import Account, Peddler, Established, Client, Seller
import requests as req
import random


def get_context(request):
    account = request.user
    favorites = []
    is_client = False
    if Client.objects.filter(pk=account.pk).exists():
        is_client = True
        f_p = list(Client.objects.get(pk=account.pk).f_peddler.all())
        f_e = list(Client.objects.get(pk=account.pk).f_established.all())
        favorites = [i.pk for i in f_p] + [i.pk for i in f_e]
    is_authenticated = account.is_authenticated()
    peddlers = Peddler.objects.all()
    established = Established.objects.all()
    only_favs = False
    if is_authenticated:
        try:
            client = Client.objects.get(pk=account.pk)
            only_favs = client.only_favs
            is_client = True
        except:
            is_client = False

        if Account.objects.filter(pk=account.pk).exists():
            account = Account.objects.get(pk=account.pk)
    print(favorites)
    return {'account': account, 'is_client': is_client, 'is_authenticated': is_authenticated, 'peddlers': peddlers,
            'established': established, 'favorites': favorites, 'only_favs':only_favs}


def update_pos(request):
    res = req.get('http://freegeoip.net/json')
    pos = res.json()
    lt = pos['latitude']
    lng = pos['longitude']
    if Account.objects.filter(pk=request.user.pk).exists():
        acc = Account.objects.get(pk=request.user.pk)
        acc.lt = lt
        acc.lng = lng
        if Seller.objects.filter(pk=request.user.pk).exists():
            acc.lng -= random.random() * .001 * (1 if random.random() > 0.5 else -1)
            acc.lt -= random.random() * .001 * (1 if random.random() > 0.5 else -1)
        acc.save()
    return {'pos': pos, 'lt':lt, 'lng':lng}
