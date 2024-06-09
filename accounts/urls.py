
  
from django.urls import path, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


app_name = "accounts"

urlpatterns=[
    path('signup/customer/', views.CustomerSignUpView.as_view(), name="customer_signup"),
    path('signup/plugmanager/', views.ManagerSignUpView.as_view(), name="plugmanager_signup"),
	path('sign-in', views.SignInView.as_view(), name="sign-in"),
	path('sign-out', views.sign_out, name="sign-out"),
    path('profile/', views.get_user_profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('login/customer/', views.loginView.as_view(), name="login"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]

