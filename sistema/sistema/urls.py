"""map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from .settings import local
from django.views.generic import TemplateView
from users import urls as users_urls
from producao import views as producao_views
from django.conf.urls import handler500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(users_urls)),
    url(r'^producao/', include('producao.urls', namespace='producao')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/', include("producao.api.urls", namespace='api')),
    # url(r'^plan-api/', include("planeamento.api.urls", namespace='plan-api')),
]

if local.DEBUG:
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)

handler500 = producao_views.error_500
