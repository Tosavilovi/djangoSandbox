from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'1/$', views.index_html, name="index"),
    url(r'contacts/$', views.contacts, name="contacts")
    
]