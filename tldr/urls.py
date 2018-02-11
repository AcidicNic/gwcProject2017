from django.conf.urls import url
from tldr import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='main'),
    url(r'^results/', views.Done, name='results'),
    url(r'^about/', views.About, name='about')
]
