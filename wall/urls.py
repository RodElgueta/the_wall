from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('signup',views.signup),
    path('logout',views.logout),
    path('wall',views.wall),
    path('comment/<msgid>',views.comment),
    path('delete/<msgid>',views.delete)
]
