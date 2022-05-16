
from django.contrib import admin
from django.urls import path, include
from apps.api.models import MovieResource
from . import views

movie_resource = MovieResource()

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(movie_resource.urls)),
    path('', views.home)
]
