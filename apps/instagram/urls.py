from django.urls import path

from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pagina_id>/results', views.results, name='results'),
    path('create', views.CreateView.as_view(), name='create'),
    # path('create_form', views.form_cadastrar_pagina(), name='form_cadastrar_pagina'),
    # path('<int:pagina_id>/edit', views.edit, name='edit')
]
