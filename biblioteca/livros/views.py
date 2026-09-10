from rest_framework import viewsets, permissions 
from .models import Autor, Livro 
from .serializers import AutorSerializer, LivroSerializer 
class AutorViewSet(viewsets.ModelViewSet): 
    queryset = Autor.objects.all() 
    serializer_class = AutorSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 


class LivroViewSet(viewsets.ModelViewSet):
	queryset = Livro.objects.all()
	serializer_class = LivroSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	#Exemplo 1 - parametro de URL
	#GET /api/livros/5/ <-- Capturado da rota (existe naturalmente no DRF)
	#Livros.objects.get(pk=5)

	#Exemplo 2 - parametros de consulta (sobrescrita de get_queryset())
	#GET /api/livros/?titulo=e-book_DSD&ano_publicacao=2022
	def get_queryset(self):
		queryset = Livro.objects.all()
		titulo = self.request.query_params.get('titulo')

		ano = self.request.query_params.get('ano_publicacao')

		if titulo:
			queryset = queryset.filter(titulo__icontains = titulo)

		if ano:
			queryset = queryset.filter(ano_publicacao = ano)

		return queryset

	#Exemplo 4 - parametros de corpo (sobrescrita de create)
	#POST /api/livros/ --> {"titulo":"Romeu e Julieta","ano_publicacao":1595,"autor":1}
	def create(self, request, *args, **kwargs):
		print(request.data)
		return super().create(request, *args, **kwargs)