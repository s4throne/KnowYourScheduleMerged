import traceback

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from model.teacher import Teacher
from repo.user_repo import UserRepo
from service.account_service import AccountService
from utils import generate_uuid, timestamp


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

def adminAddSubmit(request):
    adminAddView = loader.get_template('../UI/AddViewer.html')
    context = {}
    if request.method == 'GET':
        fname = request.GET["txtName"]

        fullname = fname.split(" ")
        if len(fullname)!=2:
            context["error_msg"] = "Full Name Required"
            return HttpResponse(adminAddView.render(context, request))
        email = request.GET["txtEmail"]
        user = Teacher()
        user.first_name = fullname[0]
        user.last_name = fullname[1]
        user.email = email
        confirmation = generate_uuid()
        time = timestamp()
        context["user"] = user
        if not fname:
            context["error_msg"] = "Name field required"
        elif not email:
            context["error_msg"] = "Email field required"
        else:
            try:
                use_repo = UserRepo()
                if use_repo.save(user, confirmation, time):
                    context["success_msg"] = "Teacher Added, Confirmation Code is "+confirmation
            except Exception:
                traceback.print_exc()
                context["error_msg"] = "Something went wrong"
    return HttpResponse(adminAddView.render(context, request))
