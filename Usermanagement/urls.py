from django.contrib import admin
from django.urls import path
from useractivities import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.users, name='users'),
]
