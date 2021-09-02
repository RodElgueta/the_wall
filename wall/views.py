
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.db import IntegrityError
import bcrypt
from .decorators import login_req
import pdb


def index(request):
    context = {
        'saludo': 'Hola'
    }
    return redirect('/signup')


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')

    else:

        name = request.POST['name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pass_conf = request.POST['pass_conf']
        

        if password != pass_conf:
            messages.error(request, 'Passwords dont coincide')
            return redirect('/signup')
        
        errors = Users.objects.user_valid(request.POST)
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        if len(errors) > 0:
            for key, error_msg in errors.items():
                messages.error(request, error_msg)
            return redirect('/signup')
        try:
            new_user = Users.objects.create(
            name=name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=pw_hash)

        except IntegrityError:
            messages.error(request,"This Username/Email is already in use")
            return redirect('/signup')

        request.session['user'] = {'id':new_user.id,'name':name}

        messages.success(request,f'Welcome {name} to The Wall')
        return redirect('/wall')


def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    
    else:
        username = request.POST['name']
        password = request.POST['password']

        user = Users.objects.filter(name = username)
        if not user:
            messages.error('usuario no existe')
            return redirect('/login')
        
        
        logged_user = user[0]
        
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['user'] = {'id':logged_user.id,'name':username}
            
            messages.success(request,f'Welcome {username} to The Wall')
            return redirect('/wall')
        else:
            messages.error(request,"Invalid Username/Password")
            return redirect('/login')

def logout(request):
    del request.session['user']
    return redirect('/login')

def wall(request):
    if request.method == 'GET':
        context = {'messages': Messages.objects.all(),
                    'comments': Comments.objects.all()}
        return render(request,'wall.html',context)
    else:
            message = request.POST['message']
            Messages.objects.create(message=message,user=Users.objects.get(id=int(request.session['user']['id'])))
            return redirect('/wall')

def edit(request,int):
    message = Messages.objects.get(id=int)
    context = {'message':message}

    return redirect('/wall')

def comment(request,msgid):
    comment = request.POST['comment']

    comm=Comments.objects.create(comment=comment,user_id=int(request.session['user']['id']),message_id = int(msgid))
    
    return redirect ('/wall')

def delete(request,msgid):
    msgdel = Messages.objects.get(id=int(msgid))
    msgdel.delete()
    return redirect ('/wall')

    


