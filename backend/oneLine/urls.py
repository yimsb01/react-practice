from django.urls import path
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]
