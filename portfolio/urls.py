from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.photo_category,name='photoCategory'),
    url(r'^about/',views.about,name='about'),
    url(r'^contact/',views.contact,name='contact'),


    url(r'^search/', views.search_results, name='search_results'),
]

##register the MEDIA_ROOT route inorder to serve uploaded images on the development server
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)