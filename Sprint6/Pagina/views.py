from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentarioForm
from .models import Publicacion, Comentario


def landing(request):
    print(Publicacion._meta.db_table)
    contexto ={
        'publicacionesLlave' : Publicacion.objects.raw('SELECT * FROM Pagina_publicacion ORDER BY id DESC'),
        'titulo': 'Pagina-Landing'
    }
    return render(request,'Pagina/landing.html', contexto)


def crear_comentario(request, publicacion_id):
    publicacion = Publicacion.objects.get(pk=publicacion_id)
    if request.method == "POST":
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.usuario = request.user
            comentario.publicacion = publicacion
            comentario.save()
    else:
        formulario = ComentarioForm()
    return render(request, 'Pagina/crear_comentario.html', {'formulario': formulario})
