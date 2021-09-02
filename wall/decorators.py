from django.shortcuts import redirect
from django.contrib import messages

def login_req(func):
    
    def wrapper(request,*args,**kwargs):
        
        if 'user' not in request.session:
            messages.error(request,"Please log-in")
            return redirect('/login')
        resp=func(request,*args,**kwargs)
        return resp
    return (wrapper)