
from django.urls import path
from .views import article_list, register, logout_view, add_article, article_details, update_article, delete_article
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', article_list, name = 'article_list'),
    path('add-article/', add_article, name = 'add_article'),
    path('article/<slug:slug>/', article_details, name = 'article_details'),
    path('update/<slug:slug>/', update_article, name = 'update_article'),
    path('delete/<slug:slug>/', delete_article, name = 'delete_article'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register', register, name = 'register'),
]
