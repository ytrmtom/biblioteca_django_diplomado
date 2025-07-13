from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'autor', views.AutorViewSet)
router.register(r'libro', views.LibroViewSet)
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'prestamo', views.PrestamoViewSet)

urlpatterns = [
   # path('', views.index, name='index'),
   path('categorias_create/', views.CategoriaCreateView.as_view(), name='categoria-create'),
   path('autor_create/', views.AutorCreateView.as_view(), name='autor-create'),
   path('libro_create/', views.LibroCreateView.as_view(), name='libro-create'),
   path('usuario_create/', views.UsuarioCreateView.as_view(), name='usuario-create'),
   path('prestamo_create/', views.PrestamoCreateView.as_view(), name='prestamo-create'),

   path('categorias_create/cantidad/', views.categoria_count, name='categoria-count'),
   path('', include(router.urls)),  
]



