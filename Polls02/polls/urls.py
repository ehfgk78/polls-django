"""polls URL Configuration

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = '첫페이지'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = '투표하기'),
    url(r'^(?P<질문번호>[0-9]+)/집계/$', views.집계, name = '집계'),
    url(r'^(?P<pk>[0-9]+)/결과/$', views.ResultsView.as_view(), name = '결과'),
]
