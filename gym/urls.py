from django.urls import path
from . import views

urlpatterns = [
    #path('',views.about, name = 'about'),    
    path('about/',views.about, name = 'about'),   
    path('contact/',views.contact, name = 'contact'),
    path('',views.index, name = 'home'),   
    path('admin_login',views.login, name = 'login'),
    path('logout',views.logout_admin, name = 'logout'),
]