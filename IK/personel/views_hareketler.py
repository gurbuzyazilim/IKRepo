from kullanicilar.models import *
from .models_hareketler import *
from .models_tanimlamalar import *
from .models_personel import *
from .meslekler import *
from .sehirler import *
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone


def HareketOlustur(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session["KullaniciKodu"],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsKullanicilar == True):
			islemlerKontrol = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
			if(islemlerKontrol.IsKullaniciOlustur == True):
				if(request.is_ajax()):
					ajaxDetay = request.POST.get("ajaxDetay")
					ajaxHareketlerDetay = request.POST.get("ajaxHareketlerDetay")
					veriTabaniDegiskeniDetay = ""
					if(ajaxDetay != None):
						if(ajaxHareketlerDetay == "adresler"):
							veriTabaniDegiskeniDetay = HareketAdresler
							hareketlerBaslikDetay    = ["id","PersonelKodu","AdresKodu","KapiNo","ApartmanNo","ApartmanAdi","Sokak","Cadde","Mahalle","Ilce","Il","Bolge","Ulke","PostaKodu","Tel"]
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "bankaHesaplari"):
							veriTabaniDegiskeniDetay = HareketBankaHesaplari
							hareketlerBaslikDetay    = ["id","PersonelKodu","BankaKodu","Iban","HesapNo","IsimSoyisim"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "destekler"):
							veriTabaniDegiskeniDetay = HareketDestekler
							hareketlerBaslikDetay    = ["id","PersonelKodu","DestekTuru","Miktar","BaslangicTarihi","BitisTarihi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "digerKimlikler"):
							veriTabaniDegiskeniDetay = HareketDigerKimlikler
							hareketlerBaslikDetay    = ["id","PersonelKodu","KimlikKodu","BelgeNo","TurSınıf","VerenMakam","DuzenlemeTarihi","GecerlilikTarihi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "aileBilgileri"):
							veriTabaniDegiskeniDetay = HareketAileBilgileri
							hareketlerBaslikDetay    = ["id","PersonelKodu","AileFerdiAdiSoyadi","AileFerdiDogumTarihi","AileFerdiTuru","AileFerdiTelefon","AileFerdiPersonelKodu","Çalışıyor mu ?","AileFerdiMeslek"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "vizeler"):
							veriTabaniDegiskeniDetay = HareketVizeler
							hareketlerBaslikDetay    = ["id","PersonelKodu","VizeKodu","VizeUlkeBolge","VizeBelgeNo","VizeBaslangicTarihi","VizeBitisTarihi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)		
						if(ajaxHareketlerDetay == "dernekler"):
							veriTabaniDegiskeniDetay = HareketDernekler
							hareketlerBaslikDetay    = ["id","PersonelKodu","DernekAdi","DernekFaaliyetDetayi","UyeNo","UyePozisyon","UyelikTarihi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "hukumlulukler"):
							veriTabaniDegiskeniDetay = HareketHukumlulukler
							hareketlerBaslikDetay    = ["id","PersonelKodu","CezaeviTuru","CezaeviTipi","IsnadEdilenFiil","IsnadEdilenFiilDetayi","HapisSuresi","HapishaneBaslangic","HapishaneBitis","TamamlananHapisSuresi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "meslekler"):
							veriTabaniDegiskeniDetay = HareketMeslekler
							hareketlerBaslikDetay    = ["id","PersonelKodu","MeslekAdi","MeslekDetayi","Tecrubesi","OkulKursKodu","BelgeSertifikaKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "isGecmisi"):
							veriTabaniDegiskeniDetay = HareketIsGecmisi
							hareketlerBaslikDetay    = ["id","PersonelKodu","SirketAdi","SirketUlke","SirketSehir","SirketTel","CalismaTuru","Departman","Pozisyon","BaslangicTarihi","BitisTarihi","AyrilikSebebi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "okullarKurslar"):
							veriTabaniDegiskeniDetay = HareketOkullarKurslar
							hareketlerBaslikDetay    = ["id","PersonelKodu","OkulKursAdi","Ulke","Sehir","BolumAdi","BaslangicTarihi","BitisTarihi","BelgeAdi","BelgeTuru","BelgeTarihi","BelgeKaynak"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)		
						if(ajaxHareketlerDetay == "nitelikler"):
							veriTabaniDegiskeniDetay = HareketNitelikler
							hareketlerBaslikDetay    = ["id","PersonelKodu","NitelikKodu","NitelikTecrubesi","NitelikSeviyesi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "diller"):
							veriTabaniDegiskeniDetay = HareketDiller
							hareketlerBaslikDetay    = ["id","PersonelKodu","DilKodu","OgrenimTuru","OkumaSeviyesi","YazmaSeviyesi","KonusmaSeviyesi","OkulKursKodu","BelgeSertifikaKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "fazlaMesailer"):
							veriTabaniDegiskeniDetay = HareketFazlaMesailer
							hareketlerBaslikDetay    = ["id","PersonelKodu","MesaiTuru","MesaiTarihi","SaatAraligi1","SaatAraligi2","Saati","ArttirimOrani","MesaiUcreti"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "gorevler"):
							veriTabaniDegiskeniDetay = HareketGorevler
							hareketlerBaslikDetay    = ["id","PersonelKodu","GorevKodu","DepartmanKodu","GorevAmiriKodu","BaslangicTarihi","BitisTarihi","GorevSonuc","GorevSonucDetayi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "performanslar"):
							veriTabaniDegiskeniDetay = HareketPerformanslar
							hareketlerBaslikDetay    = ["id","PersonelKodu","PerformansKodu","DegerlendirmeyiYapan","PerformansPeriyodu","DegerlendirmePuani","DegerlendirmePuaniDetayi"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)					
						if(ajaxHareketlerDetay == "yardimlar"):
							veriTabaniDegiskeniDetay = HareketYardimlar
							hareketlerBaslikDetay    = ["id","PersonelKodu","YardimKodu","YardimTarihi","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "izinler"):
							veriTabaniDegiskeniDetay = HareketIzinler
							hareketlerBaslikDetay    = ["id","PersonelKodu","IzinTuru","IzinSebebi","BaslangicTarihi","BitisTarihi","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "avanslar"):
							veriTabaniDegiskeniDetay = HareketlerAvanslar
							hareketlerBaslikDetay    = ["id","PersonelKodu","AvansTuru","AvansSebebi","AvansMiktari","AvansTarihi","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "primler"):
							veriTabaniDegiskeniDetay = HareketPrimler
							hareketlerBaslikDetay    = ["id","PersonelKodu","PrimTuru","PrimSebebi","PrimMiktari","PrimTarihi","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "tahakkuklar"):
							veriTabaniDegiskeniDetay = HareketTahakkuklar
							hareketlerBaslikDetay    = ["id","PersonelKodu","TahakkukTuru","TahakkukSebebi","TahakkukMiktari","TahakkukTarihi","TahakkukPeriyodu","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "ikramiyeler"):
							veriTabaniDegiskeniDetay = HareketlerIkramiyeler
							hareketlerBaslikDetay    = ["id","PersonelKodu","IkramiyeTuru","IkramiyeSebebi","IkramiyeMiktari","IkramiyeTarihi","MuhasebeIslemKodu"] 
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)							
						if(ajaxHareketlerDetay == "kesintiler"):
							veriTabaniDegiskeniDetay = HareketKesintiler
							hareketlerBaslikDetay    = ["id","PersonelKodu","KesintiTuru","KesintiSebebi","KesintiMiktari","KesintiTarihi","MuhasebeIslemKodu"]
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						if(ajaxHareketlerDetay == "zimmetler"):
							veriTabaniDegiskeniDetay = HareketZimmetler
							hareketlerBaslikDetay    = ["id","PersonelKodu","Kategori","Marka","Model","Miktar","AlanKisi","VerenKisi","Aciklama1","Aciklama2","Aciklama3","BaslangicTarihi","BitisTarihi","MuhasebeIslemKodu"]
							sqlHareketlerDetay       = veriTabaniDegiskeniDetay.objects.values_list().get(id=ajaxDetay)
						context = {
							"ajaxHareketlerBaslikDetay" : hareketlerBaslikDetay,
							"ajaxSqlHareketlerDetay"    : sqlHareketlerDetay,
							}
						return JsonResponse(context)	
					ajaxSil = request.POST.get("ajaxSil")
					ajaxHareketlerSil = request.POST.get("ajaxHareketlerSil")
					if(ajaxSil != None):
						veriTabaniDegiskeniSil = ""
						if(ajaxHareketlerSil == "adresler"):
							veriTabaniDegiskeniSil = HareketAdresler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "bankaHesaplari"):
							veriTabaniDegiskeniSil = HareketBankaHesaplari	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "destekler"):
							veriTabaniDegiskeniSil = HareketDestekler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()	
						if(ajaxHareketlerSil == "digerKimlikler"):
							veriTabaniDegiskeniSil = HareketDigerKimlikler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "aileBilgileri"):
							veriTabaniDegiskeniSil = HareketAileBilgileri	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "vizeler"):
							veriTabaniDegiskeniSil = HareketVizeler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "dernekler"):
							veriTabaniDegiskeniSil = HareketDernekler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "hukumlulukler"):
							veriTabaniDegiskeniSil = HareketHukumlulukler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "meslekler"):
							veriTabaniDegiskeniSil = HareketMeslekler
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()	
						if(ajaxHareketlerSil == "isGecmisi"):
							veriTabaniDegiskeniSil = HareketIsGecmisi	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "okullarKurslar"):
							veriTabaniDegiskeniSil = HareketOkullarKurslar
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "nitelikler"):
							veriTabaniDegiskeniSil = HareketNitelikler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "diller"):
							veriTabaniDegiskeniSil = HareketDiller	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "fazlaMesailer"):
							veriTabaniDegiskeniSil = HareketFazlaMesailer	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()	
						if(ajaxHareketlerSil == "gorevler"):
							veriTabaniDegiskeniSil = HareketGorevler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "performanslar"):
							veriTabaniDegiskeniSil = HareketPerformanslar	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "yardimlar"):
							veriTabaniDegiskeniSil = HareketYardimlar	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "izinler"):
							veriTabaniDegiskeniSil = HareketIzinler	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "avanslar"):
							veriTabaniDegiskeniSil = HareketlerAvanslar	
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "primler"):
							veriTabaniDegiskeniSil = HareketPrimler
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "tahakkuklar"):
							veriTabaniDegiskeniSil = HareketTahakkuklar
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "ikramiyeler"):
							veriTabaniDegiskeniSil = HareketlerIkramiyeler
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "kesintiler"):
							veriTabaniDegiskeniSil = HareketKesintiler
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()
						if(ajaxHareketlerSil == "zimmetler"):
							veriTabaniDegiskeniSil = HareketZimmetler
							sqlHareketlerSil = get_object_or_404(veriTabaniDegiskeniSil,id=ajaxSil)
							sqlHareketlerSil.IsDeleted = True
							sqlHareketlerSil.save()				
						context = {"ajaxMesaj"  : "Silindi !"}
						return JsonResponse(context)

					ajaxGuncelle = request.POST.get("ajaxGuncelle")
					ajaxHareketlerGuncelle = request.POST.get("ajaxHareketlerGuncelle")
					if(ajaxGuncelle != None):
						veriTabaniDegiskeniGuncelle = ""
						if(ajaxHareketlerGuncelle == "adresler"):
							veriTabaniDegiskeniGuncelle = HareketAdresler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "bankaHesaplari"):
							veriTabaniDegiskeniGuncelle = HareketBankaHesaplari
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)	
						if(ajaxHareketlerGuncelle == "destekler"):
							veriTabaniDegiskeniGuncelle = HareketDestekler
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "digerKimlikler"):
							veriTabaniDegiskeniGuncelle = HareketDigerKimlikler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "aileBilgileri"):
							veriTabaniDegiskeniGuncelle = HareketAileBilgileri	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "vizeler"):
							veriTabaniDegiskeniGuncelle = HareketVizeler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "dernekler"):
							veriTabaniDegiskeniGuncelle = HareketDernekler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "hukumlulukler"):
							veriTabaniDegiskeniGuncelle = HareketHukumlulukler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "meslekler"):
							veriTabaniDegiskeniGuncelle = HareketMeslekler
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "isGecmisi"):
							veriTabaniDegiskeniGuncelle = HareketIsGecmisi	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "okullarKurslar"):
							veriTabaniDegiskeniGuncelle = HareketOkullarKurslar
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "nitelikler"):
							veriTabaniDegiskeniGuncelle = HareketNitelikler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)	
						if(ajaxHareketlerGuncelle == "diller"):
							veriTabaniDegiskeniGuncelle = HareketDiller	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "fazlaMesailer"):
							veriTabaniDegiskeniGuncelle = HareketFazlaMesailer	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "gorevler"):
							veriTabaniDegiskeniGuncelle = HareketGorevler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "performanslar"):
							veriTabaniDegiskeniGuncelle = HareketPerformanslar	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "yardimlar"):
							veriTabaniDegiskeniGuncelle = HareketYardimlar	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "izinler"):
							veriTabaniDegiskeniGuncelle = HareketIzinler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "avanslar"):
							veriTabaniDegiskeniGuncelle = HareketlerAvanslar	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "primler"):
							veriTabaniDegiskeniGuncelle = HareketPrimler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "tahakkuklar"):
							veriTabaniDegiskeniGuncelle = HareketTahakkuklar	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "ikramiyeler"):
							veriTabaniDegiskeniGuncelle = HareketlerIkramiyeler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "kesintiler"):
							veriTabaniDegiskeniGuncelle = HareketKesintiler	
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						if(ajaxHareketlerGuncelle == "zimmetler"):
							veriTabaniDegiskeniGuncelle = HareketZimmetler
							sqlHareketlerGuncelle = veriTabaniDegiskeniGuncelle.objects.values_list().get(id=ajaxGuncelle)
						context = {"ajaxHareketlerGuncelle"  : sqlHareketlerGuncelle}
						return JsonResponse(context)	
					ajaxHareketler = request.POST.get("ajaxHareketler")
					if(ajaxHareketler != None):
						veriTabaniDegiskeni = ""
						if(ajaxHareketler == "adresler"):
							veriTabaniDegiskeni = HareketAdresler
							hareketlerBaslik    = ["id","PersonelKodu","AdresKodu","KapiNo","ApartmanNo","ApartmanAdi","Sokak","Cadde","Mahalle","Ilce","Il","Bolge","Ulke","PostaKodu","Tel"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)	
						if(ajaxHareketler == "bankaHesaplari"):
							veriTabaniDegiskeni = HareketBankaHesaplari
							hareketlerBaslik    = ["id","PersonelKodu","BankaKodu","Iban","HesapNo","IsimSoyisim"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "destekler"):
							veriTabaniDegiskeni = HareketDestekler
							hareketlerBaslik    = ["id","PersonelKodu","DestekTuru","Miktar","BaslangicTarihi","BitisTarihi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "digerKimlikler"):
							veriTabaniDegiskeni = HareketDigerKimlikler
							hareketlerBaslik    = ["id","PersonelKodu","KimlikKodu","BelgeNo","TurSınıf","VerenMakam","DuzenlemeTarihi","GecerlilikTarihi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)		
						if(ajaxHareketler == "aileBilgileri"):
							veriTabaniDegiskeni = HareketAileBilgileri
							hareketlerBaslik    = ["id","PersonelKodu","AileFerdiAdiSoyadi","AileFerdiDogumTarihi","AileFerdiTuru","AileFerdiTelefon","AileFerdiPersonelKodu","Çalışıyor Mu ?","AileFerdiMeslek"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "vizeler"):
							veriTabaniDegiskeni = HareketVizeler
							hareketlerBaslik    = ["id","PersonelKodu","VizeKodu","VizeUlkeBolge","VizeBelgeNo","VizeBaslangicTarihi","VizeBitisTarihi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)		
						if(ajaxHareketler == "dernekler"):
							veriTabaniDegiskeni = HareketDernekler
							hareketlerBaslik    = ["id","PersonelKodu","DernekAdi","DernekFaaliyetDetayi","UyeNo","UyePozisyon","UyelikTarihi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "hukumlulukler"):
							veriTabaniDegiskeni = HareketHukumlulukler
							hareketlerBaslik    = ["id","PersonelKodu","CezaeviTuru","CezaeviTipi","IsnadEdilenFiil","IsnadEdilenFiilDetayi","HapisSuresi","HapishaneBaslangic","HapishaneBitis","TamamlananHapisSuresi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "meslekler"):
							veriTabaniDegiskeni = HareketMeslekler
							hareketlerBaslik    = ["id","PersonelKodu","MeslekAdi","MeslekDetayi","Tecrubesi","OkulKursKodu","BelgeSertifikaKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "isGecmisi"):
							veriTabaniDegiskeni = HareketIsGecmisi
							hareketlerBaslik    = ["id","PersonelKodu","SirketAdi","SirketUlke","SirketSehir","SirketTel","CalismaTuru","Departman","Pozisyon","BaslangicTarihi","BitisTarihi","AyrilikSebebi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "okullarKurslar"):
							veriTabaniDegiskeni = HareketOkullarKurslar
							hareketlerBaslik    = ["id","PersonelKodu","OkulKursAdi","Ulke","Sehir","BolumAdi","BaslangicTarihi","BitisTarihi","BelgeAdi","BelgeTuru","BelgeTarihi","BelgeKaynak"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)		
						if(ajaxHareketler == "nitelikler"):
							veriTabaniDegiskeni = HareketNitelikler
							hareketlerBaslik    = ["id","PersonelKodu","NitelikKodu","NitelikTecrubesi","NitelikSeviyesi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "diller"):
							veriTabaniDegiskeni = HareketDiller
							hareketlerBaslik    = ["id","PersonelKodu","DilKodu","OgrenimTuru","OkumaSeviyesi","YazmaSeviyesi","KonusmaSeviyesi","OkulKursKodu","BelgeSertifikaKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "fazlaMesailer"):
							veriTabaniDegiskeni = HareketFazlaMesailer
							hareketlerBaslik    = ["id","PersonelKodu","MesaiTuru","MesaiTarihi","SaatAraligi1","SaatAraligi2","Saati","ArttirimOrani","MesaiUcreti"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)	
						if(ajaxHareketler == "gorevler"):
							veriTabaniDegiskeni = HareketGorevler
							hareketlerBaslik    = ["id","PersonelKodu","GorevKodu","DepartmanKodu","GorevAmiriKodu","BaslangicTarihi","BitisTarihi","GorevSonuc","GorevSonucDetayi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "performanslar"):
							veriTabaniDegiskeni = HareketPerformanslar
							hareketlerBaslik    = ["id","PersonelKodu","PerformansKodu","DegerlendirmeyiYapan","PerformansPeriyodu","DegerlendirmePuani","DegerlendirmePuaniDetayi"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)					
						if(ajaxHareketler == "yardimlar"):
							veriTabaniDegiskeni = HareketYardimlar
							hareketlerBaslik    = ["id","PersonelKodu","YardimKodu","YardimTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "izinler"):
							veriTabaniDegiskeni = HareketIzinler
							hareketlerBaslik    = ["id","PersonelKodu","IzinTuru","IzinSebebi","BaslangicTarihi","BitisTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "avanslar"):
							veriTabaniDegiskeni = HareketlerAvanslar
							hareketlerBaslik    = ["id","PersonelKodu","AvansTuru","AvansSebebi","AvansMiktari","AvansTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "primler"):
							veriTabaniDegiskeni = HareketPrimler
							hareketlerBaslik    = ["id","PersonelKodu","PrimTuru","PrimSebebi","PrimMiktari","PrimTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "tahakkuklar"):
							veriTabaniDegiskeni = HareketTahakkuklar
							hareketlerBaslik    = ["id","PersonelKodu","TahakkukTuru","TahakkukSebebi","TahakkukMiktari","TahakkukTarihi","TahakkukPeriyodu","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "ikramiyeler"):
							veriTabaniDegiskeni = HareketlerIkramiyeler
							hareketlerBaslik    = ["id","PersonelKodu","IkramiyeTuru","IkramiyeSebebi","IkramiyeMiktari","IkramiyeTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)								
						if(ajaxHareketler == "kesintiler"):
							veriTabaniDegiskeni = HareketKesintiler
							hareketlerBaslik    = ["id","PersonelKodu","KesintiTuru","KesintiSebebi","KesintiMiktari","KesintiTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						if(ajaxHareketler == "zimmetler"):
							veriTabaniDegiskeni = HareketZimmetler
							hareketlerBaslik    = ["id","PersonelKodu","Kategori","Marka","Model","Miktar","AlanKisi","VerenKisi","Aciklama1","Aciklama2","Aciklama3","BaslangicTarihi","BitisTarihi","MuhasebeIslemKodu"] 
							hareketlerListesi   = []
							for sqlHareketler in veriTabaniDegiskeni.objects.values_list().filter(IsDeleted=False):
								hareketlerListesi.append(sqlHareketler)
						context = {
							"ajaxHareketlerBaslik"  : hareketlerBaslik,
							"ajaxHareketlerListesi" : hareketlerListesi,
						}
						return JsonResponse(context)
					ajaxArguman  = request.POST.get("ajaxArguman")
					ajaxArguman2 = request.POST.get("ajaxArguman2")
					ajaxArguman3 = request.POST.get("ajaxArguman3")
					ajaxPersonel = request.POST.get("ajaxPersonel")
					if(ajaxArguman == "adresler"):
						ajaxAdresKodu   = request.POST.get("ajaxAdresKodu")
						ajaxKapiNo      = request.POST.get("ajaxKapiNo")
						ajaxApartmanNo  = request.POST.get("ajaxApartmanNo")
						ajaxApartmanAdi = request.POST.get("ajaxApartmanAdi")
						ajaxSokak       = request.POST.get("ajaxSokak")
						ajaxCadde       = request.POST.get("ajaxCadde")
						ajaxMahalle     = request.POST.get("ajaxMahalle")
						ajaxIlce        = request.POST.get("ajaxIlce")
						ajaxIl          = request.POST.get("ajaxIl")
						ajaxBolge       = request.POST.get("ajaxBolge")
						ajaxUlke        = request.POST.get("ajaxUlke")
						ajaxPostaKodu   = request.POST.get("ajaxPostaKodu")
						ajaxTel         = request.POST.get("ajaxTel")
						if(ajaxArguman2 == "1"):
							sqlAdreslerGuncelle = get_object_or_404(HareketAdresler,id=ajaxArguman3)
							sqlAdreslerGuncelle.LastUpUser   = request.session["KullaniciKodu"]
							sqlAdreslerGuncelle.LastUpDate   = timezone.now() 
							sqlAdreslerGuncelle.PersonelKodu = ajaxPersonel
							sqlAdreslerGuncelle.AdresKodu    = ajaxAdresKodu
							sqlAdreslerGuncelle.KapiNo       = ajaxKapiNo
							sqlAdreslerGuncelle.ApartmanNo   = ajaxApartmanNo
							sqlAdreslerGuncelle.ApartmanAdi  = ajaxApartmanAdi
							sqlAdreslerGuncelle.Sokak        = ajaxSokak
							sqlAdreslerGuncelle.Cadde        = ajaxCadde
							sqlAdreslerGuncelle.Mahalle      = ajaxMahalle
							sqlAdreslerGuncelle.Ilce         = ajaxIlce
							sqlAdreslerGuncelle.Il           = ajaxIl
							sqlAdreslerGuncelle.Bolge        = ajaxBolge
							sqlAdreslerGuncelle.Ulke         = ajaxUlke
							sqlAdreslerGuncelle.PostaKodu    = ajaxPostaKodu
							sqlAdreslerGuncelle.Tel          = ajaxTel
							sqlAdreslerGuncelle.save()
						else:
							sqlAdresler = HareketAdresler()
							sqlAdresler.CreateUser   = request.session["KullaniciKodu"]
							sqlAdresler.CreateDate   = timezone.now() 
							sqlAdresler.PersonelKodu = ajaxPersonel
							sqlAdresler.AdresKodu    = ajaxAdresKodu
							sqlAdresler.KapiNo       = ajaxKapiNo
							sqlAdresler.ApartmanNo   = ajaxApartmanNo
							sqlAdresler.ApartmanAdi  = ajaxApartmanAdi
							sqlAdresler.Sokak        = ajaxSokak
							sqlAdresler.Cadde        = ajaxCadde
							sqlAdresler.Mahalle      = ajaxMahalle
							sqlAdresler.Ilce         = ajaxIlce
							sqlAdresler.Il           = ajaxIl
							sqlAdresler.Bolge        = ajaxBolge
							sqlAdresler.Ulke         = ajaxUlke
							sqlAdresler.PostaKodu    = ajaxPostaKodu
							sqlAdresler.Tel          = ajaxTel
							sqlAdresler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)

					if(ajaxArguman == "bankaHesaplari"):
						ajaxBankaKodu   = request.POST.get("ajaxBankaKodu")
						ajaxIban        = request.POST.get("ajaxIban")
						ajaxHesapNo     = request.POST.get("ajaxHesapNo")
						ajaxIsimSoyisim = request.POST.get("ajaxIsimSoyisim")
						if(ajaxArguman2 == "1"):
							sqlBankaHesaplariGuncelle = get_object_or_404(HareketBankaHesaplari,id=ajaxArguman3)
							sqlBankaHesaplariGuncelle.LastUpUser   = request.session["KullaniciKodu"]
							sqlBankaHesaplariGuncelle.LastUpDate   = timezone.now() 
							sqlBankaHesaplariGuncelle.PersonelKodu = ajaxPersonel
							sqlBankaHesaplariGuncelle.BankaKodu    = ajaxBankaKodu
							sqlBankaHesaplariGuncelle.Iban         = ajaxIban
							sqlBankaHesaplariGuncelle.HesapNo      = int(ajaxHesapNo)
							sqlBankaHesaplariGuncelle.IsimSoyisim  = ajaxIsimSoyisim
							sqlBankaHesaplariGuncelle.save()
						else:
							sqlBankaHesaplari = HareketBankaHesaplari()
							sqlBankaHesaplari.CreateUser   = request.session["KullaniciKodu"]
							sqlBankaHesaplari.CreateDate   = timezone.now() 
							sqlBankaHesaplari.PersonelKodu = ajaxPersonel
							sqlBankaHesaplari.BankaKodu    = ajaxBankaKodu
							sqlBankaHesaplari.Iban         = ajaxIban
							sqlBankaHesaplari.HesapNo      = int(ajaxHesapNo)
							sqlBankaHesaplari.IsimSoyisim  = ajaxIsimSoyisim
							sqlBankaHesaplari.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)

					if(ajaxArguman == "destekler"):
						ajaxDestekTuru    = request.POST.get("ajaxDestekTuru")
						ajaxDestekMiktari = request.POST.get("ajaxDestekMiktari")
						ajaxDestekBasTar  = request.POST.get("ajaxDestekBasTar")
						ajaxDestekBitTar  = request.POST.get("ajaxDestekBitTar")
						if(ajaxArguman2 == "1"):
							sqlDesteklerGuncelle = get_object_or_404(HareketDestekler,id=ajaxArguman3)
							sqlDesteklerGuncelle.LastUpUser      = request.session["KullaniciKodu"]
							sqlDesteklerGuncelle.LastUpDate      = timezone.now()
							sqlDesteklerGuncelle.PersonelKodu    = ajaxPersonel
							sqlDesteklerGuncelle.DestekTuru      = ajaxDestekTuru
							sqlDesteklerGuncelle.Miktar          = float(ajaxDestekMiktari)
							sqlDesteklerGuncelle.BaslangicTarihi = ajaxDestekBasTar
							sqlDesteklerGuncelle.BitisTarihi     = ajaxDestekBitTar
							sqlDesteklerGuncelle.save()
						else:
							sqlDestekler = HareketDestekler()
							sqlDestekler.CreateUser      = request.session["KullaniciKodu"]
							sqlDestekler.CreateDate      = timezone.now()
							sqlDestekler.PersonelKodu    = ajaxPersonel
							sqlDestekler.DestekTuru      = ajaxDestekTuru
							sqlDestekler.Miktar          = float(ajaxDestekMiktari)
							sqlDestekler.BaslangicTarihi = ajaxDestekBasTar
							sqlDestekler.BitisTarihi     = ajaxDestekBitTar
							sqlDestekler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "digerKimlikler"):
						ajaxKimlikKodu             = request.POST.get("ajaxKimlikKodu")
						ajaxKimlikBelgeNo          = request.POST.get("ajaxKimlikBelgeNo")
						ajaxKimlikTurSinif         = request.POST.get("ajaxKimlikTurSinif")
						ajaxKimlikVerenMakam       = request.POST.get("ajaxKimlikVerenMakam")
						ajaxKimlikDuzenlemeTarihi  = request.POST.get("ajaxKimlikDuzenlemeTarihi")
						ajaxKimlikGecerlilikTarihi = request.POST.get("ajaxKimlikGecerlilikTarihi")
						if(ajaxArguman2 == "1"):
							sqlDigerKimliklerGuncelle = get_object_or_404(HareketDigerKimlikler,id=ajaxArguman3)
							sqlDigerKimliklerGuncelle.LastUpUser       = request.session["KullaniciKodu"]
							sqlDigerKimliklerGuncelle.LastUpDate       = timezone.now() 
							sqlDigerKimliklerGuncelle.PersonelKodu     = ajaxPersonel
							sqlDigerKimliklerGuncelle.KimlikKodu       = ajaxKimlikKodu
							sqlDigerKimliklerGuncelle.BelgeNo          = ajaxKimlikBelgeNo
							sqlDigerKimliklerGuncelle.TurSinif         = ajaxKimlikTurSinif
							sqlDigerKimliklerGuncelle.VerenMakam       = ajaxKimlikVerenMakam
							sqlDigerKimliklerGuncelle.DuzenlemeTarihi  = ajaxKimlikDuzenlemeTarihi
							sqlDigerKimliklerGuncelle.GecerlilikTarihi = ajaxKimlikGecerlilikTarihi
							sqlDigerKimliklerGuncelle.save()
						else:
							sqlDigerKimlikler = HareketDigerKimlikler()
							sqlDigerKimlikler.CreateUser       = request.session["KullaniciKodu"]
							sqlDigerKimlikler.CreateDate       = timezone.now() 
							sqlDigerKimlikler.PersonelKodu     = ajaxPersonel
							sqlDigerKimlikler.KimlikKodu       = ajaxKimlikKodu
							sqlDigerKimlikler.BelgeNo          = ajaxKimlikBelgeNo
							sqlDigerKimlikler.TurSinif         = ajaxKimlikTurSinif
							sqlDigerKimlikler.VerenMakam       = ajaxKimlikVerenMakam
							sqlDigerKimlikler.DuzenlemeTarihi  = ajaxKimlikDuzenlemeTarihi
							sqlDigerKimlikler.GecerlilikTarihi = ajaxKimlikGecerlilikTarihi
							sqlDigerKimlikler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "aileBilgileri"):
						ajaxAileFerdiAdSoyad      = request.POST.get("ajaxAileFerdiAdSoyad")
						ajaxAileFerdiDogumTarihi  = request.POST.get("ajaxAileFerdiDogumTarihi")
						ajaxAileFerdiTuru         = request.POST.get("ajaxAileFerdiTuru")
						ajaxAileFerdiTel          = request.POST.get("ajaxAileFerdiTel")
						ajaxAileFerdiPersonelKodu = request.POST.get("ajaxAileFerdiPersonelKodu")
						ajaxAileFerdiCalisiyor    = request.POST.get("ajaxAileFerdiCalisiyor")
						ajaxAileFerdiMeslek       = request.POST.get("ajaxAileFerdiMeslek")
						if(ajaxArguman2 == "1"):
							sqlAileBilgileriGuncelle = get_object_or_404(HareketAileBilgileri,id=ajaxArguman3)
							sqlAileBilgileriGuncelle.LastUpUser            = request.session["KullaniciKodu"]
							sqlAileBilgileriGuncelle.LastUpDate            = timezone.now() 
							sqlAileBilgileriGuncelle.PersonelKodu          = ajaxPersonel
							sqlAileBilgileriGuncelle.AileFerdiAdiSoyadi    = ajaxAileFerdiAdSoyad
							sqlAileBilgileriGuncelle.AileFerdiDogumTarihi  = ajaxAileFerdiDogumTarihi
							sqlAileBilgileriGuncelle.AileFerdiTuru         = ajaxAileFerdiTuru
							sqlAileBilgileriGuncelle.AileFerdiTelefon      = ajaxAileFerdiTel
							sqlAileBilgileriGuncelle.AileFerdiPersonelKodu = ajaxAileFerdiPersonelKodu
							sqlAileBilgileriGuncelle.Calisiyor             = ajaxAileFerdiCalisiyor
							sqlAileBilgileriGuncelle.Meslek                = ajaxAileFerdiMeslek
							sqlAileBilgileriGuncelle.save()
						else:
							sqlAileBilgileri = HareketAileBilgileri()
							sqlAileBilgileri.CreateUser            = request.session["KullaniciKodu"]
							sqlAileBilgileri.CreateDate            = timezone.now() 
							sqlAileBilgileri.PersonelKodu          = ajaxPersonel
							sqlAileBilgileri.AileFerdiAdiSoyadi    = ajaxAileFerdiAdSoyad
							sqlAileBilgileri.AileFerdiDogumTarihi  = ajaxAileFerdiDogumTarihi
							sqlAileBilgileri.AileFerdiTuru         = ajaxAileFerdiTuru
							sqlAileBilgileri.AileFerdiTelefon      = ajaxAileFerdiTel
							sqlAileBilgileri.AileFerdiPersonelKodu = ajaxAileFerdiPersonelKodu
							sqlAileBilgileri.Calisiyor             = ajaxAileFerdiCalisiyor
							sqlAileBilgileri.Meslek                = ajaxAileFerdiMeslek
							sqlAileBilgileri.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "vizeler"):	
						ajaxVizeKodu            = request.POST.get("ajaxVizeKodu")
						ajaxVizeUlke            = request.POST.get("ajaxVizeUlke")
						ajaxVizeBelgeNo         = request.POST.get("ajaxVizeBelgeNo")
						ajaxVizeBaslangicTarihi = request.POST.get("ajaxVizeBaslangicTarihi")
						ajaxVizeBitisTarihi     = request.POST.get("ajaxVizeBitisTarihi")
						if(ajaxArguman2 == "1"):
							sqlVizelerGuncelle = get_object_or_404(HareketVizeler,id=ajaxArguman3)
							sqlVizelerGuncelle.LastUpUser          = request.session["KullaniciKodu"]
							sqlVizelerGuncelle.LastUpDate          = timezone.now() 
							sqlVizelerGuncelle.PersonelKodu        = ajaxPersonel
							sqlVizelerGuncelle.VizeKodu            = ajaxVizeKodu
							sqlVizelerGuncelle.VizeUlkeBolge       = ajaxVizeUlke
							sqlVizelerGuncelle.VizeBelgeNo         = ajaxVizeBelgeNo
							sqlVizelerGuncelle.VizeBaslangicTarihi = ajaxVizeBaslangicTarihi
							sqlVizelerGuncelle.VizeBitisTarihi     = ajaxVizeBitisTarihi
							sqlVizelerGuncelle.save()
						else:	
							sqlVizeler = HareketVizeler()
							sqlVizeler.CreateUser          = request.session["KullaniciKodu"]
							sqlVizeler.CreateDate          = timezone.now()
							sqlVizeler.PersonelKodu        = ajaxPersonel
							sqlVizeler.VizeKodu            = ajaxVizeKodu
							sqlVizeler.VizeUlkeBolge       = ajaxVizeUlke
							sqlVizeler.VizeBelgeNo         = ajaxVizeBelgeNo
							sqlVizeler.VizeBaslangicTarihi = ajaxVizeBaslangicTarihi
							sqlVizeler.VizeBitisTarihi     = ajaxVizeBitisTarihi
							sqlVizeler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "dernekler"):
						ajaxDernekAdi            = request.POST.get("ajaxDernekAdi")
						ajaxDernekFaaliyetDetayi = request.POST.get("ajaxDernekFaaliyetDetayi")
						ajaxUyeNo                = request.POST.get("ajaxUyeNo")
						ajaxUyePozisyon          = request.POST.get("ajaxUyePozisyon")
						ajaxUyelikTarihi         = request.POST.get("ajaxUyelikTarihi")
						if(ajaxArguman2 == "1"):
							sqlDerneklerGuncelle = get_object_or_404(HareketDernekler,id=ajaxArguman3)
							sqlDerneklerGuncelle.LastUpUser           = request.session["KullaniciKodu"]
							sqlDerneklerGuncelle.LastUpDate           = timezone.now() 
							sqlDerneklerGuncelle.PersonelKodu         = ajaxPersonel
							sqlDerneklerGuncelle.DernekAdi            = ajaxDernekAdi
							sqlDerneklerGuncelle.DernekFaaliyetDetayi = ajaxDernekFaaliyetDetayi
							sqlDerneklerGuncelle.UyeNo                = ajaxUyeNo
							sqlDerneklerGuncelle.UyePozisyon          = ajaxUyePozisyon
							sqlDerneklerGuncelle.UyelikTarihi         = ajaxUyelikTarihi
							sqlDerneklerGuncelle.save()
						else:
							sqlDernekler = HareketDernekler()
							sqlDernekler.CreateUser           = request.session["KullaniciKodu"]
							sqlDernekler.CreateDate           = timezone.now() 
							sqlDernekler.PersonelKodu         = ajaxPersonel
							sqlDernekler.DernekAdi            = ajaxDernekAdi
							sqlDernekler.DernekFaaliyetDetayi = ajaxDernekFaaliyetDetayi
							sqlDernekler.UyeNo                = ajaxUyeNo
							sqlDernekler.UyePozisyon          = ajaxUyePozisyon
							sqlDernekler.UyelikTarihi         = ajaxUyelikTarihi
							sqlDernekler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "hukumlulukler"):
						ajaxCezaviTuru            = request.POST.get("ajaxCezaviTuru")
						ajaxCezaeviTipi	          = request.POST.get("ajaxCezaeviTipi")
						ajaxIsnadEdilenFiil       = request.POST.get("ajaxIsnadEdilenFiil")
						ajaxIsnadEdilenFiilDetayi = request.POST.get("ajaxIsnadEdilenFiilDetayi")
						ajaxHapisSuresi           = request.POST.get("ajaxHapisSuresi")
						ajaxHapisBaslangicTarihi  = request.POST.get("ajaxHapisBaslangicTarihi")
						ajaxHapisBitisTarihi      = request.POST.get("ajaxHapisBitisTarihi")
						ajaxTamamlananHapisSuresi = request.POST.get("ajaxTamamlananHapisSuresi")
						if(ajaxArguman2 == "1"):
							sqlHukumluluklerGuncelle = get_object_or_404(HareketHukumlulukler,id=ajaxArguman3)
							sqlHukumluluklerGuncelle.LastUpUser            = request.session["KullaniciKodu"]
							sqlHukumluluklerGuncelle.LastUpDate            = timezone.now()
							sqlHukumluluklerGuncelle.PersonelKodu          = ajaxPersonel
							sqlHukumluluklerGuncelle.CezaeviTuru           = ajaxCezaviTuru
							sqlHukumluluklerGuncelle.CezaeviTipi           = ajaxCezaeviTipi
							sqlHukumluluklerGuncelle.IsnadEdilenFiil       = ajaxIsnadEdilenFiil
							sqlHukumluluklerGuncelle.IsnadEdilenFiilDetayi = ajaxIsnadEdilenFiilDetayi
							sqlHukumluluklerGuncelle.HapisSuresi           = ajaxHapisSuresi
							sqlHukumluluklerGuncelle.HapishaneBaslangic    = ajaxHapisBaslangicTarihi
							sqlHukumluluklerGuncelle.HapishaneBitis        = ajaxHapisBitisTarihi
							sqlHukumluluklerGuncelle.TamamlananHapisSuresi = ajaxTamamlananHapisSuresi
							sqlHukumluluklerGuncelle.save()
						else:
							sqlHukumlulukler = HareketHukumlulukler()
							sqlHukumlulukler.CreateUser            = request.session["KullaniciKodu"]
							sqlHukumlulukler.CreateDate            = timezone.now() 
							sqlHukumlulukler.PersonelKodu          = ajaxPersonel
							sqlHukumlulukler.CezaeviTuru           = ajaxCezaviTuru
							sqlHukumlulukler.CezaeviTipi           = ajaxCezaeviTipi
							sqlHukumlulukler.IsnadEdilenFiil       = ajaxIsnadEdilenFiil
							sqlHukumlulukler.IsnadEdilenFiilDetayi = ajaxIsnadEdilenFiilDetayi
							sqlHukumlulukler.HapisSuresi           = ajaxHapisSuresi
							sqlHukumlulukler.HapishaneBaslangic    = ajaxHapisBaslangicTarihi
							sqlHukumlulukler.HapishaneBitis        = ajaxHapisBitisTarihi
							sqlHukumlulukler.TamamlananHapisSuresi = ajaxTamamlananHapisSuresi
							sqlHukumlulukler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "meslekler"):	
						ajaxMeslekAdi          = request.POST.get("ajaxMeslekAdi")
						ajaxMeslekDetayi       = request.POST.get("ajaxMeslekDetayi")
						ajaxMeslekTecrubesi    = request.POST.get("ajaxMeslekTecrubesi")
						ajaxOkulKursKodu       = request.POST.get("ajaxOkulKursKodu")
						ajaxBelgeSertifikaKodu = request.POST.get("ajaxBelgeSertifikaKodu")
						if(ajaxArguman2 == "1"):
							sqlMesleklerGuncelle = get_object_or_404(HareketMeslekler,id=ajaxArguman3)
							sqlMesleklerGuncelle.LastUpUser         = request.session["KullaniciKodu"]
							sqlMesleklerGuncelle.LastUpDate         = timezone.now()
							sqlMesleklerGuncelle.PersonelKodu       = ajaxPersonel
							sqlMesleklerGuncelle.MeslekAdi          = ajaxMeslekAdi
							sqlMesleklerGuncelle.MeslekDetayi       = ajaxMeslekDetayi
							sqlMesleklerGuncelle.Tecrubesi          = ajaxMeslekTecrubesi
							sqlMesleklerGuncelle.OkulKursKodu       = ajaxOkulKursKodu
							sqlMesleklerGuncelle.BelgeSertifikaKodu = ajaxBelgeSertifikaKodu
							sqlMesleklerGuncelle.save()
						else:	
							sqlMeslekler = HareketMeslekler()
							sqlMeslekler.CreateUser         = request.session["KullaniciKodu"]
							sqlMeslekler.CreateDate         = timezone.now()
							sqlMeslekler.PersonelKodu       = ajaxPersonel
							sqlMeslekler.MeslekAdi          = ajaxMeslekAdi
							sqlMeslekler.MeslekDetayi       = ajaxMeslekDetayi
							sqlMeslekler.Tecrubesi          = ajaxMeslekTecrubesi
							sqlMeslekler.OkulKursKodu       = ajaxOkulKursKodu
							sqlMeslekler.BelgeSertifikaKodu = ajaxBelgeSertifikaKodu
							sqlMeslekler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "isGecmisi"):
						ajaxSirketAdi                = request.POST.get("ajaxSirketAdi")
						ajaxSirketUlke               = request.POST.get("ajaxSirketUlke")
						ajaxSirketSehir              = request.POST.get("ajaxSirketSehir")
						ajaxSirketTel                = request.POST.get("ajaxSirketTel")
						ajaxCalismaTuru              = request.POST.get("ajaxCalismaTuru")
						ajaxIsGecmisiDepartman       = request.POST.get("ajaxIsGecmisiDepartman")
						ajaxIsGecmisiPozisyon        = request.POST.get("ajaxIsGecmisiPozisyon")
						ajaxIsGecmisiBaslangicTarihi = request.POST.get("ajaxIsGecmisiBaslangicTarihi")
						ajaxIsGecmisiBitisTarihi     = request.POST.get("ajaxIsGecmisiBitisTarihi")
						ajaxAyrilikSebebi            = request.POST.get("ajaxAyrilikSebebi")
						if(ajaxArguman2 == "1"):
							sqlIsGecmisiGuncelle = get_object_or_404(HareketIsGecmisi,id=ajaxArguman3)
							sqlIsGecmisiGuncelle.LastUpUser      = request.session["KullaniciKodu"]
							sqlIsGecmisiGuncelle.LastUpDate      = timezone.now()
							sqlIsGecmisiGuncelle.PersonelKodu    = ajaxPersonel
							sqlIsGecmisiGuncelle.SirketAdi       = ajaxSirketAdi
							sqlIsGecmisiGuncelle.SirketUlke      = ajaxSirketUlke
							sqlIsGecmisiGuncelle.SirketSehir     = ajaxSirketSehir
							sqlIsGecmisiGuncelle.SirketTel       = ajaxSirketTel
							sqlIsGecmisiGuncelle.CalismaTuru     = ajaxCalismaTuru
							sqlIsGecmisiGuncelle.Departman       = ajaxIsGecmisiDepartman
							sqlIsGecmisiGuncelle.Pozisyon        = ajaxIsGecmisiPozisyon
							sqlIsGecmisiGuncelle.BaslangicTarihi = ajaxIsGecmisiBaslangicTarihi
							sqlIsGecmisiGuncelle.BitisTarihi     = ajaxIsGecmisiBitisTarihi
							sqlIsGecmisiGuncelle.AyrilikSebebi   = ajaxAyrilikSebebi
							sqlIsGecmisiGuncelle.save()
						else:	
							sqlIsGecmisi = HareketIsGecmisi()
							sqlIsGecmisi.CreateUser      = request.session["KullaniciKodu"]
							sqlIsGecmisi.CreateDate      = timezone.now()
							sqlIsGecmisi.PersonelKodu    = ajaxPersonel
							sqlIsGecmisi.SirketAdi       = ajaxSirketAdi
							sqlIsGecmisi.SirketUlke      = ajaxSirketUlke
							sqlIsGecmisi.SirketSehir     = ajaxSirketSehir
							sqlIsGecmisi.SirketTel       = ajaxSirketTel
							sqlIsGecmisi.CalismaTuru     = ajaxCalismaTuru
							sqlIsGecmisi.Departman       = ajaxIsGecmisiDepartman
							sqlIsGecmisi.Pozisyon        = ajaxIsGecmisiPozisyon
							sqlIsGecmisi.BaslangicTarihi = ajaxIsGecmisiBaslangicTarihi
							sqlIsGecmisi.BitisTarihi     = ajaxIsGecmisiBitisTarihi
							sqlIsGecmisi.AyrilikSebebi   = ajaxAyrilikSebebi
							sqlIsGecmisi.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "okullarKurslar"):	
						ajaxEgitimKodu              = request.POST.get("ajaxEgitimKodu")
						ajaxOkulKursAdi             = request.POST.get("ajaxOkulKursAdi")
						ajaxOkulKursUlke            = request.POST.get("ajaxOkulKursUlke")
						ajaxOkulKursSehir           = request.POST.get("ajaxOkulKursSehir")
						ajaxBolumAdi                = request.POST.get("ajaxBolumAdi")
						ajaxOkulKursBaslangicTarihi = request.POST.get("ajaxOkulKursBaslangicTarihi")
						ajaxOkulKursBitisTarihi     = request.POST.get("ajaxOkulKursBitisTarihi")
						ajaxOkulKursBelgeAdi        = request.POST.get("ajaxOkulKursBelgeAdi")
						ajaxOkulKursBelgeTuru       = request.POST.get("ajaxOkulKursBelgeTuru")
						ajaxOkulKursBelgeTarihi     = request.POST.get("ajaxOkulKursBelgeTarihi")
						ajaxOkulKursBelgeKaynak     = request.POST.get("ajaxOkulKursBelgeKaynak")
						if(ajaxArguman2 == "1"):
							sqlOkullarKurslarGuncelle = get_object_or_404(HareketOkullarKurslar,id=ajaxArguman3)
							sqlOkullarKurslarGuncelle.LastUpUser      = request.session["KullaniciKodu"]
							sqlOkullarKurslarGuncelle.LastUpDate      = timezone.now()
							sqlOkullarKurslarGuncelle.PersonelKodu    = ajaxPersonel
							sqlOkullarKurslarGuncelle.OkulKursAdi     = ajaxOkulKursAdi
							sqlOkullarKurslarGuncelle.Ulke            = ajaxOkulKursUlke
							sqlOkullarKurslarGuncelle.Sehir           = ajaxOkulKursSehir
							sqlOkullarKurslarGuncelle.BolumAdi        = ajaxBolumAdi
							sqlOkullarKurslarGuncelle.BaslangicTarihi = ajaxOkulKursBaslangicTarihi
							sqlOkullarKurslarGuncelle.BitisTarihi     = ajaxOkulKursBitisTarihi
							sqlOkullarKurslarGuncelle.BelgeAdi        = ajaxOkulKursBelgeAdi
							sqlOkullarKurslarGuncelle.BelgeTuru       = ajaxOkulKursBelgeTuru
							sqlOkullarKurslarGuncelle.BelgeTarihi     = ajaxOkulKursBelgeTarihi
							sqlOkullarKurslarGuncelle.BelgeKaynak     = ajaxOkulKursBelgeKaynak
							sqlOkullarKurslarGuncelle.save()
						else:
							sqlOkullarKurslar = HareketOkullarKurslar()
							sqlOkullarKurslar.CreateUser      = request.session["KullaniciKodu"]
							sqlOkullarKurslar.CreateDate      = timezone.now()
							sqlOkullarKurslar.PersonelKodu    = ajaxPersonel
							sqlOkullarKurslar.OkulKursAdi     = ajaxOkulKursAdi
							sqlOkullarKurslar.Ulke            = ajaxOkulKursUlke
							sqlOkullarKurslar.Sehir           = ajaxOkulKursSehir
							sqlOkullarKurslar.BolumAdi        = ajaxBolumAdi
							sqlOkullarKurslar.BaslangicTarihi = ajaxOkulKursBaslangicTarihi
							sqlOkullarKurslar.BitisTarihi     = ajaxOkulKursBitisTarihi
							sqlOkullarKurslar.BelgeAdi        = ajaxOkulKursBelgeAdi
							sqlOkullarKurslar.BelgeTuru       = ajaxOkulKursBelgeTuru
							sqlOkullarKurslar.BelgeTarihi     = ajaxOkulKursBelgeTarihi
							sqlOkullarKurslar.BelgeKaynak     = ajaxOkulKursBelgeKaynak
							sqlOkullarKurslar.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "nitelikler"):	
						ajaxNitelikKodu      = request.POST.get("ajaxNitelikKodu")
						ajaxNitelikTecrubesi = request.POST.get("ajaxNitelikTecrubesi")
						ajaxNitelikSeviyesi  = request.POST.get("ajaxNitelikSeviyesi")
						if(ajaxArguman2 == "1"):
							sqlNiteliklerGuncelle = get_object_or_404(HareketNitelikler,id=ajaxArguman3)
							sqlNiteliklerGuncelle.LastUpUser       = request.session["KullaniciKodu"]
							sqlNiteliklerGuncelle.LastUpDate       = timezone.now()
							sqlNiteliklerGuncelle.PersonelKodu     = ajaxPersonel
							sqlNiteliklerGuncelle.NitelikKodu      = ajaxNitelikKodu
							sqlNiteliklerGuncelle.NitelikTecrubesi = ajaxNitelikTecrubesi
							sqlNiteliklerGuncelle.NitelikSeviyesi  = ajaxNitelikSeviyesi
							sqlNiteliklerGuncelle.save()
						else:
							sqlNitelikler = HareketNitelikler()
							sqlNitelikler.CreateUser       = request.session["KullaniciKodu"]
							sqlNitelikler.CreateDate       = timezone.now()
							sqlNitelikler.PersonelKodu     = ajaxPersonel
							sqlNitelikler.NitelikKodu      = ajaxNitelikKodu
							sqlNitelikler.NitelikTecrubesi = ajaxNitelikTecrubesi
							sqlNitelikler.NitelikSeviyesi  = ajaxNitelikSeviyesi
							sqlNitelikler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "diller"):	
						ajaxDilKodu                  = request.POST.get("ajaxDilKodu")
						ajaxOgrenimTuru              = request.POST.get("ajaxOgrenimTuru")
						ajaxOkumaSeviyesi            = request.POST.get("ajaxOkumaSeviyesi")
						ajaxYazmaSeviyesi            = request.POST.get("ajaxYazmaSeviyesi")
						ajaxKonusmaSeviyesi          = request.POST.get("ajaxKonusmaSeviyesi")
						ajaxDillerOkulKursKodu       = request.POST.get("ajaxDillerOkulKursKodu")
						ajaxDillerBelgeSertifikaKodu = request.POST.get("ajaxDillerBelgeSertifikaKodu")
						if(ajaxArguman2 == "1"):
							sqlDillerGuncelle = get_object_or_404(HareketDiller,id=ajaxArguman3)
							sqlDillerGuncelle.LastUpUser         = request.session["KullaniciKodu"]
							sqlDillerGuncelle.LastUpDate         = timezone.now()
							sqlDillerGuncelle.PersonelKodu       = ajaxPersonel
							sqlDillerGuncelle.DilKodu            = ajaxDilKodu
							sqlDillerGuncelle.OgrenimTuru        = ajaxOgrenimTuru
							sqlDillerGuncelle.OkumaSeviyesi      = ajaxOkumaSeviyesi
							sqlDillerGuncelle.YazmaSeviyesi      = ajaxYazmaSeviyesi
							sqlDillerGuncelle.KonusmaSeviyesi    = ajaxKonusmaSeviyesi
							sqlDillerGuncelle.OkulKursKodu       = ajaxDillerOkulKursKodu
							sqlDillerGuncelle.BelgeSertifikaKodu = ajaxDillerBelgeSertifikaKodu
							sqlDillerGuncelle.save()
						else:
							sqlDiller = HareketDiller()
							sqlDiller.CreateUser         = request.session["KullaniciKodu"]
							sqlDiller.CreateDate         = timezone.now()
							sqlDiller.PersonelKodu       = ajaxPersonel
							sqlDiller.DilKodu            = ajaxDilKodu
							sqlDiller.OgrenimTuru        = ajaxOgrenimTuru
							sqlDiller.OkumaSeviyesi      = ajaxOkumaSeviyesi
							sqlDiller.YazmaSeviyesi      = ajaxYazmaSeviyesi
							sqlDiller.KonusmaSeviyesi    = ajaxKonusmaSeviyesi
							sqlDiller.OkulKursKodu       = ajaxDillerOkulKursKodu
							sqlDiller.BelgeSertifikaKodu = ajaxDillerBelgeSertifikaKodu
							sqlDiller.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)	
					if(ajaxArguman == "fazlaMesailer"):
						ajaxFazlaMesaiTuru          = request.POST.get("ajaxFazlaMesaiTuru")
						ajaxFazlaMesaiTarihi        = request.POST.get("ajaxFazlaMesaiTarihi")
						ajaxFazlaMesaiSaatAraligi1  = request.POST.get("ajaxFazlaMesaiSaatAraligi1")
						ajaxFazlaMesaiSaatAraligi2  = request.POST.get("ajaxFazlaMesaiSaatAraligi2")
						ajaxFazlaMesaiSaati         = request.POST.get("ajaxFazlaMesaiSaati")
						ajaxFazlaMesaiArttirimOrani = request.POST.get("ajaxFazlaMesaiArttirimOrani")
						ajaxFazlaMesaiUcreti        = request.POST.get("ajaxFazlaMesaiUcreti")
						replaceFazlaMesaiUcreti     = ajaxFazlaMesaiUcreti.replace(",",".")
						
						if(ajaxArguman2 == "1"):
							sqlFazlaMesailerGuncelle = get_object_or_404(HareketFazlaMesailer,id=ajaxArguman3)
							sqlFazlaMesailerGuncelle.LastUpUser    = request.session["KullaniciKodu"]
							sqlFazlaMesailerGuncelle.LastUpDate    = timezone.now()
							sqlFazlaMesailerGuncelle.PersonelKodu  = ajaxPersonel
							sqlFazlaMesailerGuncelle.MesaiTuru     = ajaxFazlaMesaiTuru
							sqlFazlaMesailerGuncelle.MesaiTarihi   = ajaxFazlaMesaiTarihi
							sqlFazlaMesailerGuncelle.SaatAraligi1  = ajaxFazlaMesaiSaatAraligi1
							sqlFazlaMesailerGuncelle.SaatAraligi2  = ajaxFazlaMesaiSaatAraligi2
							sqlFazlaMesailerGuncelle.Saati         = float(ajaxFazlaMesaiSaati)
							sqlFazlaMesailerGuncelle.ArttirimOrani = float(ajaxFazlaMesaiArttirimOrani)
							sqlFazlaMesailerGuncelle.MesaiUcreti   = float(ajaxFazlaMesaiUcreti)
							sqlFazlaMesailerGuncelle.save()
						else:	
							sqlFazlaMesailer = HareketFazlaMesailer()
							sqlFazlaMesailer.CreateUser    = request.session["KullaniciKodu"]
							sqlFazlaMesailer.CreateDate    = timezone.now()
							sqlFazlaMesailer.PersonelKodu  = ajaxPersonel
							sqlFazlaMesailer.MesaiTuru     = ajaxFazlaMesaiTuru
							sqlFazlaMesailer.MesaiTarihi   = ajaxFazlaMesaiTarihi
							sqlFazlaMesailer.SaatAraligi1  = ajaxFazlaMesaiSaatAraligi1
							sqlFazlaMesailer.SaatAraligi2  = ajaxFazlaMesaiSaatAraligi2
							sqlFazlaMesailer.Saati         = float(ajaxFazlaMesaiSaati)
							sqlFazlaMesailer.ArttirimOrani = float(ajaxFazlaMesaiArttirimOrani)
							sqlFazlaMesailer.MesaiUcreti   = float(ajaxFazlaMesaiUcreti)
							sqlFazlaMesailer.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "gorevler"):	
						ajaxGorevKodu             = request.POST.get("ajaxGorevKodu")
						ajaxGorevlerDepartmanKodu = request.POST.get("ajaxGorevlerDepartmanKodu")
						ajaxGorevAmirKodu         = request.POST.get("ajaxGorevAmirKodu")
						ajaxGorevBaslangicTarihi  = request.POST.get("ajaxGorevBaslangicTarihi")
						ajaxGorevBitisTarihi      = request.POST.get("ajaxGorevBitisTarihi")
						ajaxGorevSonuc            = request.POST.get("ajaxGorevSonuc")
						ajaxGorevSonucDetayi      = request.POST.get("ajaxGorevSonucDetayi")
						if(ajaxArguman2 == "1"):
							sqlGorevlerGuncelle = get_object_or_404(HareketGorevler,id=ajaxArguman3)
							sqlGorevlerGuncelle.LastUpUser       = request.session["KullaniciKodu"]
							sqlGorevlerGuncelle.LastUpDate       = timezone.now()
							sqlGorevlerGuncelle.PersonelKodu     = ajaxPersonel
							sqlGorevlerGuncelle.GorevKodu        = ajaxGorevKodu
							sqlGorevlerGuncelle.DepartmanKodu    = ajaxGorevlerDepartmanKodu
							sqlGorevlerGuncelle.GorevAmiriKodu   = ajaxGorevAmirKodu
							sqlGorevlerGuncelle.BaslangicTarihi  = ajaxGorevBaslangicTarihi
							sqlGorevlerGuncelle.BitisTarihi      = ajaxGorevBitisTarihi
							sqlGorevlerGuncelle.GorevSonuc       = ajaxGorevSonuc
							sqlGorevlerGuncelle.GorevSonucDetayi = ajaxGorevSonucDetayi
							sqlGorevlerGuncelle.save()
						else:
							sqlGorevler = HareketGorevler()
							sqlGorevler.CreateUser       = request.session["KullaniciKodu"]
							sqlGorevler.CreateDate       = timezone.now()
							sqlGorevler.PersonelKodu     = ajaxPersonel
							sqlGorevler.GorevKodu        = ajaxGorevKodu
							sqlGorevler.DepartmanKodu    = ajaxGorevlerDepartmanKodu
							sqlGorevler.GorevAmiriKodu   = ajaxGorevAmirKodu
							sqlGorevler.BaslangicTarihi  = ajaxGorevBaslangicTarihi
							sqlGorevler.BitisTarihi      = ajaxGorevBitisTarihi
							sqlGorevler.GorevSonuc       = ajaxGorevSonuc
							sqlGorevler.GorevSonucDetayi = ajaxGorevSonucDetayi
							sqlGorevler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "performanslar"):	
						ajaxPerformansKodu             = request.POST.get("ajaxPerformansKodu")
						ajaxPerformanDegerlendirenKodu = request.POST.get("ajaxPerformanDegerlendirenKodu")
						ajaxPerformansPeriyodu         = request.POST.get("ajaxPerformansPeriyodu")
						ajaxDegerlendirmePuani         = request.POST.get("ajaxDegerlendirmePuani")
						ajaxDegerlendirmePuaniDetayi   = request.POST.get("ajaxDegerlendirmePuaniDetayi")
						if(ajaxArguman2 == "1"):
							sqlPerformanslarGuncelle = get_object_or_404(HareketPerformanslar,id=ajaxArguman3)
							sqlPerformanslarGuncelle.LastUpUser               = request.session["KullaniciKodu"]
							sqlPerformanslarGuncelle.LastUpDate               = timezone.now()
							sqlPerformanslarGuncelle.PersonelKodu             = ajaxPersonel
							sqlPerformanslarGuncelle.PerformansKodu           = ajaxPerformansKodu
							sqlPerformanslarGuncelle.DegerlendirmeyiYapan     = ajaxPerformanDegerlendirenKodu
							sqlPerformanslarGuncelle.PerformansPeriyodu       = ajaxPerformansPeriyodu
							sqlPerformanslarGuncelle.DegerlendirmePuani       = ajaxDegerlendirmePuani
							sqlPerformanslarGuncelle.DegerlendirmePuaniDetayi = ajaxDegerlendirmePuaniDetayi
							sqlPerformanslarGuncelle.save()
						else:
							sqlPerformanslar = HareketPerformanslar()
							sqlPerformanslar.CreateUser               = request.session["KullaniciKodu"]
							sqlPerformanslar.CreateDate               = timezone.now()
							sqlPerformanslar.PersonelKodu             = ajaxPersonel
							sqlPerformanslar.PerformansKodu           = ajaxPerformansKodu
							sqlPerformanslar.DegerlendirmeyiYapan     = ajaxPerformanDegerlendirenKodu
							sqlPerformanslar.PerformansPeriyodu       = ajaxPerformansPeriyodu
							sqlPerformanslar.DegerlendirmePuani       = ajaxDegerlendirmePuani
							sqlPerformanslar.DegerlendirmePuaniDetayi = ajaxDegerlendirmePuaniDetayi
							sqlPerformanslar.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "yardimlar"):
						ajaxYardimKodu            = request.POST.get("ajaxYardimKodu")
						ajaxYardimTarihi          = request.POST.get("ajaxYardimTarihi")
						ajaxYardimlarMuhİslemKodu = request.POST.get("ajaxYardimlarMuhİslemKodu")
						if(ajaxArguman2 == "1"):
							sqlYardimlarGuncelle = get_object_or_404(HareketYardimlar,id=ajaxArguman3)
							sqlYardimlarGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlYardimlarGuncelle.LastUpDate        = timezone.now()
							sqlYardimlarGuncelle.PersonelKodu      = ajaxPersonel
							sqlYardimlarGuncelle.YardimKodu        = ajaxYardimKodu
							sqlYardimlarGuncelle.YardimTarihi      = ajaxYardimTarihi
							sqlYardimlarGuncelle.MuhasebeIslemKodu = ajaxYardimlarMuhİslemKodu
							sqlYardimlarGuncelle.save()
						else:
							sqlYardimlar = HareketYardimlar()
							sqlYardimlar.CreateUser        = request.session["KullaniciKodu"]
							sqlYardimlar.CreateDate        = timezone.now()
							sqlYardimlar.PersonelKodu      = ajaxPersonel
							sqlYardimlar.YardimKodu        = ajaxYardimKodu
							sqlYardimlar.YardimTarihi      = ajaxYardimTarihi
							sqlYardimlar.MuhasebeIslemKodu = ajaxYardimlarMuhİslemKodu
							sqlYardimlar.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "izinler"):	
						ajaxIzinTuru            = request.POST.get("ajaxIzinTuru")
						ajaxIzinSebebi          = request.POST.get("ajaxIzinSebebi")
						ajaxIzinBaslangicTarihi = request.POST.get("ajaxIzinBaslangicTarihi")
						ajaxIzinBitisTarihi     = request.POST.get("ajaxIzinBitisTarihi")
						ajaxIzinlerMuhIslemKodu = request.POST.get("ajaxIzinlerMuhIslemKodu")
						if(ajaxArguman2 == "1"):
							sqlIzinlerGuncelle = get_object_or_404(HareketIzinler,id=ajaxArguman3)
							sqlIzinlerGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlIzinlerGuncelle.LastUpDate        = timezone.now()
							sqlIzinlerGuncelle.PersonelKodu      = ajaxPersonel
							sqlIzinlerGuncelle.IzinTuru          = ajaxIzinTuru
							sqlIzinlerGuncelle.IzinSebebi        = ajaxIzinSebebi
							sqlIzinlerGuncelle.BaslangicTarihi   = ajaxIzinBaslangicTarihi
							sqlIzinlerGuncelle.BitisTarihi       = ajaxIzinBitisTarihi
							sqlIzinlerGuncelle.MuhasebeIslemKodu = ajaxIzinlerMuhIslemKodu
							sqlIzinlerGuncelle.save()
						else:
							sqlIzinler = HareketIzinler()
							sqlIzinler.CreateUser        = request.session["KullaniciKodu"]
							sqlIzinler.CreateDate        = timezone.now()
							sqlIzinler.PersonelKodu      = ajaxPersonel
							sqlIzinler.IzinTuru          = ajaxIzinTuru
							sqlIzinler.IzinSebebi        = ajaxIzinSebebi
							sqlIzinler.BaslangicTarihi   = ajaxIzinBaslangicTarihi
							sqlIzinler.BitisTarihi       = ajaxIzinBitisTarihi
							sqlIzinler.MuhasebeIslemKodu = ajaxIzinlerMuhIslemKodu
							sqlIzinler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "avanslar"):
						ajaxAvansTuru            = request.POST.get("ajaxAvansTuru")
						ajaxAvansSebebi          = request.POST.get("ajaxAvansSebebi")
						ajaxAvansMiktari         = request.POST.get("ajaxAvansMiktari")
						ajaxAvansTarihi          = request.POST.get("ajaxAvansTarihi")
						ajaxAvanslarMuhIslemKodu = request.POST.get("ajaxAvanslarMuhIslemKodu")
						replaceAvansMiktari = ajaxAvansMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlAvanslarGuncelle = get_object_or_404(HareketlerAvanslar,id=ajaxArguman3)
							sqlAvanslarGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlAvanslarGuncelle.LastUpDate        = timezone.now()
							sqlAvanslarGuncelle.PersonelKodu      = ajaxPersonel
							sqlAvanslarGuncelle.AvansTuru         = ajaxAvansTuru
							sqlAvanslarGuncelle.AvansSebebi       = ajaxAvansSebebi
							sqlAvanslarGuncelle.AvansMiktari      = float(replaceAvansMiktari)
							sqlAvanslarGuncelle.AvansTarihi       = ajaxAvansTarihi
							sqlAvanslarGuncelle.MuhasebeIslemKodu = ajaxAvanslarMuhIslemKodu
							sqlAvanslarGuncelle.save()
						else:
							sqlAvanslar = HareketlerAvanslar()
							sqlAvanslar.CreateUser        = request.session["KullaniciKodu"]
							sqlAvanslar.CreateDate        = timezone.now()
							sqlAvanslar.PersonelKodu      = ajaxPersonel
							sqlAvanslar.AvansTuru         = ajaxAvansTuru
							sqlAvanslar.AvansSebebi       = ajaxAvansSebebi
							sqlAvanslar.AvansMiktari      = float(replaceAvansMiktari)
							sqlAvanslar.AvansTarihi       = ajaxAvansTarihi
							sqlAvanslar.MuhasebeIslemKodu = ajaxAvanslarMuhIslemKodu
							sqlAvanslar.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "primler"):
						ajaxPrimTuru            = request.POST.get("ajaxPrimTuru")
						ajaxPrimSebebi          = request.POST.get("ajaxPrimSebebi")
						ajaxPrimMiktari         = request.POST.get("ajaxPrimMiktari")
						ajaxPrimTarihi          = request.POST.get("ajaxPrimTarihi")
						ajaxPrimlerMuhIslemKodu = request.POST.get("ajaxPrimlerMuhIslemKodu")
						replacePrimMiktari      = ajaxPrimMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlPrimlerGuncelle = get_object_or_404(HareketPrimler,id=ajaxArguman3)
							sqlPrimlerGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlPrimlerGuncelle.LastUpDate        = timezone.now()
							sqlPrimlerGuncelle.PersonelKodu      = ajaxPersonel
							sqlPrimlerGuncelle.PrimTuru          = ajaxPrimTuru
							sqlPrimlerGuncelle.PrimSebebi        = ajaxPrimSebebi
							sqlPrimlerGuncelle.PrimMiktari       = float(replacePrimMiktari)
							sqlPrimlerGuncelle.PrimTarihi        = ajaxPrimTarihi
							sqlPrimlerGuncelle.MuhasebeIslemKodu = ajaxPrimlerMuhIslemKodu
							sqlPrimlerGuncelle.save()
						else:
							sqlPrimler = HareketPrimler()
							sqlPrimler.CreateUser        = request.session["KullaniciKodu"]
							sqlPrimler.CreateDate        = timezone.now()
							sqlPrimler.PersonelKodu      = ajaxPersonel
							sqlPrimler.PrimTuru          = ajaxPrimTuru
							sqlPrimler.PrimSebebi        = ajaxPrimSebebi
							sqlPrimler.PrimMiktari       = float(replacePrimMiktari)
							sqlPrimler.PrimTarihi        = ajaxPrimTarihi
							sqlPrimler.MuhasebeIslemKodu = ajaxPrimlerMuhIslemKodu
							sqlPrimler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "tahakkuklar"):
						ajaxTahakkukTuru            = request.POST.get("ajaxTahakkukTuru")
						ajaxTahakkukSebebi          = request.POST.get("ajaxTahakkukSebebi")
						ajaxTahakkukMiktari         = request.POST.get("ajaxTahakkukMiktari")
						ajaxTahakkukTarihi          = request.POST.get("ajaxTahakkukTarihi")
						ajaxTahakkukPeriyodu        = request.POST.get("ajaxTahakkukPeriyodu")
						ajaxTahakkuklarMuhIslemKodu = request.POST.get("ajaxTahakkuklarMuhIslemKodu")
						replaceTahakkukMiktari      = ajaxTahakkukMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlTahakkuklarGuncelle = get_object_or_404(HareketTahakkuklar,id=ajaxArguman3)
							sqlTahakkuklarGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlTahakkuklarGuncelle.LastUpDate        = timezone.now()
							sqlTahakkuklarGuncelle.PersonelKodu      = ajaxPersonel
							sqlTahakkuklarGuncelle.TahakkukTuru      = ajaxTahakkukTuru
							sqlTahakkuklarGuncelle.TahakkukSebebi    = ajaxTahakkukSebebi
							sqlTahakkuklarGuncelle.TahakkukMiktari   = float(replaceTahakkukMiktari)
							sqlTahakkuklarGuncelle.TahakkukTarihi    = ajaxTahakkukTarihi
							sqlTahakkuklarGuncelle.TahakkukPeriyodu  = ajaxTahakkukPeriyodu
							sqlTahakkuklarGuncelle.MuhasebeIslemKodu = ajaxTahakkuklarMuhIslemKodu
							sqlTahakkuklarGuncelle.save()
						else:
							sqlTahakkuklar  = HareketTahakkuklar()
							sqlTahakkuklar.CreateUser        = request.session["KullaniciKodu"]
							sqlTahakkuklar.CreateDate        = timezone.now()
							sqlTahakkuklar.PersonelKodu      = ajaxPersonel
							sqlTahakkuklar.TahakkukTuru      = ajaxTahakkukTuru
							sqlTahakkuklar.TahakkukSebebi    = ajaxTahakkukSebebi
							sqlTahakkuklar.TahakkukMiktari   = float(replaceTahakkukMiktari)
							sqlTahakkuklar.TahakkukTarihi    = ajaxTahakkukTarihi
							sqlTahakkuklar.TahakkukPeriyodu  = ajaxTahakkukPeriyodu
							sqlTahakkuklar.MuhasebeIslemKodu = ajaxTahakkuklarMuhIslemKodu
							sqlTahakkuklar.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "ikramiyeler"):
						ajaxIkramiyeTuru            = request.POST.get("ajaxIkramiyeTuru")
						ajaxIkramiyeSebebi          = request.POST.get("ajaxIkramiyeSebebi")
						ajaxIkramiyeMiktari         = request.POST.get("ajaxIkramiyeMiktari")
						ajaxIkramiyeTarihi          = request.POST.get("ajaxIkramiyeTarihi")
						ajaxIkramiyelerMuhIslemKodu = request.POST.get("ajaxIkramiyelerMuhIslemKodu")
						replaceIkramiyeMiktari      = ajaxIkramiyeMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlIkramiyelerGuncelle = get_object_or_404(HareketlerIkramiyeler,id=ajaxArguman3)
							sqlIkramiyelerGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlIkramiyelerGuncelle.LastUpDate        = timezone.now() 
							sqlIkramiyelerGuncelle.PersonelKodu      = ajaxPersonel
							sqlIkramiyelerGuncelle.IkramiyeTuru      = ajaxIkramiyeTuru
							sqlIkramiyelerGuncelle.IkramiyeSebebi    = ajaxIkramiyeSebebi
							sqlIkramiyelerGuncelle.IkramiyeMiktari   = float(replaceIkramiyeMiktari)
							sqlIkramiyelerGuncelle.IkramiyeTarihi    = ajaxIkramiyeTarihi
							sqlIkramiyelerGuncelle.MuhasebeIslemKodu = ajaxIkramiyelerMuhIslemKodu
							sqlIkramiyelerGuncelle.save()
						else:
							sqlIkramiyeler  = HareketlerIkramiyeler()
							sqlIkramiyeler.CreateUser        = request.session["KullaniciKodu"]
							sqlIkramiyeler.CreateDate        = timezone.now()
							sqlIkramiyeler.PersonelKodu      = ajaxPersonel
							sqlIkramiyeler.IkramiyeTuru      = ajaxIkramiyeTuru
							sqlIkramiyeler.IkramiyeSebebi    = ajaxIkramiyeSebebi
							sqlIkramiyeler.IkramiyeMiktari   = float(replaceIkramiyeMiktari)
							sqlIkramiyeler.IkramiyeTarihi    = ajaxIkramiyeTarihi
							sqlIkramiyeler.MuhasebeIslemKodu = ajaxIkramiyelerMuhIslemKodu
							sqlIkramiyeler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					if(ajaxArguman == "kesintiler"):
						ajaxKesintiTuru         = request.POST.get("ajaxKesintiTuru")
						ajaxKesintiSebebi       = request.POST.get("ajaxKesintiSebebi")
						ajaxKesintiMiktari      = request.POST.get("ajaxKesintiMiktari")
						ajaxKesintiTarihi       = request.POST.get("ajaxKesintiTarihi")
						ajaxKesintiMuhIslemKodu = request.POST.get("ajaxKesintiMuhIslemKodu")
						replaceKesintiMiktari   = ajaxKesintiMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlKesintilerGuncelle = get_object_or_404(HareketKesintiler,id=ajaxArguman3)
							sqlKesintilerGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlKesintilerGuncelle.LastUpDate        = timezone.now()
							sqlKesintilerGuncelle.PersonelKodu      = ajaxPersonel
							sqlKesintilerGuncelle.KesintiTuru       = ajaxKesintiTuru
							sqlKesintilerGuncelle.KesintiSebebi     = ajaxKesintiSebebi
							sqlKesintilerGuncelle.KesintiMiktari    = float(replaceKesintiMiktari)
							sqlKesintilerGuncelle.KesintiTarihi     = ajaxKesintiTarihi
							sqlKesintilerGuncelle.MuhasebeIslemKodu = ajaxKesintiMuhIslemKodu
							sqlKesintilerGuncelle.save()
						else:	
							sqlKesintiler  = HareketKesintiler()
							sqlKesintiler.CreateUser        = request.session["KullaniciKodu"]
							sqlKesintiler.CreateDate        = timezone.now()
							sqlKesintiler.PersonelKodu      = ajaxPersonel
							sqlKesintiler.KesintiTuru       = ajaxKesintiTuru
							sqlKesintiler.KesintiSebebi     = ajaxKesintiSebebi
							sqlKesintiler.KesintiMiktari    = float(replaceKesintiMiktari)
							sqlKesintiler.KesintiTarihi     = ajaxKesintiTarihi
							sqlKesintiler.MuhasebeIslemKodu = ajaxKesintiMuhIslemKodu
							sqlKesintiler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)

					if(ajaxArguman == "zimmetler"):
						ajaxKategori           = request.POST.get("ajaxKategori")
						ajaxZimmetBasTarihi    = request.POST.get("ajaxZimmetBasTarihi")
						ajaxZimmetBitisTarihi  = request.POST.get("ajaxZimmetBitisTarihi")
						ajaxZimmetAlanKisi     = request.POST.get("ajaxZimmetAlanKisi")
						ajaxZimmetVerenKisi    = request.POST.get("ajaxZimmetVerenKisi")
						ajaxZimmetMiktari      = request.POST.get("ajaxZimmetMiktari")
						ajaxZimmetMarka        = request.POST.get("ajaxZimmetMarka")
						ajaxZimmetModel        = request.POST.get("ajaxZimmetModel")
						ajaxAciklama1          = request.POST.get("ajaxAciklama1")
						ajaxAciklama2          = request.POST.get("ajaxAciklama2")
						ajaxAciklama3          = request.POST.get("ajaxAciklama3")
						ajaxZimmetMuhIslemKodu = request.POST.get("ajaxZimmetMuhIslemKodu")
						replaceZimmetMiktari   = ajaxZimmetMiktari.replace(",",".")
						if(ajaxArguman2 == "1"):
							sqlZimmetlerGuncelle = get_object_or_404(HareketZimmetler,id=ajaxArguman3)
							sqlZimmetlerGuncelle.LastUpUser        = request.session["KullaniciKodu"]
							sqlZimmetlerGuncelle.LastUpDate        = timezone.now()
							sqlZimmetlerGuncelle.PersonelKodu      = ajaxPersonel
							sqlZimmetlerGuncelle.Kategori          = ajaxKategori
							sqlZimmetlerGuncelle.BaslangicTarihi   = ajaxZimmetBasTarihi
							sqlZimmetlerGuncelle.BitisTarihi       = ajaxZimmetBitisTarihi
							sqlZimmetlerGuncelle.AlanKisi          = ajaxZimmetAlanKisi
							sqlZimmetlerGuncelle.VerenKisi         = ajaxZimmetVerenKisi
							sqlZimmetlerGuncelle.Miktar            = float(replaceZimmetMiktari)
							sqlZimmetlerGuncelle.Marka             = ajaxZimmetMarka
							sqlZimmetlerGuncelle.Model             = ajaxZimmetModel
							sqlZimmetlerGuncelle.Aciklama1         = ajaxAciklama1
							sqlZimmetlerGuncelle.Aciklama2         = ajaxAciklama2
							sqlZimmetlerGuncelle.Aciklama3         = ajaxAciklama3
							sqlZimmetlerGuncelle.MuhasebeIslemKodu = ajaxZimmetMuhIslemKodu
							sqlZimmetlerGuncelle.save()
						else:	
							sqlZimmetler  = HareketZimmetler()
							sqlZimmetler.CreateUser        = request.session["KullaniciKodu"]
							sqlZimmetler.CreateDate        = timezone.now()
							sqlZimmetler.PersonelKodu      = ajaxPersonel
							sqlZimmetler.Kategori          = ajaxKategori
							sqlZimmetler.BaslangicTarihi   = ajaxZimmetBasTarihi
							sqlZimmetler.BitisTarihi       = ajaxZimmetBitisTarihi
							sqlZimmetler.AlanKisi          = ajaxZimmetAlanKisi
							sqlZimmetler.VerenKisi         = ajaxZimmetVerenKisi
							sqlZimmetler.Miktar            = float(replaceZimmetMiktari)
							sqlZimmetler.Marka             = ajaxZimmetMarka
							sqlZimmetler.Model             = ajaxZimmetModel
							sqlZimmetler.Aciklama1         = ajaxAciklama1
							sqlZimmetler.Aciklama2         = ajaxAciklama2
							sqlZimmetler.Aciklama3         = ajaxAciklama3
							sqlZimmetler.MuhasebeIslemKodu = ajaxZimmetMuhIslemKodu
							sqlZimmetler.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)

					ajaxFzlMsArtOr = request.POST.get("ajaxFzlMsArtOr")	
					ajaxFzlMsSaati = request.POST.get("ajaxFzlMsSaati")
					ajaxFzlPers    = request.POST.get("ajaxFzlPers")
					if(ajaxFzlMsArtOr != None):
						sqlPersonel         = get_object_or_404(Personel,Kodu=ajaxFzlPers, IsDeleted=False)
						sqlMaasTipi         = get_object_or_404(TanimlamaMaasTipleri,Kodu=sqlPersonel.UcretTipi)
						brutTutar           = float(sqlMaasTipi.Deger)
						sgkIsciKes          = float(brutTutar) * 0.14 #Brüt Ücret İle İsci payı orani 
						sgkIsverenKes       = float(brutTutar) * 0.155 #Brüt Ücret İle İsveren payı orani
						issizlikIsciKes     = float(brutTutar) * 0.01 #Brüt Ücret İle İşsizlik İsci payı orani 
						issizlikIsverenKes  = float(brutTutar) * 0.02 #Brüt Ücret İle İşsizlik İsveren payı orani
						gelirVergisiMatrahi = float(brutTutar) - (sgkIsciKes + issizlikIsciKes)
						gelirVergisiKes     = gelirVergisiMatrahi * 0.15 #Gelir Vergisi Oranı
						damgaVerKes         = float(brutTutar) * 0.00759  #Damga Vergisi Oranı
						agiHaricNetTutar    = brutTutar - (sgkIsciKes + issizlikIsciKes + gelirVergisiKes + damgaVerKes)
						agiYillikBrut       = float(brutTutar) * 12
						agi = 0
						esi = 0
						cocugu = 0
						try:
							cocukSayisi = 0
							for sqlAileBilgileri in HareketAileBilgileri.objects.filter(PersonelKodu=ajaxFzlPers):
								if(sqlAileBilgileri.AileFerdiTuru == "12"):
									cocukSayisi = int(cocukSayisi) + 1		
							if(sqlPersonel.MedeniHal == "1" and sqlAileBilgileri.AileFerdiTuru == "11" and sqlAileBilgileri.Calisiyor == False):
								esi = 0.10		
							if (sqlAileBilgileri.Calisiyor == False and cocukSayisi == 1):
								cocugu = 0.075
							if (sqlAileBilgileri.Calisiyor == False and cocukSayisi == 2):
								cocugu = 0.15
							if (sqlAileBilgileri.Calisiyor == False and cocukSayisi == 3):
								cocugu = 0.25
							if (sqlAileBilgileri.Calisiyor == True and cocukSayisi == 1):
								cocugu = 0.075
							if (sqlAileBilgileri.Calisiyor == True and cocukSayisi == 2):
								cocugu = 0.15
							if (sqlAileBilgileri.Calisiyor == True and cocukSayisi == 3):
								cocugu = 0.25	
							if (sqlAileBilgileri.Calisiyor == True and cocukSayisi == 4):
								cocugu = 0.30
							if (sqlAileBilgileri.Calisiyor == True and cocukSayisi == 5):
								cocugu = 0.35					
						except:
							pass	
						agi              = agiYillikBrut * (float(ajaxFzlMsArtOr) + esi + cocugu) * 0.15 / 12	
						netTutar         = agiHaricNetTutar + agi
						saatUcreti       = brutTutar / 30 / 7.5
						fazlaMesaiFarki  = saatUcreti * float(ajaxFzlMsArtOr)
						fazlaMesaiUcreti = (saatUcreti + fazlaMesaiFarki) * float(ajaxFzlMsSaati)
						
						context = {"ajaxFazlaMesaiSaatUcreti" : fazlaMesaiUcreti}
						return JsonResponse(context)
					ajaxIlSecim = request.POST.get("ajaxIlSecim")
					if(ajaxIlSecim != None):			
						ilceler = ""
						if(ajaxIlSecim == "Adana"):
							ilceler = Adana
						if(ajaxIlSecim == "Adıyaman"):
							ilceler = Adıyaman
						if(ajaxIlSecim == "Afyonkarahisar"):
							ilceler = Afyonkarahisar
						if(ajaxIlSecim == "Ağrı"):
							ilceler = Ağrı
						if(ajaxIlSecim == "Aksaray"):
							ilceler = Aksaray
						if(ajaxIlSecim == "Amasya"):
							ilceler = Amasya
						if(ajaxIlSecim == "Ankara"):
							ilceler = Ankara
						if(ajaxIlSecim == "Antalya"):
							ilceler = Antalya
						if(ajaxIlSecim == "Ardahan"):
							ilceler = Ardahan
						if(ajaxIlSecim == "Artvin"):
							ilceler = Artvin
						if(ajaxIlSecim == "Aydın"):
							ilceler = Aydın
						if(ajaxIlSecim == "Balıkesir"):
							ilceler = Balıkesir
						if(ajaxIlSecim == "Bartın"):
							ilceler = Bartın
						if(ajaxIlSecim == "Batman"):
							ilceler = Batman
						if(ajaxIlSecim == "Bayburt"):
							ilceler = Bayburt
						if(ajaxIlSecim == "Bilecik"):
							ilceler = Bilecik
						if(ajaxIlSecim == "Bingöl"):
							ilceler = Bingöl
						if(ajaxIlSecim == "Bitlis"):
							ilceler = Bitlis
						if(ajaxIlSecim == "Bolu"):
							ilceler = Bolu
						if(ajaxIlSecim == "Burdur"):
							ilceler = Burdur
						if(ajaxIlSecim == "Bursa"):
							ilceler = Bursa
						if(ajaxIlSecim == "Çanakkale"):
							ilceler = Çanakkale
						if(ajaxIlSecim == "Çankırı"):
							ilceler = Çankırı
						if(ajaxIlSecim == "Çorum"):
							ilceler = Çorum
						if(ajaxIlSecim == "Denizli"):
							ilceler = Denizli
						if(ajaxIlSecim == "Diyarbakır"):
							ilceler = Diyarbakır
						if(ajaxIlSecim == "Düzce"):
							ilceler = Düzce
						if(ajaxIlSecim == "Edirne"):
							ilceler = Edirne
						if(ajaxIlSecim == "Elazığ"):
							ilceler = Elazığ
						if(ajaxIlSecim == "Erzincan"):
							ilceler = Erzincan
						if(ajaxIlSecim == "Erzurum"):
							ilceler = Erzurum
						if(ajaxIlSecim == "Eskişehir"):
							ilceler = Eskişehir
						if(ajaxIlSecim == "Gaziantep"):
							ilceler = Gaziantep
						if(ajaxIlSecim == "Giresun"):
							ilceler = Giresun
						if(ajaxIlSecim == "Gümüşhane"):
							ilceler = Gümüşhane
						if(ajaxIlSecim == "Hakkâri"):
							ilceler = Hakkâri																	
						if(ajaxIlSecim == "Hatay"):
							ilceler = Hatay
						if(ajaxIlSecim == "Iğdır"):
							ilceler = Iğdır
						if(ajaxIlSecim == "Isparta"):
							ilceler = Isparta
						if(ajaxIlSecim == "İstanbul"):
							ilceler = İstanbul
						if(ajaxIlSecim == "Karabük"):
							ilceler = Karabük
						if(ajaxIlSecim == "Kahramanmaraş"):
							ilceler = Kahramanmaraş
						if(ajaxIlSecim == "Karaman"):
							ilceler = Karaman
						if(ajaxIlSecim == "Kars"):
							ilceler = Kars
						if(ajaxIlSecim == "Kastamonu"):
							ilceler = Kastamonu
						if(ajaxIlSecim == "Kayseri"):
							ilceler = Kayseri
						if(ajaxIlSecim == "Kırıkkale"):
							ilceler = Kırıkkale
						if(ajaxIlSecim == "Kırklareli"):
							ilceler = Kırklareli
						if(ajaxIlSecim == "Kırşehir"):
							ilceler = Kırşehir
						if(ajaxIlSecim == "Kilis"):
							ilceler = Kilis
						if(ajaxIlSecim == "Kocaeli"):
							ilceler = Kocaeli
						if(ajaxIlSecim == "Konya"):
							ilceler = Konya
						if(ajaxIlSecim == "Kütahya"):
							ilceler = Kütahya
						if(ajaxIlSecim == "Malatya"):
							ilceler = Malatya
						if(ajaxIlSecim == "Manisa"):
							ilceler = Manisa
						if(ajaxIlSecim == "Mardin"):
							ilceler = Mardin
						if(ajaxIlSecim == "Mersin"):
							ilceler = Mersin
						if(ajaxIlSecim == "Muğla"):
							ilceler = Muğla
						if(ajaxIlSecim == "Muş"):
							ilceler = Muş
						if(ajaxIlSecim == "Nevşehir"):
							ilceler = Nevşehir
						if(ajaxIlSecim == "Niğde"):
							ilceler = Niğde
						if(ajaxIlSecim == "Ordu"):
							ilceler = Ordu
						if(ajaxIlSecim == "Osmaniye"):
							ilceler = Osmaniye
						if(ajaxIlSecim == "Rize"):
							ilceler = Rize
						if(ajaxIlSecim == "Sakarya"):
							ilceler = Sakarya
						if(ajaxIlSecim == "Samsun"):
							ilceler = Samsun
						if(ajaxIlSecim == "Siirt"):
							ilceler = Siirt
						if(ajaxIlSecim == "Sinop"):
							ilceler = Sinop
						if(ajaxIlSecim == "Sivas"):
							ilceler = Sivas
						if(ajaxIlSecim == "Şanlıurfa"):
							ilceler = Şanlıurfa
						if(ajaxIlSecim == "Şırnak"):
							ilceler = Şırnak
						if(ajaxIlSecim == "Tekirdağ"):
							ilceler = Tekirdağ
						if(ajaxIlSecim == "Tokat"):
							ilceler = Tokat
						if(ajaxIlSecim == "Trabzon"):
							ilceler = Trabzon
						if(ajaxIlSecim == "Tunceli"):
							ilceler = Tunceli																													
						if(ajaxIlSecim == "Uşak"):
							ilceler = Uşak
						if(ajaxIlSecim == "Van"):
							ilceler = Van
						if(ajaxIlSecim == "Yalova"):
							ilceler = Yalova
						if(ajaxIlSecim == "Yozgat"):
							ilceler = Yozgat
						if(ajaxIlSecim == "Zonguldak"):
							ilceler = Zonguldak				
						context = {"ajaxIlceler" : ilceler}
						return JsonResponse(context)	
				
				sqlYardimlar      = TanimlamaYardimlar.objects.all()
				sqlAvanslar       = TanimlamaAvanslar.objects.all()
				sqlBankaHesaplari = TanimlamaBankaHesaplari.objects.all()
				sqlDestekler      = TanimlamaDestekler.objects.all()
				sqlFazlaMesailer  = TanimlamaFazlaMesailer.objects.all()
				sqlAdresler       = TanimlamaAdresler.objects.all()
				sqlDigerKimlikler = TanimlamaDigerKimlikler.objects.all()
				sqlOkullarKurslar = TanimlamaOkullarKurslar.objects.all()
				sqlSertifikalar   = TanimlamaSertifikalar.objects.all()
				sqlDepartmanlar   = TanimlamaDepartmanlar.objects.all()
				sqlDiller         = TanimlamaDiller.objects.all()
				sqlGorevler       = TanimlamaGorevler.objects.all()
				sqlNitelikler     = TanimlamaNitelikler.objects.all()
				sqlMesaiTipleri   = TanimlamaMesaiTipleri.objects.all()
				sqlVizeler        = TanimlamaVizeler.objects.all()
				sqlIzinler        = TanimlamaIzinler.objects.all()
				sqlPrimler        = TanimlamaPrimler.objects.all()
				sqlPerformaslar   = TanimlamaPerformanslar.objects.all()
				sqlTahakkuklar    = TanimlamaTahakkuklar.objects.all()
				sqlIkramiyeler    = TanimlamaIkramiyeler.objects.all()
				sqlKesintiler     = TanimlamaKesintiler.objects.all()
				sqlPersoneller    = Personel.objects.filter(IsDeleted=False)
				sqlZimmetler      = TanimlamaZimmetler.objects.all()
					
				context = {
					"suan"              : timezone.now(),
					"modulYetkisi"      : modulYetkisi,
					"sqlYardimlar"      : sqlYardimlar,
					"sqlAvanslar"       : sqlAvanslar,
					"sqlBankaHesaplari" : sqlBankaHesaplari,
					"sqlDestekler"      : sqlDestekler,
					"sqlFazlaMesailer"  : sqlFazlaMesailer,
					"sqlAdresler"       : sqlAdresler,
					"sqlDepartmanlar"   : sqlDepartmanlar,
					"sqlDigerKimlikler" : sqlDigerKimlikler,
					"sqlDiller"         : sqlDiller,
					"sqlGorevler"       : sqlGorevler,
					"sqlOkullarKurslar" : sqlOkullarKurslar,
					"sqlSertifikalar"   : sqlSertifikalar,
					"sqlNitelikler"     : sqlNitelikler,
					"sqlMesaiTipleri"   : sqlMesaiTipleri,
					"sqlVizeler"        : sqlVizeler,
					"sqlIzinler"        : sqlIzinler,
					"sqlPrimler"        : sqlPrimler,
					"sqlPerformaslar"   : sqlPerformaslar,
					"sqlTahakkuklar"    : sqlTahakkuklar,
					"sqlIkramiyeler"    : sqlIkramiyeler,
					"sqlKesintiler"     : sqlKesintiler,
					"sqlPersoneller"    : sqlPersoneller,
					"sqlZimmetler"      : sqlZimmetler,
					"meslekler"         : meslekler,
					"pozisyonlar"       : pozisyonlar,
					"ulkeler"           : ulkeler,
					"iller"             : iller,
				}
				return render (request, "personel/hareketler.html", context)
			else:		
				messages.success(request, "Kullanıcı Oluşturma Yetkiniz Yok !")
				return redirect("anasayfa")
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")				