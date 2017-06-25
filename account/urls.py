from django.conf.urls import url
from account import views
from account.views import AccountCreateView, ClientCreateView, PeddlerCreateView, EstablishedCreateView

app_name = 'account'

urlpatterns = [

    # account/
    url(r'^register/$', AccountCreateView.as_view(), name='register'),
    url(r'^register/client/$', ClientCreateView.as_view(), name='register_client'),
    url(r'^register/peddler/$', PeddlerCreateView.as_view(), name='register_peddler'),
    url(r'^register/established/$', EstablishedCreateView.as_view(), name='register_established'),

    # url(r'^$', views.index, name='index'),
]
