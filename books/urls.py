from django.conf.urls import patterns, include, url
from models import Publisher
from django.views.generic.list import ListView

#from views import search_form, search_res, contact, thank

urlpatterns = patterns('books.views',

        url(r'^search-form/$', 'search_form'),
        url(r'^$', 'search_form'),
        url(r'^haha(?P<num>\d{1,3})$', 'haha'),
        url(r'^publisher/$', ListView.as_view(queryset=Publisher.objects.all())),
        #url(r'^(haha)$', 'haha'),
        url(r'^foo$', 'hahaha', {'num':'foo'}),
        url(r'^bar$', 'hahaha', {'num':'bar'}),
        url(r'^contact/thanks/$', 'thank'),
        url(r'^contact/$', 'contact'),
        url(r'^search-res/$', 'search_res'),

        )
