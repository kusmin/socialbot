from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from instagram.models import Pagina


def index(request):
    list_page = Pagina.objects.all().order_by('-nome')
    context = {
        'list_page': list_page,
    }
    return render(request, 'instagram/index.html', context)

def detail(request, pagina_id):
    pagina = get_object_or_404(Pagina, pk=pagina_id)
    return render(request, 'instagram/detail.html', {'pagina': pagina})

def results(request, pagina_id):
    return HttpResponse("Você estava vendo detalhes da pagina %s." % pagina_id)

