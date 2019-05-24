
from django.conf.urls import url, include
from core import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^cadastro/$', views.cadastro),
    url(r'^cadastrar/$', views.cadastrar),
    url(r'^login/$', views.login),
    url(r'^post/$', views.post),
    url(r'^logout/$', views.logout),
]
