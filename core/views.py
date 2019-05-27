# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext, loader
from django.http.response import HttpResponse
from django.shortcuts import render,render_to_response
from django.core.files.storage import FileSystemStorage
from core.models import *
from django.db.models import Q
import os
import md5
from django.utils import timezone

# Create your views here.

def home(request):
	try:
		template=loader.get_template('main.html')	
		tags=[]
		maxPost=20
		TagList=[]
		try:
			TagsFilters=request.GET.get("TagsFilters")
			TagsFilters=str(TagsFilters).replace(" ","[,]").split("[,]")
			TagList=TagsFilters
			tags=""
			i=0
			for tag in TagsFilters:
				if(i==0):
					tags=Q(POST_TAGS__contains=tag)
				else:
					tags=tags|Q(POST_TAGS__contains=tag)
				i+=1
			if(u'None' in TagsFilters):
				TagList=[]
				tags=""
		except Exception:
			tags=""
		if(tags!=""):
			posts=POST.objects.filter(tags).order_by('-POST_TIME')[:maxPost]
		else:
			posts=POST.objects.all().order_by('-POST_TIME')[:maxPost]
		context = {
			'title': 'UnBusca',
			'USER' : USER.objects.get(USER_ID=request.session['USER_ID']),
			'POSTS' : posts,
			'TAGS' : TagList,
			'TAGSNAMES' : tags
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
	try:
		m = USER.objects.get(USER_NAME=request.POST.get('Username'))
		if m.USER_PASSWORD == md5.new(str(request.POST.get('Password'))).hexdigest():
			request.session['USER_ID'] = m.USER_ID
			message=""
		else:
			message="Seu nome de usuário e senha não conferem"
	except Exception:
		message="Usuário não existe"
	template=loader.get_template('login.html')
	context = {
		'title': 'UnBusca'
		,'message': message,
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
			tags=str(post.POST_TITLE)+" "+str(post.POST_TEXT)+" "+str(post.POST_LOCAL)+" "+str(post.POST_USER.USER_NAME)+" @"+str(post.POST_USER.USER_NAME)
			tags=tags.lower()
			tags=tags.replace(" ","[,]")
			post.POST_TAGS=tags
		except Exception:
			pass
		try:
			post.save()
		except Exception:
			post="erro"
	except Exception:
		pass
	try:
		image=request.FILES['POST_IMAGES']
		fileStorage=FileSystemStorage()
		fileName=fileStorage.save("webfiles/images/posts/"+str(post.POST_ID)+"."+str(image.name).split(".")[-1],image)
		uploadFile=fileStorage.url(fileName)
		post.POST_IMAGE=str(post.POST_ID)+"."+str(image.name).split(".")[-1]
		post.save()
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
