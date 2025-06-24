from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('', views.loginView, name='login'),
    path('index/', views.display, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('a_positive', views.apositive, name="a_positive"),
    path('b_positive', views.bpositive, name="b_positive"),
    path('o_positive', views.opositive, name="o_positive"),
    path('a_negative', views.anegative, name="a_negative"),
    path('b_negative', views.bnegative, name="b_negative"),
    path('o_negative', views.onegative, name="o_negative"),
    path('ab_negative', views.abnegative, name="ab_negative"),
    path('ab_positive', views.abpositive, name="ab_positive"),
    # path('final_report',views.create_pdf, name="report")
    
]  