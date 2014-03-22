from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finalproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^dna/$', 'dna.views.dna', name='dna'),

    # url(r'^graphs/$', 'graphs.views.graphs', name='graphs'),

    url(r'^search/$', 'users.views.search', name='search'),

    url(r'^thanks/$', 'users.views.thanks', name='thanks'),

    url(r'^profiles/$', 'profiles.views.profiles', name='profiles'),

    # url(r'^tables/$', 'tables.views.tables', name='tables'),

    url(r'^users/$', 'users.views.users', name='users'),


)
