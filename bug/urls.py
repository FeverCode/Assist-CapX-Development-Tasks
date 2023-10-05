from django.urls import path
from .views import BugCreateView, BugDetailView, BugListView

urlpatterns = [
    path('', BugCreateView.as_view(), name='home'),
    path('bug/<int:bug_id>/', BugDetailView.as_view(), name='view_bug'),
    path('bugs/', BugListView.as_view(), name='bug_list'),
]
