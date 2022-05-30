
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    re_path(r'^static/(?P<path>.*)$',serve, {'document_root':settings.STATIC_ROOT}),
]
