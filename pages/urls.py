from django.urls import path
from .views import HomePageView,AboutViewPage

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutViewPage.as_view(),name='about')
]