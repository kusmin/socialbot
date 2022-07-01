from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib import messages
from apps.instagram.forms import PaginaForm
from apps.instagram.models import Pagina


@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'home/instagram.html'
    context_object_name = 'list_page'

    def get_queryset(self):
        return Pagina.objects.filter(user=self.request.user, ativo=True).order_by('-nome')


@method_decorator(login_required, name='dispatch')
class UpdateView(SuccessMessageMixin,UpdateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'home/instagram.html'
    success_message = 'Conta alterada com sucesso'

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Pagina, id=id)

    def put(self, *args, **kwargs):
        if self.form_class.is_valid():
            pagina = self.form_class.save(commit=False)
            pagina.save()
            return render(self.request , reverse_lazy('instagram:index'))
        else:
            return render(self.request, 'instagram.html', {})


@method_decorator(login_required, name='dispatch')
class UpdateViewDelete(DeleteView, SuccessMessageMixin):
    model = Pagina
    form_class = PaginaForm
    template_name = 'home/instagram.html'
    success_message = 'Conta deletada com sucesso'

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Pagina, id=id)

    def put(self, *args, **kwargs):
        if self.form_class.is_valid():
            pagina = self.form_class.save(commit=False)
            pagina.save()
            return render(self.request, reverse_lazy('instagram:index'))
        else:
            return render(self.request, 'instagram.html', {})


class DetailView(generic.DetailView):
    model = Pagina
    template_name = 'home/instagram.html'


@method_decorator(login_required, name='dispatch')
class CreateView(SuccessMessageMixin, generic.CreateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'home/instagram.html'
    success_message = 'Conta criada com sucesso'

    def post(self, request, *args, **kwargs):
        user = request.user
        form_class = PaginaForm(request.POST)
        if form_class.is_valid():
            pagina = form_class.save(commit=False)
            pagina.user = user
            pagina.save()
            messages.success(self.request, 'Conta criada com sucesso')
            return HttpResponseRedirect(reverse_lazy('instagram:index'))
        else:
            return HttpResponseRedirect(reverse_lazy('instagram:index'))


# @login_required(login_url="/login/")
# def get_instagram():
#
# def form_cadastrar_pagina(request):
#     form_class = PaginaForm()
#     return render(request, "form.html", {'form': form_class})

def results(request, pagina_id):
    return HttpResponse("Você estava vendo detalhes da pagina %s." % pagina_id)
