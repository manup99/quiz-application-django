from django.urls import path
from . import views
app_name='quiz1'

urlpatterns=[
    path('',views.Login.as_view(),name='login'),
    path('register',views.Register.as_view(),name='register'),
    path('index',views.index.as_view(),name='index'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('quiz_form',views.Quizcreate.as_view(),name='quiz_form'),
    path('quizcreate',views.Quizcontent.as_view(),name='quizcontent'),
    path('play/<int:yo>/',views.Play.as_view(),name='play'),
    path('quizscore/<int:yo>',views.Quizrank.as_view(),name='quizscore'),
]