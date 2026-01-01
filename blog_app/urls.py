from django.urls import path, register_converter
from . import views
from .feeds import LatestPostsFeed

class UnicodeSlugConverter:
    regex = '[-a-zA-Z0-9_éèàçôâêîûùëïü]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

register_converter(UnicodeSlugConverter, 'uslug')

app_name = 'blog_app'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    
    path('tag/<uslug:tag_slug>/',
         views.post_list,
         name='post_list_by_tag'),

    path('<int:year>/<int:month>/<int:day>/<uslug:post>/',
         views.post_detail,
         name='post_detail'),
    
    path('<int:post_id>/comment/',
         views.post_comment,
         name='post_comment'),
     path('<int:post_id>/share/', views.post_share, name='post_share'),
     path('feed/', LatestPostsFeed(), name='post_feed'),
     path('search/', views.post_search, name='post_search'),
]