from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/<int:page_id>/', views.view_page, name='view_page'),
]