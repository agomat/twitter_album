"""twitter_album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import IndexView, TopicView, OwnerView

urlpatterns = [
    url(r'^(api)?$', IndexView.as_view(), name='index'),
    url(r'^(api/)?topic/(?P<topic>.*)$', TopicView.as_view(), name='topic'),
    url(r'^(api/)?owner/(?P<owner>.*)$', OwnerView.as_view(), name='owner'),
    url(r'^admin/', admin.site.urls),
]

###########
# Task testing purpose
#
# from datasource.tasker.TwitterTask import TwitterTask
# TwitterTask()
#
###########