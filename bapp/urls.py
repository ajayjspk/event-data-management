from django.contrib import admin
from django.urls import path
from bapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.home, name="home"),
    path("events", views.page, name="events"),
    path("login", views.login, name="login"),
    path("loginuser", views.loginuser, name="login_user"),
    path("regisevent", views.eve_reg, name="addevent"),
    path("addevent", views.eve_regis, name="addevent1"),
    path("addevent", views.eve_regis, name="addevent1"),
    path("regisorganizer", views.regisorganizer, name="orgregis"),
    path("loginorganizer", views.loginorganizer, name="orglogin"),
    path("delete/<int:pk>", views.delete_eve, name="delete"),
    path("deleteevents", views.deleteevents, name="deleteevents"),
    path("stu_regis", views.stu_regis, name="stu_regis"),
    path("remove/<int:id>", views.remove_student, name="remove"),
]
