"""Defines URL patterns or this app"""
from django.urls import path # when mapping urls to views
from . import views

app_name = 'app_renekton'
# list of urls that can be requested from the current app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new post
    path('new_post/<int:topic_id>/', views.new_post, name='new_post'),
    # Page for editing a post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]

