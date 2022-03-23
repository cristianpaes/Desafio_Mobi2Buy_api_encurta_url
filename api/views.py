from django.shortcuts import render, redirect
from datetime import date, timedelta
from random import sample
from string import ascii_letters
from django.views import View
from rest_framework import viewsets
from .models import urls
from .serializers import urlsSerializer


end_encurta = "http://localhost:8000/"
prazo = date.today() - timedelta(days=7)
data_expirado = date.today() + timedelta(days=7)


class encurtadorViewset(viewsets.ModelViewSet):
    queryset = urls.objects.filter(data_criacao__gte=prazo)
    expirado = urls.objects.filter(data_criacao__lte=prazo)
    for url in expirado:
        url.delete()
    serializer_class = urlsSerializer

    def perform_create(self, serializer):
        encurta = ascii_letters
        if not self.request.data['url_encurtada']:
            encurta_url = end_encurta+("".join(sample(encurta, 6)))
            if self.request.data['data_expiracao']:
                serializer.save(url_encurtada=encurta_url)
            else:
                serializer.save(url_encurtada=encurta_url, data_expiracao=data_expirado)
        else:
            encurta_url = end_encurta + self.request.data['url_encurtada']
            if self.request.data['data_expiracao']:
                serializer.save(url_encurtada=encurta_url)
            else:
                serializer.save(url_encurtada=encurta_url, data_expiracao=data_expirado)


class urlRedirect(View):
  def get(self, request, url_encurtada, *args, **kwargs):
     linkEncurtado = end_encurta + self.kwargs['url_encurtada']
     redirecionamento = urls.objects.filter(url_encurtada=linkEncurtado).first().url_normal
     return redirect(redirecionamento)