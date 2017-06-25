from account.models import Account


def get_account(request):
    account = request.user
    is_client = False
    is_authenticated = account.is_authenticated()
    if is_authenticated:
        if Account.objects.filter(pk=account.pk).exists():
            account = Account.objects.get(pk=account.pk)

    return {'account': account, 'is_client': is_client, 'is_authenticated': is_authenticated}
