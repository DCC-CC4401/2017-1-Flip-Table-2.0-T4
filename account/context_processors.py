from account.models import Account, Peddler, Established, Client


def get_account(request):
    account = request.user
    is_client = False
    is_authenticated = account.is_authenticated()
    peddlers = Peddler.objects.all()
    established = Established.objects.all()
    if is_authenticated:
        try:
            client = Client.objects.get(pk=account.pk)
            is_client = True
        except:
            is_client = False

        if Account.objects.filter(pk=account.pk).exists():
            account = Account.objects.get(pk=account.pk)

    return {'account': account, 'is_client': is_client, 'is_authenticated': is_authenticated, 'peddlers': peddlers,
            'established': established}
