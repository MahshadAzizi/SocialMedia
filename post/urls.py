from django.urls import path
from .views import *


urlpatterns = [
    path('new_post', NewPost.as_view(), name='new_post'),
    path('new_comment/<int:post_id>', new_comment, name='new_comment'),
    path('all', Posts.as_view(), name='all'),
    path('postdetail/<int:pk>', PostDetail.as_view(), name='postdetail'),
    path('postsweek/', LastPostWeek.as_view(), name='postsweek'),
]

