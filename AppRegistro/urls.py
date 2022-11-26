from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserRegisterView, UserEditView, PasswordChangeView


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name="profiles/change_password.html")),
    path('password/', views.PasswordsChangeView.as_view(template_name="profiles/change_password.html")),
    path('password_success', views.password_success, name="password_success"),
]



