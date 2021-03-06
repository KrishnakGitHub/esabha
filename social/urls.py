from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from social import views
from django.views.generic.base import RedirectView

urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),
    
    path('myprofile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/social/home")),
    
    path('mypost/create/', views.MyPostCreate.as_view(success_url="/social/mypost")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/social/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    path('mypost/like/<int:pk>', views.like),
    path('mypost/unlike/<int:pk>', views.unlike),


    path('myprofile/', views.MyProfileListView.as_view()),
    path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),
    path('myprofile/follow/<int:pk>', views.follow),
    path('myprofile/unfollow/<int:pk>', views.unfollow),

    
    path('', RedirectView.as_view(url="home/")),

    path('allpost/',views.AllPost.as_view()),
    path('csv/',views.getfile),
    path('pdf/',views.getpdf),
    path('email1/',views.mail),
    path('thanks/',views.thanks),
    path('feedback/',views.Feedback_Form.as_view(success_url="/social/thanks")),
    path('fdd/<int:pk>',views.FeedbackDetailView.as_view()),
    path('faq/',views.QuestionCreate.as_view(success_url="/social/thanks")),
	
	
	path('emailform/', views.Email_Form),
    path('success/', views.successView),
    path('email2/', views.SendEmail),

    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),



#     path('mylist/', views.MyList.as_view()),
#accounts/ ^password/change/$ [name='auth_password_change']
#accounts/ ^password/change/done/$ [name='auth_password_change_done']
#accounts/ ^password/reset/$ [name='auth_password_reset']
#accounts/ ^password/reset/complete/$ [name='auth_password_reset_complete']
#accounts/ ^password/reset/done/$ [name='auth_password_reset_done']
#accounts/ ^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$ [name='auth_password_reset_confirm']
#social/
#     path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/college/home")),
]
