from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContatoForm

def index(request):
    return render(request, 'core/index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                form.sendEmail() # Corrigido para sendEmail
                messages.success(request, 'E-mail enviado com sucesso!')
                # Redireciona para a mesma página para evitar reenvio ao atualizar
                return redirect(reverse('contato')) 
            except Exception as e:
                # Captura exceções genéricas e exibe uma mensagem de erro
                messages.error(request, f'Erro ao enviar e-mail: {str(e)}')
                # Redireciona mesmo em caso de erro para mostrar a mensagem
                return redirect(reverse('contato'))
        else:
            # Se o formulário não for válido (ex: campos obrigatórios faltando),
            # renderiza a página novamente com os erros do formulário
            messages.error(request, 'Por favor, corrija os erros no formulário.')
            # Passa o formulário inválido para o template exibir os erros
            context = {'form': form}
            return render(request, 'core/contato.html', context)
    else:
        # Se for uma requisição GET (primeiro acesso à página),
        # cria um formulário vazio e o passa para o template
        form = ContatoForm()
        context = {'form': form}
        return render(request, 'core/contato.html', context)

# A linha abaixo foi removida pois a importação já existe no início do arquivo
# from django.core.mail import send_mail, EmailMessage