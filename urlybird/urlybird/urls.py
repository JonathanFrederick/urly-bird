"""urlybird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bookmarkapp import views
# from django.views.generic import TemplateView

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/', views.UserCreateView.as_view(
        template_name='bookmarkapp/register.html'), name='register'),
    url(r'^user/(?P<pk>\d+)$', views.UserDetailView.as_view(),
        name='user_detail'),
    url(r'^to/(?P<short_url>\w+)$', views.short_to_long, name='short'),
    url(r'^add/', views.addbookmark, name='addbookmark'),
    url(r'^$', views.AllBookmarkView.as_view(), name='home_page'),
    url(r'^edit/(?P<uid>\d+)$', views.editbookmark, name='editbookmark'),
    url(r'^delete/(?P<uid>\d+)$', views.deletebookmark, name='deletebookmark')

]
