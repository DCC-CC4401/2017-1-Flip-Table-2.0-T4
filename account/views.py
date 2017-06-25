import datetime
import simplejson
from django.shortcuts import render
from django.utils import timezone
from .forms import GestionProductosForm, editarProductosForm
from .models import Usuario, Comida, Favoritos, Imagen, Transacciones
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.generic.edit import FormView
from mainpage.forms import ClientCreateForm


def loginReq(request):
    # inicaliar variables
    tipo = 0
    nombre = ''
    url = ''
    id = 0
    horarioIni = 0
    horarioFin = 0
    encontrado = False
    email = request.POST.get("email")
    avatar = ''
    contraseña = ''
    password = request.POST.get("password")
    listaDeProductos = []
    formasDePago = []
    activo = False

    # buscar vendedor en base de datos
    MyLoginForm = LoginForm(request.POST)
    if MyLoginForm.is_valid():
        vendedores = []
        for p in Usuario.objects.all():
            if p.contraseña == password and p.email == email:
                tipo = p.tipo
                nombre = p.nombre
                if (tipo == 0):
                    url = 'mainpage/baseAdmin.html'
                    id = p.id
                    tipo = p.tipo
                    encontrado = True
                    avatar = p.avatar
                    contraseña = p.contraseña
                    break
                elif (tipo == 1):
                    url = 'mainpage/baseAlumno.html'
                    id = p.id
                    avatar = p.avatar
                    tipo = p.tipo
                    encontrado = True
                    avatar = p.avatar

                    break
                elif (tipo == 2):
                    url = 'mainpage/vendedor-fijo.html'
                    id = p.id
                    tipo = p.tipo
                    encontrado = True
                    horarioIni = p.horarioIni
                    horarioFin = p.horarioFin
                    request.session['horarioIni'] = horarioIni
                    request.session['horarioFin'] = horarioFin
                    avatar = p.avatar
                    activo = p.activo
                    formasDePago = p.formasDePago
                    request.session['formasDePago'] = formasDePago
                    request.session['activo'] = activo
                    break
                elif (tipo == 3):
                    url = 'mainpage/vendedor-ambulante.html'
                    id = p.id
                    tipo = p.tipo
                    encontrado = True
                    avatar = p.avatar
                    activo = p.activo
                    formasDePago = p.formasDePago
                    request.session['formasDePago'] = formasDePago
                    request.session['activo'] = activo
                    break

        # si no se encuentra el usuario, se retorna a pagina de login
        if encontrado == False:
            return render(request, 'main/login.html', {"error": "Usuario o contraseña invalidos"})

        # crear datos de sesion
        request.session['id'] = id
        request.session['tipo'] = tipo
        request.session['email'] = email
        request.session['nombre'] = nombre
        request.session['avatar'] = str(avatar)
        # si son vendedores, crear lista de productos
        for p in Usuario.objects.all():
            if p.tipo == 2 or p.tipo == 3:
                vendedores.append(p.id)
        vendedoresJson = simplejson.dumps(vendedores)

        # obtener alimentos en caso de que sea vendedor fijo o ambulante
        if tipo == 2 or tipo == 3:
            i = 0
            for producto in Comida.objects.all():
                if producto.idVendedor == id:
                    listaDeProductos.append([])
                    listaDeProductos[i].append(producto.nombre)
                    categoria = str(producto.categorias)
                    listaDeProductos[i].append(categoria)
                    listaDeProductos[i].append(producto.stock)
                    listaDeProductos[i].append(producto.precio)
                    listaDeProductos[i].append(producto.descripcion)
                    listaDeProductos[i].append(str(producto.imagen))
                    i += 1

        listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')

        # limpiar argumentos de salida segun tipo de vista
        argumentos = {"email": email, "tipo": tipo, "id": id, "vendedores": vendedoresJson, "nombre": nombre,
                      "horarioIni": horarioIni, "horarioFin": horarioFin, "avatar": avatar,
                      "listaDeProductos": listaDeProductos}
        if (tipo == 0):
            request.session['contraseña'] = contraseña
            return adminPOST(id, avatar, email, nombre, contraseña, request)
        if (tipo == 1):
            argumentos = {"nombresesion": nombre, "tipo": tipo, "id": id, "vendedores": vendedoresJson,
                          "avatarSesion": avatar}
        if (tipo == 2):
            request.session['listaDeProductos'] = str(listaDeProductos)
            request.session['favoritos'] = obtenerFavoritos(id)
            argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "horarioIni": horarioIni,
                          "favoritos": obtenerFavoritos(id), "horarioFin": horarioFin, "avatar": avatar,
                          "listaDeProductos": listaDeProductos, "activo": activo, "formasDePago": formasDePago,
                          "activo": activo}
        if (tipo == 3):
            request.session['listaDeProductos'] = str(listaDeProductos)
            request.session['favoritos'] = obtenerFavoritos(id)
            argumentos = {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar, "favoritos": obtenerFavoritos(id),
                          "listaDeProductos": listaDeProductos, "activo": activo, "formasDePago": formasDePago}

        # enviar a vista respectiva de usuario
        return render(request, url, argumentos)

    # retornar en caso de datos invalidos
    else:
        return render(request, 'main/login.html', {"error": "Usuario o contraseña invalidos"})


def signup(request):
    return render(request, 'main/signup.html', {})


def signupAdmin(request):
    return render(request, 'main/signupAdmin.html', {})

def login(request):
    return render(request, 'main/login.html', {})

def loggedin(request):
    return render(request, 'main/loggedin.html', {})