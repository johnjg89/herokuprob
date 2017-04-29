# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django.utils.encoding import python_2_unicode_compatible



usuarios = User.username


@python_2_unicode_compatible
class disenos(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    descripcion = models.TextField()
    presupuesto = models.IntegerField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)
   

    def __str__(self):
        return self.titulo

@python_2_unicode_compatible
class disenador(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    descripcion = models.TextField()
    presupuesto = models.IntegerField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    #usuario = models.ForeignKey(User.username, default = 'a')
    
    

    def __str__(self):
        return self.titulo        


@python_2_unicode_compatible
class Comentario(models.Model):
    nombre =models.CharField(max_length=100, verbose_name='Tu Nombre')
    Correo = models.CharField(max_length=100, verbose_name='Tu Correo')
    fecha_registro = models.DateTimeField(auto_now=True)
    proyecto = models.ForeignKey(disenos)
    texto = models.CharField(max_length=100, verbose_name='Comentario')
    costo = models.IntegerField()
    imagen = models.ImageField(upload_to='images', verbose_name=u'Imágen')
    estado = models.CharField(max_length=100, default = 'En proceso' )
    def __str__(self):
        return self.texto
