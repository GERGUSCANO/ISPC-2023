#PRIMERA SOLUCION

from django.shortcuts import render, redirect
from .models import Articulo, Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required

@login_required
def agregar_al_carrito(request, articulo_id):
    articulo = Articulo.objects.get(idarticulo=articulo_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, articulo=articulo)
    if not creado:
        item_carrito.cantidad += 1
        item_carrito.save()

    return redirect('carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item_carrito = ItemCarrito.objects.get(id=item_id)
    item_carrito.delete()
    return redirect('carrito')

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)

    total = 0
    for item in items_carrito:
        total += item.articulo.precio * item.cantidad

    contexto = {
        'items_carrito': items_carrito,
        'total': total
    }
    return render(request, 'carrito.html', contexto)

#SEGUNDA SOLUCION

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Carrito, ItemCarrito
from .forms import AgregarAlCarritoForm

@login_required
def agregar_al_carrito(request, id_articulo):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    articulo = Articulo.objects.get(idarticulo=id_articulo)

    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, articulo=articulo)
            item.cantidad += cantidad
            item.save()
            return redirect('carrito')
    else:
        form = AgregarAlCarritoForm()

    context = {
        'form': form,
        'articulo': articulo
    }

    return render(request, 'agregar_al_carrito.html', context)

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)

    context = {
        'carrito': carrito,
        'items': items
    }

    return render(request, 'ver_carrito.html', context)

@login_required
def eliminar_item_carrito(request, id_item):
    item = ItemCarrito.objects.get(id=id_item)
    item.delete()
    return redirect('carrito')

@login_required
def vaciar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    items.delete()
    return redirect('carrito')

#TERCERA SOLUCION

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Articulo, Carrito, ItemCarrito

class ListaArticulos(ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    context_object_name = 'articulos'

class DetalleArticulo(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    context_object_name = 'articulo'

class DetalleCarrito(LoginRequiredMixin, DetailView):
    model = Carrito
    template_name = 'detalle_carrito.html'
    context_object_name = 'carrito'

    def get_object(self, queryset=None):
        return self.request.user.carrito

class AgregarItemCarrito(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        articulo_id = request.POST.get('articulo_id')
        articulo = Articulo.objects.get(idarticulo=articulo_id)
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

        item_carrito, creado = ItemCarrito.objects.get_or_create(carrito=carrito, articulo=articulo)
        if not creado:
            item_carrito.cantidad += 1
            item_carrito.save()

        return redirect('carrito')

class EliminarItemCarrito(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        item_carrito = ItemCarrito.objects.get(id=item_id)
        item_carrito.delete()
        return redirect('carrito')
