from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('favicon.jpg', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.jpg'))),
]