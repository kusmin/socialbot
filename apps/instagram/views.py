from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from apps.instagram.forms import PaginaForm
from apps.instagram.models import Pagina
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'home/instagram.html'
    context_object_name = 'list_page'

    def get_queryset(self):
        return Pagina.objects.all().order_by('-nome')


class DetailView(generic.DetailView):
    model = Pagina
    template_name = 'home/instagram.html'


@method_decorator(login_required, name='dispatch')
class CreateView(generic.CreateView):
    model = Pagina
    form_class = PaginaForm

    def post(self, request, *args, **kwargs):
        user = request.user
        form_class = PaginaForm(request.POST)
        if form_class.is_valid():
            pagina = form_class.save(commit=False)
            pagina.user = user
            pagina.save()
            return HttpResponseRedirect(reverse_lazy('instagram:detail', args=[pagina.id]))
        else:
            return render(request, 'instagram.html', {})


# @login_required(login_url="/login/")
# def get_instagram():
#
# def form_cadastrar_pagina(request):
#     form_class = PaginaForm()
#     return render(request, "form.html", {'form': form_class})

def results(request, pagina_id):
    return HttpResponse("Você estava vendo detalhes da pagina %s." % pagina_id)
