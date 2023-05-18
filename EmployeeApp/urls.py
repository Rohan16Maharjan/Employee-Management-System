from django.urls import path
from . import views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView
)

urlpatterns = [
    
    path('home/',views.home,name='home'),
    path('depart/',views.depart,name='depart'),
    path('emp/',views.emp,name='emp'),
    path("add/", views.addEmployee,name='addEmployee'),
    path("read/", views.readEmployee,name='viewEmployee'),
    path("readDepart/", views.readDepartment,name='viewDepartment'),
    path("readRole/", views.readRole,name='viewRole'),
    path("addDept/", views.addDepart,name='addDept'),
    path("addRole/", views.addRole,name='addRole'),
    path("update/<str:id>/", views.updateEmployee,name='updateEmployee'),
    path("delete/<str:id>/", views.deleteEmployee,name='deleteEmployee'),
    path("",views.loginPage,name='login'),
    path("logout/",views.logoutPage,name='logout'),
    path("register/",views.register,name='register'),
    path('reset-password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]




