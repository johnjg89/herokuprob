# coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comentario, disenos
from .forms import ComentarioForm, ContactoForm, RecetaForm
from django.views.decorators.csrf import csrf_protect



def inicio(request):
    home = disenos.objects.all()
    context = {'home': home}
    return render(request, 'index.html', context)

def quienes(request):
    home = disenos.objects.all()
    context = {'home': home}
    return render(request, 'quienes.html', context)


#@csrf_protect
def nuevodis(request):
	if request.method=='POST' :
		formulario = ComentarioForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
       			return HttpResponseRedirect('/lista')
	else:
		
		formulario = ComentarioForm()
	context = {'formulario': formulario}
	return render(request, 'nuevodis.html', context)

  


def lista(request):

		proyectos = disenos.objects.all()
		context = {'datos': proyectos}
		return render(request, 'lista.html', context)



def ingresar(request):


	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
    
	if request.method == 'POST':
			formulario = AuthenticationForm(request.POST)
			if formulario.is_valid:
				usuario = request.POST['username']
				clave = request.POST['password']
				acceso = authenticate(username=usuario, password=clave)
	        	if acceso is not None:
	        		if acceso.is_active:
	        			login(request, acceso)
	        			return HttpResponseRedirect('/privado')
	        		else:
	        			return render(request, 'noactivo.html')
	        	else:
	        			return render(request, 'nousuario.html')
	else:
			formulario = AuthenticationForm()	
	context = {'formulario': formulario}
	return render(request, 'ingresar.html', context)


def proyecto(request, id_diseno):
    dato = get_object_or_404(disenos, pk=id_diseno)
    comentarios = Comentario.objects.filter(proyecto=dato).order_by('-id')
    diseno=disenos.objects.all()
    context = {'receta': dato, 'comentarios': comentarios}
    return render(request, 'detalles.html', context)







def privado(request):
    usuario = request.user
    usuarios = User.objects.all()
    proyectos = disenos.objects.all()
    context = {'usuario': usuario,'usuarios': usuarios,'proyectos': proyectos}
    return render(request, 'privado.html', context)


def principal(request, id):
	dato = get_object_or_404(User, pk=id)
	empresa = User.objects.filter(username=dato)
	context = {'cliente': dato, 'empresa': empresa}
	return render(request, 'principal.html', context)







def nuevousuario(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')

	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/ingresar')
	else:
		formulario = UserCreationForm()
	context = {'formulario': formulario}
	return render(request, 'nuevousuario.html', context)

def cerrar(request):
    if not request.user.is_anonymous():
        logout(request)
        return HttpResponseRedirect('/')
    else :
        return HttpResponseRedirect('/')


def clientes(request):
    usuarios = User.objects.all()
    proyectos = disenos.objects.all()
    context = {'proyectos': proyectos, 'usuarios':usuarios}
    return render(request, 'clientes.html', context)



def proyecto_nuevo(request):
	if request.method=='POST':
		formulario = RecetaForm(request.POST)
		if formulario.is_valid():
			post = formulario.save(commit=False)
                        post.usuario = request.user
                        post.save()
			return HttpResponseRedirect('/')
	else:
    	
		formulario = RecetaForm()
		
	usuario = request.user
	context = {'formulario': formulario, 'usuario': usuario}
	return render(request, 'proyectoform.html', context)


def usuario(request, id_cliente):
    dato = get_object_or_404(User, pk=id_cliente)
    empresa = User.objects.filter(username=dato)
    context = {'cliente': dato, 'empresa': empresa}
    return render(request, 'privado.html', context)

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)




#@login_required(login_url='/ingresar')
