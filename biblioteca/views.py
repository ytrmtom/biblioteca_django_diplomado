from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import generics
from .models import Categoria, Autor, Libro, Usuario, Prestamo
from .serializers import CategoriaSerializer, AutorSerializer, LibroSerializer, UsuarioSerializer, PrestamoSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo")



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer







class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class AutorCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class LibroCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class UsuarioCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PrestamoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer


@api_view(['GET'])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)}, status=400)

@api_view(['GET'])
def autor_count(request):
    try:
        cantidad = Autor.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)}, status=400)

@api_view(['GET'])
def libro_count(request):
    try:
        cantidad = Libro.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)}, status=400)

@api_view(['GET'])
def usuario_count(request):
    try:
        cantidad = Usuario.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)}, status=400)

@api_view(['GET'])
def prestamo_count(request):
    try:
        cantidad = Prestamo.objects.count()
        return JsonResponse({
            'cantidad': cantidad
        },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)}, status=400)

