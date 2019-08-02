import datetime

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from repo.schedule_repo import ScheduleRepo


def index(request):
    index_html_page = loader.get_template('../ui/viewerdashboard.html')
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]
        context["username"] = request.session["login_user"].split("@")[0]
        scheduleRepo = ScheduleRepo()
        context["row"] = scheduleRepo.fetchSchedule(scheduleRepo.getId(context["login_user"]),(datetime.datetime.today().weekday()+2)%7)
    else:
        return redirect("/")
    return HttpResponse(index_html_page.render(context, request))
