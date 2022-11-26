from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import SignUpView

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    #path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
]


