# HOOD URLS
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
# We will use this later for template tagging
app_name = 'hood'

urlpatterns = [
    url(r'^$', views.ListHoods.as_view(), name='all'),
    url(r'^new/$', views.NewHood.as_view(), name='new'),
    url(r'^posts/in/(?P<slug>[-\w]+)$',
        views.SingleHood.as_view(), name='single'),
    url(r'^join/(?P<slug>[-\w]+)$',
        views.JoinHood.as_view(), name='join'),
    url(r'^leave/(?P<slug>[-\w]+)$',
        views.LeaveHood.as_view(), name='leave'),
    url(r'^mtaa/$', views.mtaa, name='mtaa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
