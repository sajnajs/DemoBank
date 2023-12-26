from . import views
from django.urls import path, include
app_name = 'banking_app'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('new_page/',views.new_page,name='new_page'),
    path('register_form/',views.register_form,name='register_form'),
    path('submit_form/',views.submit_form,name='submit_form'),
    path('logout/', views.logout, name='logout'),
]






