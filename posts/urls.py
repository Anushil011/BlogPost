from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='posts'),
    path('posts/<slug:post_slug>',views.post_details, name="postDetail"),
    path('add-post/',views.addPost,name='add-post'),
    path('delete-post/<slug:post_slug>',views.deletePost,name="delete-post"),
    path('update-post/<slug:post_slug>',views.updatePost,name="update-post")
]