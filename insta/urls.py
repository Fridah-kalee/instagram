from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.home,name='home'),
    re_path(r'^search/',views.search_results,name='search_results'),
    re_path(r'^post/',views.post,name='post'),
    re_path('accounts/register/', views.register, name='register'),
    re_path('profile/',views.profile,name='profile'),
    # re_path("likes/<int:pk/>",views.likes, name='likes'),
    # re_path(r'^likes/(?P<pk>\d+)/', views.likes, name = "likes"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)