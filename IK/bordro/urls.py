from django.conf.urls import url
from .views import *

app_name = "bordro"

urlpatterns = [
    url(r'^bordroolustur/$', BordroOlustur, name="bordroolustur"),
    #url(r'^tanimlamalar/$', Tanimlamalar, name="tanimlamalar"),
]