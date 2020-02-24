from django.conf.urls import url
from .views_personel import  *
from .views_hareketler import  *
from .views_tanimlamalar import  *

app_name = "personel"

urlpatterns = [
    url(r'^tanimlamaolustur/$', TanimlamaOlustur, name="tanimlamaolustur"),
	url(r'^hareketolustur/$', HareketOlustur, name="hareketolustur"),
    url(r'^personelolustur/$', PersonelOlustur, name="personelolustur"),
]