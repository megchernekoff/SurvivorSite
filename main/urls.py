from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('signup/', views.signup, name='signup'),
    path('page3', views.page3, name='page3')
]
