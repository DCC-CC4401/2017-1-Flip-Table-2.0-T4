from django.conf.urls import url
from account import views
from account.views import AccountCreateView, ClientCreateView, PeddlerCreateView, EstablishedCreateView, ClientUpdateView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [

    # account/
    url(r'^register/$', AccountCreateView.as_view(), name='register'),
    url(r'^register/client/$', ClientCreateView.as_view(), name='register_client'),
    url(r'^register/peddler/$', PeddlerCreateView.as_view(), name='register_peddler'),
    url(r'^register/established/$', EstablishedCreateView.as_view(), name='register_established'),
    url(r'^register/([0-9A-Za-z_\/-]+)/success$', views.success, name='success'),
    url(r'^edit/(?P<pk>\d+)/$', ClientUpdateView.as_view(), name='edit_user'),
    #url(r'^edit/client$', views.edit_client, name='edit_client'),

    #url(r'^edit/peddler$', views.edit_peddler, name='edit_peddler'),

    #url(r'^edit/established$', views.edit_established, name='edit_established'),
    # /account/login
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'},
        name='login'),

    # /account/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/account/login'}, name='logout'),

    # url(r'^$', views.index, name='index'),
]
