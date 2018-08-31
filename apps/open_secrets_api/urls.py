from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^candidate_summary$', views.candidate_summary, name="candidate_summary"),
]