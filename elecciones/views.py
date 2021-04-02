from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Candidato, Region

def index(request):
    latest_question_list = Region.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detalle(request,region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'detalle.html', {'region' : region})

def votar(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    try:
        selected_candidato = region.candidato_set.get(pk=request.POST['candidato'])
    except (KeyError, Candidato.DoesNotExist):
        return render(request, 'detalle.html', {
            'region': region,
            'error_message': "No has seleccionado un candidato.",
        })
    else:
        selected_candidato.votos += 1
        selected_candidato.save()
        return HttpResponseRedirect(reverse('elecciones:resultados', args=(region_id,)))

def resultados(request, region_id):
    region = get_object_or_404(Region, pk=region_id)
    return render(request, 'resultados.html', {'region' : region})
