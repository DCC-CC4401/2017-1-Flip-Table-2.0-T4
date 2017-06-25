from django.conf.urls import url
from mainpage import views
from mainpage.views import ClientCreateView

app_name = 'products'
urlpatterns = [

    url(r'^gestionproductos/$', views.gestionproductos, name='gestionproductos'),
    url(r'^vendedorprofilepage/$', views.vendedorprofilepage, name='vendedorprofilepage'),
    url(r'^formView/', views.formView, name='formView'),
    url(r'^productoReq/', views.productoReq, name='productoReq'),
    url(r'^vistaVendedorPorAlumno/', views.vistaVendedorPorAlumno, name='vistaVendedorPorAlumno'),
    url(r'^cambiarEstado/$', views.cambiarEstado, name='cambiarEstado'),
    url(r'^borrarProducto/', views.borrarProducto, name='borrarProducto'),
    url(r'^editarProducto/', views.editarProducto, name='editarProducto'),
    url(r'^cambiarFavorito/', views.cambiarFavorito, name='cambiarFavorito'),
    url(r'^vistaVendedorPorAlumnoSinLogin/', views.vistaVendedorPorAlumnoSinLogin,
        name='vistaVendedorPorAlumnoSinLogin'),
    url(r'^getStock/$', views.getStock, name='getStock'),
    url(r'^createTransaction/$', views.createTransaction, name='createTransaction'),
    url(r'^fijoDashboard/$', views.fijoDashboard, name='fijoDashboard'),
    url(r'^ambulanteDashboard/$', views.ambulanteDashboard, name='ambulanteDashboard')

]
