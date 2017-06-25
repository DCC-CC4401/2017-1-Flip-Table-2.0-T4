from django.conf.urls import url
from mainpage import views
from mainpage.views import ClientCreateView

urlpatterns = [

    url(r'^$', views.index, name='index')

]
