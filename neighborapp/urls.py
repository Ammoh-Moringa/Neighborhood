from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.registration, name='registration'),
    url('profile/', views.index, name='profile'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('new-hood/', views.add_neighbourhood, name='new-hood'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)