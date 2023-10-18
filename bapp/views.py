from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Events, Register, eve_register, feedback, RegisterOrganizer
from django.conf import settings


def home(request):
    return render(request, "html.html")


def page(request):
    post = Events.objects.all()
    dir = str(settings.BASE_DIR)
    return render(request, "eventspage.html", {"post": post, "root_dir": dir})


def login(request):
    # post1=Events.objects.all()
    if request.method == "POST":
        user_id = request.POST["user_id"]

        email = request.POST["email"]
        password = request.POST["password"]

        k = Register(userid=user_id, email=email, password=password)
        k.save()
    return render(request, "login.html")


def loginuser(request):
    global uid
    if request.method == "POST":
        obj = Register.objects.filter(
            userid=request.POST["user_id"], password=request.POST["password"]
        )
        if obj:
            uid = request.POST["user_id"]
            post = Events.objects.all()
            dir = str(settings.BASE_DIR)
            print("login sucessfull")
            return render(request, "eventspage.html", {"post": post, "root_dir": dir})
        return render(request, "login.html")


uid = ""


def eve_reg(request):
    if request.method == "POST":
        user_id = uid
        eve_name = request.POST["event_name"]
        print(user_id, eve_name)
        k = eve_register(userid=user_id, event=eve_name)
        k.save()
        post = Events.objects.all()
        dir = str(settings.BASE_DIR)
        print("login sucessfull")
        return render(request, "eventspage.html", {"events": post, "root_dir": dir})


def feedback(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        text = request.POST["msg"]
        k = feedback(fname=fname, lname=lname, text=message, email=email)
        k.save()


def regisorganizer(request):
    # post1=Events.objects.all()
    if request.method == "POST":
        user_id = request.POST["user_id"]
        email = request.POST["email"]
        password = request.POST["password"]
        k = RegisterOrganizer(userid=user_id, email=email, password=password)
        k.save()
    return render(request, "orglogin.html")


def loginorganizer(request):
    if request.method == "POST":
        obj = RegisterOrganizer.objects.filter(
            userid=request.POST["user_id"], password=request.POST["password"]
        )
        if obj:
            uid = request.POST["user_id"]
            # post = Events.objects.all()
            # dir = str(settings.BASE_DIR)
            return render(request, "addevents.html")
    return render(request, "orglogin.html")


def eve_regis(request):
    # post1=Events.objects.all()
    if request.method == "POST":
        event_location = request.POST["event_location"]
        event_name = request.POST["event_name"]
        event_date = request.POST["event_date"]
        event_description = request.POST["event_name"]
        print(request.FILES)
        event_image = request.FILES["event_image"]
        k = Events(
            event_name=event_name,
            event_date=event_date,
            event_description=event_description,
            event_location=event_location,
            event_image=event_image,
        )
        k.save()
        post = Events.objects.all()
        dir = str(settings.MEDIA_ROOT)
    # message("")
    return redirect("/deleteevents")
    # post = Events.objects.all()
    # dir = str(settings.BASE_DIR)
    # return render(request, "deleteevents.html", {'post': post, 'root_dir': dir})
    # return redirect('/events')
    # return render(request, "eventspage.html", {'post': post, 'root_dir': dir})


def delete_eve(request, pk):
    form = Events.objects.get(id=pk)
    form.delete()
    post = Events.objects.all()
    dir = str(settings.BASE_DIR)
    return render(request, "deleteevents.html", {"post": post, "root_dir": dir})
    # return render(request, "eventspage.html, {'post':form, 'root_dir': dir}")


def deleteevents(request):
    post = Events.objects.all()
    dir = str(settings.BASE_DIR)
    return render(request, "deleteevents.html", {"post": post, "root_dir": dir})


def stu_regis(request):
    stu_regis = eve_register.objects.all()
    dir = str(settings.BASE_DIR)
    return render(request, "stu_regis.html", {"events": stu_regis, "root_dir": dir})


def remove_student(request, id):
    record = eve_register.objects.get(id=id)
    record.delete()
    records = eve_register.objects.all()
    dir = str(settings.BASE_DIR)
    return redirect("/stu_regis")
    return render(request, "stu_regis.html", {"post": records, "root_dir": dir})
