from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path ("contact",views.contact,name='contact'),
    path('lipsticks/', views.lipsticks, name='lipsticks'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('brands/', views.brands, name='brands'),
     path('thank-you/', views.thank_you, name='thank_you'),
]
