# https://docs.djangoproject.com/en/3.2/topics/http/urls/
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from core.views import view404, view500
from core.views import viewAbout, viewSignin, viewSignup, viewLogout

urlpatterns = [
    path( '',       viewAbout,  name = 'actionAbout'),
    path('signin',  viewSignin, name = 'actionSignin'),
    path('signup',  viewSignup, name = 'actionSignup'),
    path('logout',  viewLogout, name = 'actionLogout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = view404
handler500 = view500
