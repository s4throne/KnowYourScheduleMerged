from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from service.account_service import AccountService
from service.forum_service import ForumService
from utils import password_hash


def index(request):
    index_html_page = loader.get_template('../ui/index.html')
    context = {"title": "Welcome to NCCS forum site!"}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    return HttpResponse(index_html_page.render(context, request))

def newuser(request):
    index_html_page = loader.get_template('../ui/newuser.html')
    return HttpResponse(index_html_page.render())

def signin(request):
    signup_html_page = loader.get_template('../ui/index.html')
    context = {}
    if request.method == 'POST':
        email = request.POST["txtEmail"]
        password = request.POST["txtPassword"]
        if not email:
            context["error_msg"] = "Invalid email or password."
        else:
            # ph = password_hash(password)
            account_service = AccountService()
            user = account_service.signin(email, password)
            if user is None:
                context["error_msg"] = "Invalid email or password."
            else:
                request.session["login_user"] = user
                context["success_msg"] = "Login successful."
                return redirect("/account/admindash/index/")
    return HttpResponse(signup_html_page.render(context, request))

def about(request):
    return HttpResponse("This is about page.")


