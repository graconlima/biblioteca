from rest_framework import serializers 
from .models import Autor, Livro 
class AutorSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Autor 
        fields = ['id', 'nome', 'nacionalidade'] 
class LivroSerializer(serializers.ModelSerializer): 
    autor = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all()
    )
    class Meta: 
        model = Livro 
        fields = ['id', 'titulo', 'ano_publicacao', 'autor'] 