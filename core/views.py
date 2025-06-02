from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def index(request):
    return render(request, 'core/index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                form.sendEmail()
                messages.success(request, 'E-mail enviado com sucesso!')
                return redirect('contato')
            except Exception as e:
                messages.error(request, f'Erro ao enviar e-mail: {e}')
                return redirect('contato')
    else:
        form = ContatoForm()
    
    context = {
        'form': form
    }
    return render(request, 'core/contato.html', context)
