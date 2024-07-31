from django.urls import path
from . import views

urlpatterns = [
    path('account_info/', views.account_info, name='account_info'),
]