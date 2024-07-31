from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('status/', views.request_status, name='request_status'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('request/<int:pk>/update/', views.update_request_status, name='update_request_status'),
    path('request/<int:pk>/assign/', views.assign_rep, name='assign_rep'),
]


