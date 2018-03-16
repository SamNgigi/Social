from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'login/$',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),

    url(r'logout/$',
        auth_views.LogoutView.as_view(), name='logout'),

    url(r'register/$', views.SignUp.as_view(), name='register'),
    url(r'^$', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
