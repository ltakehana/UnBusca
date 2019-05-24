# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext, loader
from django.http.response import HttpResponse
from django.shortcuts import render,render_to_response
from core.models import *
import md5
from django.utils import timezone

# Create your views here.

def home(request):
	try:
		template=loader.get_template('main.html')	
		context = {
			'title': 'UnBusca',
			'USER' : USER.objects.get(USER_ID=request.session['USER_ID']),
			'POSTS' : POST.objects.all().order_by('-POST_TIME'),
		}
	except Exception:
		template=loader.get_template('index.html')
		context = {
			'title': 'UnBusca',
		}
	return HttpResponse(template.render(context))

def cadastro(request):
	template=loader.get_template('cadastro.html')
	context = {
        'title': 'UnBusca',
    }
	return HttpResponse(template.render(context))

def cadastrar(request):
	user=[]
	message=''
	try:
		user=USER(
			USER_NAME=request.POST.get('Username'),
			USER_PASSWORD=md5.new(str(request.POST.get('Password'))).hexdigest(),
			USER_FULLNAME=request.POST.get('Name'),
			USER_EMAIL=request.POST.get('Email'),
			USER_TELEPHONE=request.POST.get('Telephone'),
			USER_BIRTHDAY=request.POST.get('Birthday'),
			USER_MATRICULA=request.POST.get('Matricula'),
		)
		user.save()
		message="Usuário cadastrado com sucesso!"
	except Exception:
		message="Erro ao cadastrar usuario!"
	template=loader.get_template('cadastrar.html')
	context = {
        'title': 'UnBusca',
        'message': message,
    }
	return HttpResponse(template.render(context))
	
def login(request):
    m = USER.objects.get(USER_NAME=request.POST.get('Username'))
    if m.USER_PASSWORD == md5.new(str(request.POST.get('Password'))).hexdigest():
        request.session['USER_ID'] = m.USER_ID
        message=u"Você está autenticado."
    else:
        message=u"Seu nome de usuário e senha não conferem."
    template=loader.get_template('login.html')
    context = {
        'title': 'UnBusca',
        'message': message,
    }
    return HttpResponse(template.render(context))
    
def post(request):
	post=[]
	try:
		user=USER.objects.get(USER_ID=request.session['USER_ID'])
		post=POST(
			POST_USER = user,
			POST_TITLE = request.POST.get('POST_TITLE'),
			POST_TEXT = request.POST.get('POST_TEXT'),
			POST_LOCAL = request.POST.get('POST_LOCAL'),
		)
		try:
			post.save()
		except Exception:
			post="erro"
	except Exception:
		pass
	template=loader.get_template('post.html')
	context = {
        'title': 'UnBusca',
        'message': post,
    }
	return HttpResponse(template.render(context))

def logout(request):
	del request.session['USER_ID']
	template=loader.get_template('logout.html')
	context = {
        'title': 'UnBusca',
    }
	return HttpResponse(template.render(context))
