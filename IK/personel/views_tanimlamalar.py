from kullanicilar.models import *
from .models_tanimlamalar import *
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages


def TanimlamaOlustur(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session["KullaniciKodu"],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsKullanicilar == True):
			islemlerKontrol = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
			if(islemlerKontrol.IsKullaniciOlustur == True):
				if(request.is_ajax()):
					#Veri Tabanı Tablolarını değiskene atadık
					degisken        = ""
					aileFerdiTuru   = TanimlamaAileFerdiTurleri
					bankaHesaplari  = TanimlamaBankaHesaplari
					destekler       = TanimlamaDestekler
					gruplar         = TanimlamaGruplar
					izinler         = TanimlamaIzinler
					primler         = TanimlamaPrimler
					tahakkuklar     = TanimlamaTahakkuklar
					ikramiyeler     = TanimlamaIkramiyeler
					kesintiler      = TanimlamaKesintiler
					avanslar        = TanimlamaAvanslar
					departmanlar    = TanimlamaDepartmanlar
					nitelikler      = TanimlamaNitelikler
					performanslar   = TanimlamaPerformanslar
					fazlaMesailer   = TanimlamaFazlaMesailer
					bedenler        = TanimlamaBedenler
					bagimliliklar   = TanimlamaBagimliliklar
					diller          = TanimlamaDiller
					gorevler        = TanimlamaGorevler
					basvuruPuanlari = TanimlamaBasvuruPuanlari
					yetkiler        = TanimlamaYetkiler
					digerKimlikler  = TanimlamaDigerKimlikler 
					tasimaTipleri   = TanimlamaTasimaTipleri
					dovizler 	    = TanimlamaDovizler
					yardimlar       = TanimlamaYardimlar
					maasTipleri     = TanimlamaMaasTipleri
					adresler        = TanimlamaAdresler
					vizeler         = TanimlamaVizeler
					yemekKartlari   = TanimlamaYemekKartlari
					okullarKurslar  = TanimlamaOkullarKurslar
					sertifikalar    = TanimlamaSertifikalar
					mesaiTipleri    = TanimlamaMesaiTipleri 
					zimmetler       = TanimlamaZimmetler
					#Veri Tabanı Tablolarını değiskene atadık
			   # Seçilen Tabloyu Ajax ile Veri Tabanından Post edip Servis Etme 
					ajaxTanimlamalar = request.POST.get("ajaxTanimlamalar")
					if (ajaxTanimlamalar != None):
						if(ajaxTanimlamalar == "avanslar"):
							degisken = avanslar
						elif(ajaxTanimlamalar == "aileFerdiTuru"):
							degisken = aileFerdiTuru
						elif(ajaxTanimlamalar == "bankaHesaplari"):
							degisken = bankaHesaplari	
						elif(ajaxTanimlamalar == "destekler"):
							degisken = destekler	
						elif(ajaxTanimlamalar == "gruplar"):
							degisken = gruplar	
						elif(ajaxTanimlamalar == "izinler"):
							degisken = izinler		
						elif(ajaxTanimlamalar == "primler"):
							degisken = primler
						elif(ajaxTanimlamalar == "tahakkuklar"):
							degisken = tahakkuklar
						elif(ajaxTanimlamalar == "ikramiyeler"):
							degisken = ikramiyeler
						elif(ajaxTanimlamalar == "kesintiler"):
							degisken = kesintiler
						elif(ajaxTanimlamalar == "departmanlar"):
							degisken = departmanlar	
						elif(ajaxTanimlamalar == "nitelikler"):
							degisken = nitelikler
						elif(ajaxTanimlamalar == "performanslar"):
							degisken = performanslar
						elif(ajaxTanimlamalar == "fazlaMesailer"):
							degisken = fazlaMesailer	
						elif(ajaxTanimlamalar == "bedenler"):
							degisken = bedenler
						elif(ajaxTanimlamalar == "bagimliliklar"):
							degisken = bagimliliklar
						elif(ajaxTanimlamalar == "diller"):
							degisken = diller
						elif(ajaxTanimlamalar == "gorevler"):
							degisken = gorevler
						elif(ajaxTanimlamalar == "basvuruPuanlari"):
							degisken = basvuruPuanlari
						elif(ajaxTanimlamalar == "yetkiler"):
							degisken = yetkiler
						elif(ajaxTanimlamalar == "digerKimlikler"):
							degisken = digerKimlikler
						elif(ajaxTanimlamalar == "tasimaTipleri"):
							degisken = tasimaTipleri
						elif(ajaxTanimlamalar == "dovizler"):
							degisken = dovizler
						elif(ajaxTanimlamalar == "yardimlar"):
							degisken = yardimlar
						elif(ajaxTanimlamalar == "maasTipleri"):
							degisken = maasTipleri
						elif(ajaxTanimlamalar == "adresler"):
							degisken = adresler
						elif(ajaxTanimlamalar == "vizeler"):
							degisken = vizeler
						elif(ajaxTanimlamalar == "yemekKartlari"):
							degisken = yemekKartlari
						elif(ajaxTanimlamalar == "okullarKurslar"):
							degisken = okullarKurslar
						elif(ajaxTanimlamalar == "sertifikalar"):
							degisken = sertifikalar
						elif(ajaxTanimlamalar == "mesaiTipleri"):
							degisken = mesaiTipleri
						elif(ajaxTanimlamalar == "zimmetler"):
							degisken = zimmetler							
						tanimlamalarListesi = []
						for tanimlamaKayitTanimlamalar in degisken.objects.all():
							tanimlamaListesi = []
							tanimlamaListesi.append(tanimlamaKayitTanimlamalar.id)
							if(tanimlamaKayitTanimlamalar.id == None):
								tanimlamaKayitTanimlamalar.id = ""
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Kodu)
							else:
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Kodu)
							if(tanimlamaKayitTanimlamalar.Kodu == None):
								tanimlamaKayitTanimlamalar.Kodu = ""
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Icerik)
							else:
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Icerik)
							if(tanimlamaKayitTanimlamalar.Deger == None):
								tanimlamaKayitTanimlamalar.Deger = ""
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Deger)
							elif(tanimlamaKayitTanimlamalar.Deger == 0.0):
								tanimlamaKayitTanimlamalar.Deger = 0
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Deger)	
							else:
								tanimlamaListesi.append(tanimlamaKayitTanimlamalar.Deger)				
							tanimlamalarListesi.append(tanimlamaListesi)
						context = {"ajaxTanimlamaListesi" : tanimlamalarListesi}
						return JsonResponse(context)
				# Seçilen Tabloyu Ajax ile Veri Tabanından Post edip Servis Etme 
					ajaxTanimlamalarListesi = request.POST.get("ajaxTanimlamalarListesi")
					if (ajaxTanimlamalarListesi != None):
						ajaxTanimlamalarListesi = ajaxTanimlamalarListesi.split("<|>")
						if(ajaxTanimlamalarListesi[1] == "avanslar"):
							degisken = avanslar
						elif(ajaxTanimlamalarListesi[1] == "aileFerdiTuru"):
							degisken = aileFerdiTuru
						elif(ajaxTanimlamalarListesi[1] == "gruplar"):
							degisken = gruplar	
						elif(ajaxTanimlamalarListesi[1] == "destekler"):
							degisken = destekler	
						elif(ajaxTanimlamalarListesi[1] == "bankaHesaplari"):
							degisken = bankaHesaplari	
						elif(ajaxTanimlamalarListesi[1] == "izinler"):
							degisken = izinler		
						elif(ajaxTanimlamalarListesi[1] == "primler"):
							degisken = primler
						elif(ajaxTanimlamalarListesi[1] == "tahakkuklar"):
							degisken = tahakkuklar
						elif(ajaxTanimlamalarListesi[1] == "ikramiyeler"):
							degisken = ikramiyeler
						elif(ajaxTanimlamalarListesi[1] == "kesintiler"):
							degisken = kesintiler	
						elif(ajaxTanimlamalarListesi[1] == "departmanlar"):
							degisken = departmanlar	
						elif(ajaxTanimlamalarListesi[1] == "nitelikler"):
							degisken = nitelikler
						elif(ajaxTanimlamalarListesi[1] == "fazlaMesailer"):
							degisken = fazlaMesailer	
						elif(ajaxTanimlamalarListesi[1] == "performanslar"):
							degisken = performanslar
						elif(ajaxTanimlamalarListesi[1] == "bedenler"):
							degisken = bedenler
						elif(ajaxTanimlamalarListesi[1] == "bagimliliklar"):
							degisken = bagimliliklar
						elif(ajaxTanimlamalarListesi[1] == "diller"):
							degisken = diller
						elif(ajaxTanimlamalarListesi[1] == "gorevler"):
							degisken = gorevler
						elif(ajaxTanimlamalarListesi[1] == "basvuruPuanlari"):
							degisken = basvuruPuanlari
						elif(ajaxTanimlamalarListesi[1] == "yetkiler"):
							degisken = yetkiler
						elif(ajaxTanimlamalarListesi[1] == "digerKimlikler"):
							degisken = digerKimlikler
						elif(ajaxTanimlamalarListesi[1] == "tasimaTipleri"):
							degisken = tasimaTipleri
						elif(ajaxTanimlamalarListesi[1] == "dovizler"):
							degisken = dovizler
						elif(ajaxTanimlamalarListesi[1] == "yardimlar"):
							degisken = yardimlar
						elif(ajaxTanimlamalarListesi[1] == "maasTipleri"):
							degisken = maasTipleri
						elif(ajaxTanimlamalarListesi[1] == "adresler"):
							degisken = adresler
						elif(ajaxTanimlamalarListesi[1] == "vizeler"):
							degisken = vizeler
						elif(ajaxTanimlamalarListesi[1] == "yemekKartlari"):
							degisken = yemekKartlari
						elif(ajaxTanimlamalarListesi[1] == "okullarKurslar"):
							degisken = okullarKurslar
						elif(ajaxTanimlamalarListesi[1] == "sertifikalar"):
							degisken = sertifikalar
						elif(ajaxTanimlamalarListesi[1] == "mesaiTipleri"):
							degisken = mesaiTipleri	
						elif(ajaxTanimlamalarListesi[1] == "zimmetler"):
							degisken = zimmetler		
						try:
							tanimlamaKontrol = get_object_or_404(degisken,Kodu=ajaxTanimlamalarListesi[2],Deger=ajaxTanimlamalarListesi[3])
							context = {"ajaxMesaj" : "Kayıtlı Tanımlama"}
							return JsonResponse(context)
						except:
							tanimlamaKayit = degisken()
							tanimlamaKayit.Kodu = ajaxTanimlamalarListesi[2]
							tanimlamaKayit.Icerik = ajaxTanimlamalarListesi[3]
							ajaxTanimlamalarListesi[4].replace(",",".")
							if(ajaxTanimlamalarListesi[4] == ""):
								tanimlamaKayit.Deger = 0
							else:
								tanimlamaKayit.Deger = ajaxTanimlamalarListesi[4]	
							tanimlamaKayit.save()
							context = {"ajaxMesaj" : "Kayıt Oluşturuldu"}
							return JsonResponse(context)	
					#------------- Tanımlamna Oluşturma -----------
					#------------- Tanımlamna Silme Güncelleme -----------
					ajaxTanimlamaGuncelle = request.POST.get("ajaxTanimlamaGuncelle")
					if(ajaxTanimlamaGuncelle != None):
						tanimlamaGuncellemeSplit = ajaxTanimlamaGuncelle.split("<|>")
						if(tanimlamaGuncellemeSplit[0] == "sil"):
							if(tanimlamaGuncellemeSplit[2] == "avanslar"):
								degisken = avanslar
							elif(tanimlamaGuncellemeSplit[2] == "aileFerdiTuru"):
								degisken = aileFerdiTuru
							elif(tanimlamaGuncellemeSplit[2] == "bankaHesaplari"):
								degisken = bankaHesaplari	
							elif(tanimlamaGuncellemeSplit[2] == "destekler"):
								degisken = destekler	
							elif(tanimlamaGuncellemeSplit[2] == "izinler"):
								degisken = izinler	
							elif(tanimlamaGuncellemeSplit[2] == "gruplar"):
								degisken = gruplar		
							elif(tanimlamaGuncellemeSplit[2] == "primler"):
								degisken = primler
							elif(tanimlamaGuncellemeSplit[2] == "tahakkuklar"):
								degisken = tahakkuklar
							elif(tanimlamaGuncellemeSplit[2] == "ikramiyeler"):
								degisken = ikramiyeler
							elif(tanimlamaGuncellemeSplit[2] == "kesintiler"):
								degisken = kesintiler
							elif(tanimlamaGuncellemeSplit[2] == "departmanlar"):
								degisken = departmanlar	
							elif(tanimlamaGuncellemeSplit[2] == "nitelikler"):
								degisken = nitelikler
							elif(tanimlamaGuncellemeSplit[2] == "fazlaMesailer"):
								degisken = fazlaMesailer	
							elif(tanimlamaGuncellemeSplit[2] == "performanslar"):
								degisken = performanslar
							elif(tanimlamaGuncellemeSplit[2] == "bedenler"):
								degisken = bedenler
							elif(tanimlamaGuncellemeSplit[2] == "bagimliliklar"):
								degisken = bagimliliklar
							elif(tanimlamaGuncellemeSplit[2] == "diller"):
								degisken = diller
							elif(tanimlamaGuncellemeSplit[2] == "gorevler"):
								degisken = gorevler
							elif(tanimlamaGuncellemeSplit[2] == "basvuruPuanlari"):
								degisken = TanimlamaBasvuruPuanlari
							elif(tanimlamaGuncellemeSplit[2] == "yetkiler"):
								degisken = yetkiler
							elif(tanimlamaGuncellemeSplit[2] == "digerKimlikler"):
								degisken = digerKimlikler
							elif(tanimlamaGuncellemeSplit[2] == "tasimaTipleri"):
								degisken = tasimaTipleri
							elif(tanimlamaGuncellemeSplit[2] == "dovizler"):
								degisken = dovizler
							elif(tanimlamaGuncellemeSplit[2] == "yardimlar"):
								degisken = yardimlar
							elif(tanimlamaGuncellemeSplit[2] == "maasTipleri"):
								degisken = maasTipleri
							elif(tanimlamaGuncellemeSplit[2] == "adresler"):
								degisken = adresler
							elif(tanimlamaGuncellemeSplit[2] == "vizeler"):
								degisken = vizeler
							elif(tanimlamaGuncellemeSplit[2] == "yemekKartlari"):
								degisken = yemekKartlari
							elif(tanimlamaGuncellemeSplit[2] == "okullarKurslar"):
								degisken = okullarKurslar
							elif(tanimlamaGuncellemeSplit[2] == "sertifikalar"):
								degisken = sertifikalar
							elif(tanimlamaGuncellemeSplit[2] == "mesaiTipleri"):
								degisken = mesaiTipleri	
							elif(tanimlamaGuncellemeSplit[2] == "zimmetler"):
								degisken = zimmetler		
							tanimlamaKontrol = get_object_or_404(degisken,id=tanimlamaGuncellemeSplit[1])
							tanimlamaKontrol.delete()
							context = {"ajaxMesaj" : "Silindi"}
							return JsonResponse(context)

						if(tanimlamaGuncellemeSplit[0] == "guncelle"):
							if(tanimlamaGuncellemeSplit[2] == "avanslar"):
								degisken = avanslar
							elif(tanimlamaGuncellemeSplit[2] == "gruplar"):
								degisken = gruplar
							elif(tanimlamaGuncellemeSplit[2] == "aileFerdiTuru"):
								degisken = aileFerdiTuru	
							elif(tanimlamaGuncellemeSplit[2] == "destekler"):
								degisken = destekler	
							elif(tanimlamaGuncellemeSplit[2] == "bankaHesaplari"):
								degisken = bankaHesaplari	
							elif(tanimlamaGuncellemeSplit[2] == "izinler"):
								degisken = izinler		
							elif(tanimlamaGuncellemeSplit[2] == "primler"):
								degisken = primler
							elif(tanimlamaGuncellemeSplit[2] == "tahakkuklar"):
								degisken = tahakkuklar
							elif(tanimlamaGuncellemeSplit[2] == "ikramiyeler"):
								degisken = ikramiyeler
							elif(tanimlamaGuncellemeSplit[2] == "kesintiler"):
								degisken = kesintiler	
							elif(tanimlamaGuncellemeSplit[2] == "departmanlar"):
								degisken = departmanlar	
							elif(tanimlamaGuncellemeSplit[2] == "nitelikler"):
								degisken = nitelikler
							elif(tanimlamaGuncellemeSplit[2] == "fazlaMesailer"):
								degisken = fazlaMesailer	
							elif(tanimlamaGuncellemeSplit[2] == "performanslar"):
								degisken = performanslar
							elif(tanimlamaGuncellemeSplit[2] == "bedenler"):
								degisken = bedenler
							elif(tanimlamaGuncellemeSplit[2] == "bagimliliklar"):
								degisken = bagimliliklar
							elif(tanimlamaGuncellemeSplit[2] == "diller"):
								degisken = diller
							elif(tanimlamaGuncellemeSplit[2] == "gorevler"):
								degisken = gorevler
							elif(tanimlamaGuncellemeSplit[2] == "basvuruPuanlari"):
								degisken = TanimlamaBasvuruPuanlari
							elif(tanimlamaGuncellemeSplit[2] == "yetkiler"):
								degisken = yetkiler
							elif(tanimlamaGuncellemeSplit[2] == "digerKimlikler"):
								degisken = digerKimlikler
							elif(tanimlamaGuncellemeSplit[2] == "tasimaTipleri"):
								degisken = tasimaTipleri
							elif(tanimlamaGuncellemeSplit[2] == "dovizler"):
								degisken = dovizler
							elif(tanimlamaGuncellemeSplit[2] == "yardimlar"):
								degisken = yardimlar
							elif(tanimlamaGuncellemeSplit[2] == "maasTipleri"):
								degisken = maasTipleri
							elif(tanimlamaGuncellemeSplit[2] == "adresler"):
								degisken = adresler
							elif(tanimlamaGuncellemeSplit[2] == "vizeler"):
								degisken = vizeler
							elif(tanimlamaGuncellemeSplit[2] == "yemekKartlari"):
								degisken = yemekKartlari
							elif(tanimlamaGuncellemeSplit[2] == "okullarKurslar"):
								degisken = okullarKurslar
							elif(tanimlamaGuncellemeSplit[2] == "sertifikalar"):
								degisken = sertifikalar
							elif(tanimlamaGuncellemeSplit[2] == "mesaiTipleri"):
								degisken = mesaiTipleri
							elif(tanimlamaGuncellemeSplit[2] == "zimmetler"):
								degisken = zimmetler
							tanimlamaKontrol = get_object_or_404(degisken,id=tanimlamaGuncellemeSplit[1])
							tanimlamaKontrol.Kodu   = tanimlamaGuncellemeSplit[3]
							tanimlamaKontrol.Icerik = tanimlamaGuncellemeSplit[4]
							tanimlamaKontrol.Deger  = tanimlamaGuncellemeSplit[5].replace(",",".")
							tanimlamaKontrol.save()
							context = {
								"ajaxKodu"   : str(tanimlamaKontrol.Kodu),
						    	"ajaxIcerik" : str(tanimlamaKontrol.Icerik),
						    	"ajaxDeger"  : str(tanimlamaKontrol.Deger),
							}	
							return JsonResponse(context)	
						#-------------tablo silme güncelleme -----------
				context = {
					"modulYetkisi" : modulYetkisi,
				}
				return render (request, "personel/tanimlamalar.html", context)
			else:		
				messages.success(request, "Kullanıcı Oluşturma Yetkiniz Yok !")
				return redirect("anasayfa")
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")