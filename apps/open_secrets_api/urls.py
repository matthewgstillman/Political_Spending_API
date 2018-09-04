from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^candidate_industry$', views.candidate_industry, name="candidate_industry"),
    url(r'^candidate_summary$', views.candidate_summary, name="candidate_summary"),
    url(r'^candidate_sectors$', views.candidate_sectors, name="candidate_sectors"),
    url(r'^candidate_contributions$', views.candidate_contributions, name="candidate_contributions"),
    url(r'^expenditures$', views.expenditures, name="expenditures"),
    url(r'^other_states$', views.other_states, name="other_states"),
    url(r'^select_candidate$', views.select_candidate, name="select_candidate"),
]