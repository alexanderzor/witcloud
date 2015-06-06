from django.conf.urls import include, url
import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from clw import settings
from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    url(r'^need_board/(?P<key>\w+)/$', views.need_board, name='need_board'),
    url(r'^need_board$', views.need_board, name='need_board'),
    url(r'^need_vote/$', views.vote, name='need_vote'),
    url(r'^thank_board/$', views.thank_board, name='thank_board'),
    url(r'^vote_board/(?P<key>[0-9]+)/$', views.vote, name='vote'),
    url(r'^consults/$', views.consults, name='consults'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^archive/$', views.forbidden, name='archive'),
    #url(r'^uploader/$', views.uploader, name='uploader'),
    url(r'^private/(?P<key>\w+)/$', views.private, name='private'),
    url(r'^index/(?P<key>\w+)/$', views.index, name='index'),
    url(r'^private$', views.private, name='private'),
    url(r'^index$', views.index, name='index'),
    url(r'^$', RedirectView.as_view(url='index')),




]

