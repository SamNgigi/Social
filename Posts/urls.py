# POST VIEWS
from django.conf.urls import url
from . import views
# we will use this later for template tagging
app_name = 'post'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'^new/$', views.NewPost.as_view(), name='new'),
    url(r'^by/(?P<username>[-\w+])/$',
        views.UserPosts.as_view(), name='profile'),
    url(r'^by/(?P<username>[-\w+])(?P<pk>\d+)/$',
        views.PostDetail.as_view(), name='single'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete')
]
