from django.urls import path

from . import views

app_name = 'tag'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.get_queryset_tag, name='tags'),
    path('create', views.CreateView.as_view(), name='create'),
    path('categoria', views.IndexViewCategoria.as_view(), name='index_categoria'),
    path('categoria/create', views.CreateViewCategoria.as_view(), name='create_categoria'),

]
