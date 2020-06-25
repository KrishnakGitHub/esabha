from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from esabha import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('social/', include('social.urls')), 
    path('', RedirectView.as_view(url="social/")),  
    
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
    template_name='social/password_reset.html',
    subject_template_name='social/password_reset_subject.txt',
    html_email_template_name='social/password_reset_email.html'),
     name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='social/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
    template_name='social/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='social/password_reset_complete.html'), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='Profile/password_change.html'),
     name='password_change'),
    path('password-change-done/',
     auth_views.PasswordChangeDoneView.as_view(template_name='Profile/password_change_done.html'),
     name='password_change_done'),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

