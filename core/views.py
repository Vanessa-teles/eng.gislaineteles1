from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContatoForm

# Dentro da sua view de contato:
if form.is_valid():
    nome = form.cleaned_data['nome']
    email = form.cleaned_data['email']
    mensagem = form.cleaned_data['mensagem']
    
    # Verifique se esta parte está sendo executada
    try:
        send_mail(
            f'Contato do site - {nome}',
            f'Mensagem de {nome} ({email}):\n\n{mensagem}',
            email,  # remetente
            ['gislaine.teles.eng@gmail.com'],  # destinatário
            fail_silently=False,
        )
        # Adicione um print aqui para debug
        print("Email enviado com sucesso!")
    except Exception as e:
        # Adicione um print do erro
        print(f"Erro ao enviar email: {e}")
