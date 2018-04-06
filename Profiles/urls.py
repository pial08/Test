from Profiles import views
from django.conf.urls import url

urlpatterns = [
    url('^$', views.Profiles, name='profile_view')
]