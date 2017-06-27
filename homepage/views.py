import datetime
import simplejson
from account.models import Account
from .forms import GestionProductosForm, editarProductosForm
from django.db.models import Count, Sum
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import requests as req

from django.views.generic.edit import FormView
from account.forms import ClientCreateForm, PeddlerCreateForm, EstablishedCreateForm


def index(request):
    return render(request, 'main/map.html')

def gestionproductos(request):
    if request.session.has_key('id'):
        email = request.session['email']
        tipo = request.session['tipo']
        id = request.session['id']
        if tipo == 3:
            path = "main/baseVAmbulante.html"
        if tipo == 2:
            path = "main/baseVFijo.html"
    return render(request, 'main/agregar-productos.html', {"path": path})


def vendedorprofilepage(request):
    return render(request, 'main/vendedor-profile-page.html', {})


def productoReq(request):
    horarioIni = 0
    horarioFin = 0
    avatar = ""
    if request.method == "POST":
        if request.session.has_key('id'):
            id = request.session['id']
            email = request.session['email']
            tipo = request.session['tipo']
            if tipo == 3:
                path = "main/baseVAmbulante.html"
                url = "main/vendedor-ambulante.html"
            if tipo == 2:
                path = "main/baseVFijo.html"
                url = "main/vendedor-fijo.html"
            Formulario = GestionProductosForm(request.POST)
            if Formulario.is_valid():
                producto = Comida()
                producto.idVendedor = id
                producto.nombre = request.POST.get("nombre")
                producto.imagen = request.FILES.get("comida")
                producto.precio = request.POST.get("precio")
                producto.stock = request.POST.get("stock")
                producto.descripcion = request.POST.get("descripcion")
                producto.categorias = request.POST.get("categoria")
                producto.save()
            else:
                return render(request, 'main/agregar-productos.html',
                              {"path": path, "respuesta": "¡Ingrese todos los datos!"})

    # obtener alimentos en caso de que sea vendedor fijo o ambulante
    i = 0
    listaDeProductos = []
    for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
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

    for p in Usuario.objects.raw('SELECT * FROM usuario'):
        if p.id == id:
            avatar = p.avatar
            horarioIni = p.horarioIni
            horarioFin = p.horarioFin
            nombre = p.nombre
    return render(request, url, {"email": email, "tipo": tipo, "id": id, "nombre": nombre, "horarioIni": horarioIni,
                                 "horarioFin": horarioFin, "avatar": avatar, "listaDeProductos": listaDeProductos})


def vistaVendedorPorAlumno(request):
    if request.method == 'POST':
        id = int(request.POST.get("id"))
        for p in Usuario.objects.raw('SELECT * FROM usuario'):
            if p.id == id:
                favorito = 0
                for f in Favoritos.objects.raw('SELECT * FROM Favoritos'):
                    if request.session['id'] == f.idAlumno:
                        if id == f.idVendedor:
                            favorito = 1
                tipo = p.tipo
                nombre = p.nombre
                avatar = p.avatar
                formasDePago = p.formasDePago
                horarioIni = p.horarioIni
                horarioFin = p.horarioFin
                if tipo == 3:
                    url = 'main/vendedor-ambulante-vistaAlumno.html'
                    break
                if tipo == 2:
                    url = 'main/vendedor-fijo-vistaAlumno.html'
                    break
    # obtener alimentos
    i = 0
    listaDeProductos = []
    for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
        listaDeProductos.append([])
        listaDeProductos[i].append(producto.nombre)
        categoria = str(producto.categorias)
        listaDeProductos[i].append(categoria)
        listaDeProductos[i].append(producto.stock)
        listaDeProductos[i].append(producto.precio)
        listaDeProductos[i].append(producto.descripcion)
        listaDeProductos[i].append(str(producto.imagen))
        i += 1
    avatarSesion = request.session['avatar']
    listaDeProductos = simplejson.dumps(listaDeProductos, ensure_ascii=False).encode('utf8')
    return render(request, url, {"nombre": nombre, "nombresesion": request.session['nombre'], "tipo": tipo, "id": id,
                                 "avatar": avatar, "listaDeProductos": listaDeProductos, "avatarSesion": avatarSesion,
                                 "favorito": favorito, "formasDePago": formasDePago, "horarioIni": horarioIni,
                                 "horarioFin": horarioFin, })


def vistaVendedorPorAlumnoSinLogin(request):
    if request.method == 'POST':
        id = int(request.POST.get("id"))
        for p in Usuario.objects.raw('SELECT * FROM usuario'):
            if p.id == id:
                tipo = p.tipo
                nombre = p.nombre
                avatar = p.avatar
                formasDePago = p.formasDePago
                horarioIni = p.horarioIni
                horarioFin = p.horarioFin
                activo = p.activo
                if tipo == 3:
                    url = 'main/vendedor-ambulante-vistaAlumno-sinLogin.html'
                    break
                if tipo == 2:
                    url = 'main/vendedor-fijo-vistaAlumno-sinLogin.html'
                    break
                    # obtener alimentos
    i = 0
    listaDeProductos = []
    for producto in Comida.objects.raw('SELECT * FROM comida WHERE idVendedor = "' + str(id) + '"'):
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
    return render(request, url,
                  {"nombre": nombre, "tipo": tipo, "id": id, "avatar": avatar, "listaDeProductos": listaDeProductos,
                   "formasDePago": formasDePago, "horarioIni": horarioIni, "horarioFin": horarioFin, "activo": activo})


@csrf_exempt
def borrarProducto(request):
    if request.method == 'GET':
        if request.is_ajax():
            comida = request.GET.get('eliminar')
            Comida.objects.filter(nombre=comida).delete()
            data = {"eliminar": comida}
            return JsonResponse(data)


@csrf_exempt
def editarProducto(request):
    if request.method == 'POST':
        if request.is_ajax():
            form = editarProductosForm(data=request.POST, files=request.FILES)
            print(request.POST)
            print(request.FILES)
            nombreOriginal = request.POST.get("nombreOriginal")
            nuevoNombre = request.POST.get('nombre')
            nuevoPrecio = (request.POST.get('precio'))
            nuevoStock = (request.POST.get('stock'))
            nuevaDescripcion = request.POST.get('descripcion')
            nuevaCategoria = (request.POST.get('categoria'))
            nuevaImagen = request.FILES.get("comida")
            if nuevoPrecio != "":
                Comida.objects.filter(nombre=nombreOriginal).update(precio=int(nuevoPrecio))
            if nuevoStock != "":
                Comida.objects.filter(nombre=nombreOriginal).update(stock=int(nuevoStock))
            if nuevaDescripcion != "":
                Comida.objects.filter(nombre=nombreOriginal).update(descripcion=nuevaDescripcion)
            if nuevaCategoria != None:
                Comida.objects.filter(nombre=nombreOriginal).update(categorias=(nuevaCategoria))
            if nuevaImagen != None:
                filename = nombreOriginal + ".jpg"
                with default_storage.open('../media/productos/' + filename, 'wb+') as destination:
                    for chunk in nuevaImagen.chunks():
                        destination.write(chunk)
                Comida.objects.filter(nombre=nombreOriginal).update(imagen='/productos/' + filename)

            if nuevoNombre != "":
                if Comida.objects.filter(nombre=nuevoNombre).exists():
                    data = {"respuesta": "repetido"}
                    return JsonResponse(data)
                else:
                    Comida.objects.filter(nombre=nombreOriginal).update(nombre=nuevoNombre)

            data = {"respuesta": nombreOriginal}
            return JsonResponse(data)


def cambiarFavorito(request):
    if request.method == "GET":
        if request.is_ajax():
            favorito = request.GET.get('favorito')
            agregar = request.GET.get('agregar')
            if agregar == "si":
                nuevoFavorito = Favoritos()
                nuevoFavorito.idAlumno = request.session['id']
                nuevoFavorito.idVendedor = favorito
                nuevoFavorito.save()
                respuesta = {"respuesta": "si"}
            else:
                Favoritos.objects.filter(idAlumno=request.session['id']).filter(idVendedor=favorito).delete()
                respuesta = {"respuesta": "no"}
            return JsonResponse(respuesta)

            # return render_to_response('main/baseAdmin.html', {'form':form,'test':test}, context_instance=RequestContext(request))


def procesarPerfilAlumno(request):
    if request.method == "POST":
        nombreOriginal = request.session['nombre']
        nuevoNombre = request.POST.get("nombre")
        count = request.POST.get("switchs")
        aEliminar = []
        nuevaImagen = request.FILES.get("comida")
        for i in range(int(count)):
            fav = request.POST.get("switch" + str(i))
            if fav != "":
                aEliminar.append(fav)
        print(request.POST)
        print(request.FILES)
        print(aEliminar)

        if nuevoNombre != "":
            if Usuario.objects.filter(nombre=nuevoNombre).exists():
                data = {"respuesta": "repetido"}
                return JsonResponse(data)
            Usuario.objects.filter(nombre=nombreOriginal).update(nombre=nuevoNombre)

        for i in aEliminar:
            for fav in Favoritos.objects.raw("SELECT * FROM Favoritos"):
                if request.session['id'] == fav.idAlumno:
                    if int(i) == fav.idVendedor:
                        Favoritos.objects.filter(idAlumno=request.session['id']).filter(idVendedor=int(i)).delete()
        if nuevaImagen != None:
            filename = nombreOriginal + ".jpg"
            with default_storage.open('../media/avatars/' + filename, 'wb+') as destination:
                for chunk in nuevaImagen.chunks():
                    destination.write(chunk)
            Usuario.objects.filter(id=request.session['id']).update(avatar='/avatars/' + filename)

        return JsonResponse({"ejemplo": "correcto"})


@csrf_exempt
def agregarAvatar(request):
    if request.is_ajax() or request.method == 'FILES':
        imagen = request.FILES.get("image")
        print(request.FILES)
        nuevaImagen = Imagen(imagen=imagen)
        nuevaImagen.save()
        return HttpResponse("Success")


def getStock(request):
    if request.method == "GET":
        stock = request.GET.get("nombre")
        for producto in Comida.objects.raw("SELECT * FROM Comida"):
            if producto.nombre == request.GET.get("nombre"):
                stock = producto.stock
        if request.GET.get("op") == "suma":
            nuevoStock = stock + 1
            Comida.objects.filter(nombre=request.GET.get("nombre")).update(stock=nuevoStock)
        if request.GET.get("op") == "resta":
            nuevoStock = stock - 1
            if stock == 0:
                return JsonResponse({"stock": stock})
            Comida.objects.filter(nombre=request.GET.get("nombre")).update(stock=nuevoStock)
    return JsonResponse({"stock": stock})


def createTransaction(request):
    print("GET:")
    print(request.GET)
    nombreProducto = request.GET.get("nombre")
    precio = 0
    idVendedor = request.GET.get("idUsuario")
    if Comida.objects.filter(nombre=nombreProducto).exists():
        precio = Comida.objects.filter(nombre=nombreProducto).values('precio')[0]
        listaAux = list(precio.values())
        precio = listaAux[0]
        print(precio)
    else:
        return HttpResponse('error message')
    print(nombreProducto)
    transaccionNueva = Transacciones(idVendedor=idVendedor, precio=precio, nombreComida=nombreProducto)
    transaccionNueva.save()
    return JsonResponse({"transaccion": "realizada"})
