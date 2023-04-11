from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path("add/", views.addEmployee,name='addEmployee'),
    path("read/", views.readEmployee,name='viewEmployee'),
    path("update/<str:id>/", views.updateEmployee,name='updateEmployee'),
    path("delete/<str:id>/", views.deleteEmployee,name='deleteEmployee'),
    path("",views.loginPage,name='login'),
    path("logout/",views.logoutPage,name='logout'),
    path("register/",views.register,name='register'),
]


