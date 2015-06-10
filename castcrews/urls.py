from django.conf.urls import url
from django.views.generic import ListView, DetailView, TemplateView

from castcrews.models import Film, Person, Role


urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='castcrews/index.html'
    )),

    url(r'^films/$', ListView.as_view(
        model=Film,
    ), name='browse-films'),
    url(r'^people/$', ListView.as_view(
        model=Person,
    ), name='browse-people'),
    url(r'^roles/$', ListView.as_view(
        model=Role,
    ), name='browse-roles'),


    url(r'^films/(?P<pk>\d+)/$', DetailView.as_view(
        model=Film,
    ), name='show-film'),
    url(r'^people/(?P<pk>\d+)/$', DetailView.as_view(
        model=Person
    ), name='show-person'),
    url(r'^roles/(?P<pk>\d+)/$', DetailView.as_view(
        model=Role,
    ), name='show-role'),
]
