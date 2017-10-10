from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dashboard/$', views.siteapp_home, name='dashboard'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='detail'),
    url(r'^project/create/$', views.create_project, name='create'),
    url(r'^project/(?P<pk>\d+)/edit/$', views.project_edit, name='edit'),
    url(r'^analytics/$', views.chart, name="chart"),
]


