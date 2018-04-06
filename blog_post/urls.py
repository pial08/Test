from django.conf.urls import url, include
from blog_post import views

urlpatterns = [
    url(r'^post_list', views.post_list, name='post_list')
]