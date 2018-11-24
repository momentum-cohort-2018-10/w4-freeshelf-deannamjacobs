"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from collection import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('admin/', admin.site.urls),
# ]




from django.contrib import admin
from django.urls import path, include 
# from django.views.generic import TemplateView, RedirectView
from collection import views
# from collection.backends import MyRegistrationView
# from django.contrib.auth.views import ( 
# 	PasswordResetView, PasswordResetDoneView, 
# 	PasswordResetConfirmView, PasswordResetCompleteView, 
# )

urlpatterns = [
    path('', views.index, name='home'),
    # path('contact/',
    #     TemplateView.as_view(template_name='contact.html'),
    #     name='contact'),
    # path('book_collection/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    # path('blogs/<slug>/', views.blog_detail,
    #     name='blog_detail'),
    # path('blogs/<slug>/edit/',
    #     views.edit_blog, name='edit_blog'),
    # path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    # path('browse/name/',
    #     views.browse_by_name, name='browse'),
    # path('browse/name/<initial>/',
    #     views.browse_by_name, name='browse_by_name'),
    # path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/password/reset/', 
    #     PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
    #     name="password_reset"),
    # path('accounts/password/reset/done/', 
    #     PasswordResetView.as_view(template_name='registration/password_reset_done.html'), 
    #     name="password_reset_done"),
    # path('accounts/password/reset/<uidb64>/<token>/', 
    #     PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
    #     name="password_reset_confirm"),
    # path('accounts/password/done/', 
    #     PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #     name="password_reset_complete"),
    # path('accounts/register/', 
    #      MyRegistrationView.as_view(), name='registration_register'),
    #  path('accounts/create_blog/', 
    #      views.create_blog, name='registration_create_blog'),
    # path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
