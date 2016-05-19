from django.conf.urls import url
from robot_control import views

urlpatterns = [
    url(r'^votes/$', views.votes_list),
    url(r'^votes/(?P<session_id>[0-9]+)$', views.votes_list),
    url(r'^sessions/$', views.SessionList.as_view()),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view()),
    url(r'^robots/$', views.RobotList.as_view()),
]
