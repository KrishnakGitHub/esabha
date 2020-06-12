from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView

import social
from college import views
urlpatterns = [
    path('notice/', views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),

    path('social/', include(social.urls)),

    path('', RedirectView.as_view(url="social/")),
]
