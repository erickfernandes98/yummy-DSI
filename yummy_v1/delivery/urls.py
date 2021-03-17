#para conseguir utilizar as urls do Django precisamos importar essas urls
from django.urls import path
#importar todas as views relacionadas às urls  
from . import views

urlpatterns = [
    path('', views.index, name='index'), # primeiro parâmetro é a rota, segundo é a view responsável por atender a requisição, terceiro é o namespace do aplicativo para essas entradas urls
    path('<int:sobremesa_id>', views.sobremesa, name='sobremesa'),
    path('buscar', views.buscar, name='buscar')
]