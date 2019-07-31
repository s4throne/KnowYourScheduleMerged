from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    index_html_page = loader.get_template('../ui/AdminDash.html')
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
    return HttpResponse(index_html_page.render(context, request))


def admin(request):
    adminDash = loader.get_template('../UI/AdminDash.html')
    return HttpResponse(adminDash.render())


def adminEdit(request):
    adminEditor = loader.get_template('../UI/editschedule.html')
    return HttpResponse(adminEditor.render())


def adminAdd(request):
    adminAddView = loader.get_template('../UI/AddViewer.html')
    return HttpResponse(adminAddView.render())
