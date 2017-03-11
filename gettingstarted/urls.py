from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import intellivest.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', intellivest.views.index, name='index'),
    url(r'^omoss', intellivest.views.omoss, name='omoss'),
    url(r'^portefolje', intellivest.views.portefolje, name='portefolje'),
    url(r'^kontaktsendt', intellivest.views.kontaktsendt, name='kontaktsendt'),
    url(r'^kontakt', intellivest.views.kontakt, name='kontakt'),
    url(r'^db', intellivest.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
