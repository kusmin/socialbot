from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib import messages
from requests import Response

from apps.tag.forms import TagForm, CategoriaForm
from apps.tag.models import Tag, Categoria
from django.template import loader
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class CreateView(SuccessMessageMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'home/tag.html'
    success_message = 'Tag criada com sucesso'

    def post(self, request, *args, **kwargs):
        form_class = TagForm(request.POST)
        if form_class.is_valid():
            tag = form_class.save()
            tag.save()
            messages.success(self.request, 'Tag criada com sucesso')
            return HttpResponseRedirect(reverse_lazy('tag:index'))
        else:
            return HttpResponseRedirect(reverse_lazy('tag:index'))


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'home/tag.html'
    context_object_name = 'list_page'

    def get_queryset(self):
        return Tag.objects.all().order_by('-nome')


@method_decorator(login_required, name='dispatch')
class IndexViewCategoria(generic.ListView):
    template_name = 'home/categoria.html'
    context_object_name = 'list_page'

    def get_queryset(self):
        return Categoria.objects.all().order_by('-nome')


@method_decorator(login_required, name='dispatch')
class CreateViewCategoria(CreateView, SuccessMessageMixin):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'home/categoria.html'
    success_message = 'Categoria criada com sucesso'

    def post(self, request, *args, **kwargs):
        form_class = CategoriaForm(request.POST)
        if form_class.is_valid():
            tag = form_class.save()
            tag.save()
            messages.success(self.request, 'Categoria criada com sucesso')
            return HttpResponseRedirect(reverse_lazy('tag:index_categoria'))
        else:
            return HttpResponseRedirect(reverse_lazy('tag:index_categoria'))


@login_required(login_url="/login/")
# @method_decorator(login_required, name='dispatch')
def get_queryset_tag(request):
    tag = Tag.objects.all().order_by('nome').values()

    return JsonResponse(list(tag), status=200, content_type="application/json", safe=False)
