#This Python file uses the following encoding: utf-8
from django.forms import ModelForm
from django import forms
from .models import disenos, Comentario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tú correo electrónico')
    mensaje = forms.CharField(widget=forms.Textarea)


class RecetaForm(ModelForm):
    class Meta:
        model = disenos
        usuari = User.username
        fields = ('titulo','descripcion','presupuesto')


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre','Correo','proyecto','proyecto','texto','costo','imagen')
