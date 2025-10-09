from rest_framework import serializers 
from drf_hal_json.serializers import HalModelSerializer 
from .models import Autor, Livro 
# Classe base HAL compatível com drf-spectacular 
class SafeHalModelSerializer(HalModelSerializer): 
    class Meta: 
        ref_name = None  # evita conflito de nome no schema 
        nested_fields = []  # evita o erro do drf_nested_fields 
class AutorSerializer(SafeHalModelSerializer): 
    class Meta: 
        model = Autor 
        fields = ['id', 'nome'] 
        ref_name = "AutorHAL" 
        nested_fields = []  # evita introspecção recursiva 
class LivroSerializer(SafeHalModelSerializer): 
    autor = AutorSerializer(read_only=True) 
    class Meta: 
        model = Livro 
        fields = ['id', 'titulo', 'autor'] 
        ref_name = "LivroHAL" 
        nested_fields = []  # evita introspecção recursiva