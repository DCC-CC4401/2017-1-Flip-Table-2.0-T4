from django.conf.urls import url
from homepage import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gestionproductos/$', views.gestionproductos, name='gestionproductos'),
    url(r'^vendedorprofilepage/$', views.vendedorprofilepage, name='vendedorprofilepage'),
    url(r'^formView/', views.formView, name='formView'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^productoReq/', views.productoReq, name='productoReq'),
    url(r'^vistaVendedorPorAlumno/', views.vistaVendedorPorAlumno, name='vistaVendedorPorAlumno'),
    url(r'^cambiarEstado/$', views.cambiarEstado, name='cambiarEstado'),
    url(r'^editarVendedor/$', views.editarVendedor, name='editarVendedor'),
    url(r'^editarDatos/$', views.editarDatos, name='editarDatos'),
    url(r'^borrarUsuario/', views.borrarUsuario, name='borrarUsuario'),
    url(r'^borrarProducto/', views.borrarProducto, name='borrarProducto'),
    url(r'^editarProducto/', views.editarProducto, name='editarProducto'),
    url(r'^cambiarFavorito/', views.cambiarFavorito, name='cambiarFavorito'),
    url(r'^vistaVendedorPorAlumnoSinLogin/', views.vistaVendedorPorAlumnoSinLogin,
        name='vistaVendedorPorAlumnoSinLogin'),
    #url(r'^editarPerfilAlumno/', views.editarPerfilAlumno, name='editarPerfilAlumno'),
    url(r'^procesarPerfilAlumno/', views.procesarPerfilAlumno, name='procesarPerfilAlumno'),
    url(r'^editarUsuario/', views.editarUsuario, name='editarUsuario'),
    url(r'^agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    url(r'^getStock/$', views.getStock, name='getStock'),
    url(r'^verificarEmail/$', views.verificarEmail, name='verificarEmail'),
    url(r'^createTransaction/$', views.createTransaction, name='createTransaction'),
    url(r'^fijoDashboard/$', views.fijoDashboard, name='fijoDashboard'),
    url(r'^ambulanteDashboard/$', views.ambulanteDashboard, name='ambulanteDashboard'),

]
