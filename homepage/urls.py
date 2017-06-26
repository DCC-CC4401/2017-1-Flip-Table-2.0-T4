from django.conf.urls import url
from homepage import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gestionproductos/$', views.gestionproductos, name='gestionproductos'),
    url(r'^vendedorprofilepage/$', views.vendedorprofilepage, name='vendedorprofilepage'),
    url(r'^productoReq/', views.productoReq, name='productoReq'),
    url(r'^vistaVendedorPorAlumno/', views.vistaVendedorPorAlumno, name='vistaVendedorPorAlumno'),
    url(r'^borrarProducto/', views.borrarProducto, name='borrarProducto'),
    url(r'^editarProducto/', views.editarProducto, name='editarProducto'),
    url(r'^cambiarFavorito/', views.cambiarFavorito, name='cambiarFavorito'),
    url(r'^agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    url(r'^getStock/$', views.getStock, name='getStock'),
    url(r'^createTransaction/$', views.createTransaction, name='createTransaction'),
    url(r'^fijoDashboard/$', views.fijoDashboard, name='fijoDashboard'),
    url(r'^ambulanteDashboard/$', views.ambulanteDashboard, name='ambulanteDashboard'),

]
