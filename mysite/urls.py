from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mysite.views import hello, curtime, hours_ahead, curtime2, display_meta, plot
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', curtime),
    url(r'^display/$', display_meta),
    url(r'^myxhh/$', 'mysite.views.myxhh'),
    url(r'^set/$', 'mysite.views.set_color'),
    url(r'^show/$', 'mysite.views.show_color'),
    url(r'^getparams/$', 'mysite.views.getparams'),
    url(r'^time/$', curtime2),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^urlpara/$', TemplateView.as_view(template_name="urlpara.html")),
    url(r'^plot/$', plot),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^hello/$', hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^books/', include('books.urls')),
)
