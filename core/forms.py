# core/forms.py
from django import forms
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _

class ContatoForm(forms.Form):
    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=True)
    cidade = forms.CharField(required=True)
    service = forms.ChoiceField(choices=[
        ('', 'Selecione o serviço'),
        ('entrega', 'Vistoria de Entrega de Chaves'),
        ('sindico', 'Vistoria para Síndicos'),
        ('laudo', 'Laudos Técnicos'),
        ('outro', 'Outro serviço'),
    ], required=True)
    assunto = forms.CharField(required=True)
    mensagem = forms.CharField(widget=forms.Textarea, required=True)

    def sendEmail(self):
        # Implemente o método de envio de email aqui
        subject = self.cleaned_data['assunto']
        message = f"""
        Nome: {self.cleaned_data['nome']}
        Email: {self.cleaned_data['email']}
        Telefone: {self.cleaned_data['telefone']}
        Cidade: {self.cleaned_data['cidade']}
        Serviço: {self.cleaned_data['service']}
        
        Mensagem:
        {self.cleaned_data['mensagem']}
        """
        send_mail(
            subject,
            message,
            'gislaine.teles.eng@gmail.com',  # Remetente
            ['gislaine_teles@outlook.com'],  # Destinatário
            fail_silently=False,
        )