from django.urls import path, include
from todolist.views import show_todolist, register, login_user, logout_user, add_task, change_status, delete

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtask/', add_task, name='add_task'),
    path('change_status/<int:id>/', change_status, name='change_status'),
    path('delete/<int:id>/', delete, name='delete'),
]