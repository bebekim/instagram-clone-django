from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Posts.as_view(), name='posts'),
    path('posts/post-create/', views.PostCreate.as_view(), name='post-create'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

"""
django.contrib.auth.urls에 포함됨

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""
