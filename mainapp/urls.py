from django.urls import path,include
from .views import  NewsPostDetailView
from mainapp.views import *

urlpatterns = [
   
    path('', index_page ,name='index' ),
    path('news/',news_page , name='news'),
    path('about/',about_page , name='about'),
    path('talapker/',talapker_page , name='talapker'),
    path('student/',student_page , name='student'),
    path('gallery/',gallery_page , name='gallery'),
    path('contact/',contact_page , name='contact'),
    path('calendar/',calendar_page , name='calendar'),
    path('post/', news_single_page,name='news_single_page'),
    path('kodeks/', kodeks_page , name='kodeks'),
    path('post/<slug>',  NewsPostDetailView.as_view(), name='post_detail'),
    path('talapker/<slug>',TalapkerPostDetailView.as_view(), name='talapker_detail'),
    path('for_parent/', parents_page,name='for_parent'),
    path('profession/', profession_page , name='profession'),

        
]
