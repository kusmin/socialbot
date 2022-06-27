from django.urls import path

from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/updated', views.UpdateView.as_view(), name='updated'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete', views.UpdateViewDelete.as_view(), name='delete'),
    # path('create_form', views.form_cadastrar_pagina(), name='form_cadastrar_pagina'),
    # path('<int:pagina_id>/edit', views.edit, name='edit')
]
