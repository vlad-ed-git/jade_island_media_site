"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from jade_island_media.views import(
    home_page_view,
    handler404,
    handler500,
)

from account.views import(
    registration_view,
    login_view,
    logout_view,
    profile_view,
    must_authenticate_view
)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('admin/', admin.site.urls),

    #language 
    re_path(r'^i18n/', include('django.conf.urls.i18n')),

    #user auth views
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name="profile"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/' , must_authenticate_view, name="must_authenticate"),

        # Password reset links
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='jade_island_media/account/password_reset/password_change_done.html'),
    name='password_change_done'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='jade_island_media/account/password_reset/password_change.html'),
    name='password_change'),
    
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='jade_island_media/account/password_reset/password_reset_done.html'),
    name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='jade_island_media/account/password_reset/password_reset_confirm.html'),
    name='password_reset_confirm'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='jade_island_media/account/password_reset/password_reset_form.html'),
    name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='jade_island_media/account/password_reset/password_reset_complete.html'),
    name='password_reset_complete'),
]

handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
