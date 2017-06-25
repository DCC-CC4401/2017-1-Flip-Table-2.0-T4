from django.conf.urls import url
from mainpage import views
from mainpage.views import ClientCreateView
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^loginReq/', views.loginReq, name='loginReq'),
    url(r'^register/client/$', ClientCreateView.as_view(), name='register_client'),
    url(r'^register/', views.register, name='register'),
    url(r'^loggedin/', views.loggedin, name='loggedin'),
    url(r'^editarVendedor/$', views.editarVendedor, name='editarVendedor'),
    url(r'^editarDatos/$', views.editarDatos, name='editarDatos'),
    url(r'^inicioAlumno/', views.inicioAlumno, name='inicioAlumno'),
    url(r'^borrarUsuario/', views.borrarUsuario, name='borrarUsuario'),
    url(r'^editarPerfilAlumno/', views.editarPerfilAlumno, name='editarPerfilAlumno'),
    url(r'^procesarPerfilAlumno/', views.procesarPerfilAlumno, name='procesarPerfilAlumno'),
    url(r'^editarUsuario/', views.editarUsuario, name='editarUsuario'),
    url(r'^agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),
    url(r'^registerAdmin/$', views.registerAdmin, name='registerAdmin'),
    url(r'^verificarEmail/$', views.verificarEmail, name='verificarEmail'),

    # /users/login
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # /users/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/users/login'}, name='logout'),
]