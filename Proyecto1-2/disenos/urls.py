from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^quienes/$', views.quienes, name='quienes'),
    url(r'^nuevousuario/$', views.nuevousuario, name='nuevousuario'),
    url(r'^privado', views.privado, name='privado'),
    url(r'^nuevodis/$', views.nuevodis, name='nuevodis'),
    url(r'^lista/', views.lista, name='lista'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^clientes/$', views.clientes, name='clientes'),
    url(r'^proyecto/nuevo/$', views.proyecto_nuevo, name='proyecto_nuevo'),
    url(r'^principal/(?P<id>\d+)$', views.principal, name='detalle_usuario'),
    url(r'^proyecto/(?P<id_diseno>\d+)$', views.proyecto, name='detalle_proyecto'),
    url(r'^sobre/$', views.sobre, name='sobre'),

]