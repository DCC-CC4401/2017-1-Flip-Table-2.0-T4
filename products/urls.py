from django.conf.urls import url
from products import views

app_name = 'products'

urlpatterns = [

    url(r'^(?P<seller_id>[0-9]+)/$', views.showcase, name='showcase'),
    url(r'^statistics/$', views.statistics, name='statistics'),

]
