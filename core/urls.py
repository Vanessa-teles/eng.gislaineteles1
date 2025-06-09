from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
 path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('core/images/favicon.ico'))),
]