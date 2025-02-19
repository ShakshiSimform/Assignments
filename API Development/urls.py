from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, UserListView, register_user
urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    path('register/', register_user, name='register-user'), 
]
