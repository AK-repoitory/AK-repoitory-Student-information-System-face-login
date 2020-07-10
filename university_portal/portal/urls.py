from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('test/', views.test, name="test"),
    path('signup', views.handlesignup, name="handlesignup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('marks', views.marks, name="marks"),
    path('face', views.face, name="face"),
    path('pdf/',views.GeneratePdf.as_view()),
    path('gallery',views.gallery,name = "gallery"),
    path('Courses',views.Courses,name = "Courses"),

]
