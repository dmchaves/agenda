from django.shortcuts import render
from core.models import Evento

# Create your views here.

# def index(request):
#    return redirect('/agenda/')
#tem que adicionar  "index" ao lado de render em from - import

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)