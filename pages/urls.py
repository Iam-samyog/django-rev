from django.urls import path
from .views import HomePageView,AboutViewPage,BlogDetailView,BlogCreateView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutViewPage.as_view(),name='about'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(),name="post_new"),
]