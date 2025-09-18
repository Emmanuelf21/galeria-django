from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.urls import reverse
from .models import Pais
from .form import ContatoForm
# Create your views here.
def home(request):
    paises = Pais.objects.all()
    return render(request, "galeria/home.html", {'paises':paises})

def pais_detail(request, id):
    pais = get_object_or_404(Pais, pk=id)
    
    context = {
        'pais': pais,
    }
    return render(request, 'galeria/pais.html', context)

def pesquisar_pais(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Pais.objects.filter(title__icontains=query)
    
    context = {
        'query': query,
        'resultados': resultados,
    }
    
    return render(request, 'galeria/pesquisa.html', context)

def sobre_nos(request):
    return render(request, 'galeria/sobre_nos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}',
                email,
                ['seu_email_para_receber@exemplo.com'],
                fail_silently=False
            )
            #redireciona para a página de sucesso
            return redirect(reverse('sucesso'))
    else:
        form = ContatoForm()
    return render(request, 'galeria/contato.html', {'form': form})

def sucesso(request):
    return render(request, 'galeria/sucesso.html')