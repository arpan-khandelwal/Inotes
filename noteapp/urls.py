from django.urls import path
from . import views
import django.contrib.auth.views as auth_views


app_name = 'noteapp'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',auth_views.LoginView.as_view(template_name = 'noteapp/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'noteapp/loggedout.html'),name = 'logout'),
    path('register/',views.register,name = 'register'),
    path('settings/',views.settings,name = 'settings'),
    path('update/<int:id>/',views.update,name = 'update'),
    #path('loggedout/',views.loggedout,name = 'loggedout'),
    path('home/',views.home_page,name = 'home_page'),
    path('delete/<int:id>/',views.delete,name = 'delete'),
    # path('addnote/',views.addnote,name = 'addnote'),
]