from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
