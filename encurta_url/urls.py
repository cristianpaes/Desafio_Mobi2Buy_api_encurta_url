from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from api.views import encurtadorViewset, urlRedirect

router = routers.DefaultRouter()
router.register(r'url', encurtadorViewset)

urlpatterns = [
    path('', RedirectView.as_view(url='api/')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('<str:url_encurtada>/', urlRedirect.as_view(), name='redirecionamento')
]
