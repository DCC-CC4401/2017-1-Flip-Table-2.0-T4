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
        favorites = f_p + f_e
    is_authenticated = account.is_authenticated()
    sellers = Seller.objects.all()
    if is_authenticated:
        if Account.objects.filter(pk=account.pk).exists():
            account = Account.objects.get(pk=account.pk)
            print(account.lt)
            print(account.lng)
    print(favorites[0].is_available())

    return {'account': account, 'is_client': is_client, 'is_authenticated': is_authenticated, 'sellers': sellers,
            'favorites': favorites}


def update_pos(request):
    pos = {}
    if Account.objects.filter(pk=request.user.pk).exists():
        res = req.get('http://freegeoip.net/json')
        pos = res.json()
        acc = Account.objects.get(pk=request.user.pk)
        acc.lt = pos['latitude']
        acc.lng = pos['longitude']
        if Seller.objects.filter(pk=request.user.pk).exists():
            acc.lng -= random.randrange(-1, 1) * 5
            acc.lt -= random.randrange(-1, 1) * 5
        acc.save()
    return {'pos': pos}
