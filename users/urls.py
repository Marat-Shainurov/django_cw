from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verify_email, UserUpdateView, user_list, UserCreateView, \
    UserDetailView, UserDeleteView, set_schedule

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='register'),
    path('registration/verification/<str:email>', verify_email, name='verify_email'),
    path('manager/list/', user_list, name='user_list'),
    path('create-user/', UserCreateView.as_view(), name='user_form'),
    path('manager/list/user-detail/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('manager/list/user-delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
    path('list/update/<int:pk>', UserUpdateView.as_view(), name='user_form'),
    path('manager/schedule-settings/', set_schedule, name='set_schedule')
]
