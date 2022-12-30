from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('product/', views.showproduct,name="product"),
    path('about/', views.showAboutInfo,name="about"),
    path('computer/', views.showComputer,name="computer"),
    path('contact/', views.showContactInfo,name="contact"),
    path('laptop/', views.showLaptop,name="laptop"),
    path('homepage/', views.showHomePage,name="homepage"),
    path('hello/', views.hello,name="hello"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logOutUser,name="logout"),
    path('register/', views.registerUser,name="register"),
    path('review/', views.reviewAdd,name="review"),
    path('checkout/', views.checkout,name="checkout"),
    path('productt/', views.gotoPro,name="gotoProduct"),
    # path('specific/', views.specificLaptop,name="specificLaptop"),
]
