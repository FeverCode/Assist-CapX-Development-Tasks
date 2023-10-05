from django.urls import path
from .views import index, view_bug, bug_list
from . import views

urlpatterns = [
    path('', index, name='home'),
    # path('register/', views.register_bug, name='register_bug'),
    path('bug/<int:bug_id>/', views.view_bug, name='view_bug'),
    path('bugs/', views.bug_list, name='bug_list'),
]
