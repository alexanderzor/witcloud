from django.conf.urls import include, url
from django.contrib import admin
import accounts
import broadcast
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from clw import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('broadcast.urls')),
    #url(r'^chat/$', include('chat.urls')),

]

