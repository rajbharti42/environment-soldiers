from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index , name="home"),
    path("contact", views.contact, name="contact"),
    path("ourmotive", views.ourmotive , name="ourmotive"),
    path("blogs", views.blogs, name="blog"), 
    path("blogpost/<str:slug>", views.blogpost, name="blogpost")
]
# /<str:slug>