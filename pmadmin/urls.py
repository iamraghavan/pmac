# pmadmin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('o/secure/<str:unique_id>/admin-control/', views.dashboard, name='dashboard_secure'),
    path('o/secure/<str:unique_id>/admin-control/profile/', views.profile, name='profile_secure'),
    path('o/secure/<str:unique_id>/admin-control/logout/', views.logout, name='logout'),
    path('o/secure/update-marital-status/', views.update_marital_status, name='update_marital_status'),

    path('o/secure/<str:unique_id>/admin-control/payment-status/', views.payment, name='payment_secure'),
    path('o/secure/update-payment-status/', views.update_payment_status, name='update_payment_status'),

    path('o/secure/<str:unique_id>/admin-control/profile-view/', views.profile_view, name='profile_view_secure'),
    
]



