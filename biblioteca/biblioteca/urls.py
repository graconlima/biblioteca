from django.contrib import admin 
from django.urls import path, include 
from rest_framework import routers 
from livros.views import AutorViewSet, LivroViewSet 
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 
 
router = routers.DefaultRouter() 
router.register(r'autores', AutorViewSet) 
router.register(r'livros', LivroViewSet) 
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), 
name='swagger-ui'), 
]