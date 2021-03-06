from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from apps.instagram.forms import PaginaForm
from apps.instagram.models import Pagina


class IndexView(generic.ListView):
    template_name = 'instagram/templates/instagram/index.html'
    context_object_name = 'list_page'

    def get_queryset(self):
        return Pagina.objects.all().order_by('-nome')


class DetailView(generic.DetailView):
    model = Pagina
    template_name = 'instagram/templates/instagram/detail.html'


class CreateView(generic.CreateView):
    model = Pagina
    template_name = 'instagram/templates/instagram/create.html'
    form_class = PaginaForm

    def post(self, request, *args, **kwargs):
        form_class = PaginaForm(request.POST)
        if form_class.is_valid():
            pagina = form_class.save()
            pagina.save()
            return HttpResponseRedirect(reverse_lazy('instagram:detail', args=[pagina.id]))


def results(request, pagina_id):
    return HttpResponse("Você estava vendo detalhes da pagina %s." % pagina_id)
