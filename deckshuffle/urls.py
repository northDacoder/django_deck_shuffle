from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'deckshuffle.views.card_list', name='cards'),
    url(r'^inheritance$', 'deckshuffle.views.inheritance', name='inheritance'),
    url(r'^inheritance2$', 'deckshuffle.views.inheritance2', name='inheritance2'),
    url(r'^specificcards$', 'deckshuffle.views.specific_cards', name='specific_cards'),
    url(r'^twocards$', 'deckshuffle.views.two_cards', name='two_cards'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
