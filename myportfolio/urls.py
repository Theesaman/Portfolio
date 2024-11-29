from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index_view,name='home-page'),
    path('blog/', BlogListView.as_view(), name='blog-page'),
    path('blog/<int:pk>/', blog_detail, name='detailsblog-page'), 
    path('About/',about_view,name='about-page'),
    path('Project/',project_view,name='project-page'),
    path('Contact/',ContactFormView.as_view(),name='contact-page'),
    path('Project/Details/',detailsproject_view,name='detailsproject-page')
]