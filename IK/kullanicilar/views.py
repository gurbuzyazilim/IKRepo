import random
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .encryption import encryption_h
from django.utils import timezone

 
def Capce():
	liste = range(10)
	capce = ""
	for i in random.sample(liste, 5):
		capce = capce + str(i)
	return capce

def KullaniciGiris(request):
	request.session.clear()
	if request.is_ajax():
		ajaxKullaniciAdi    = request.POST.get("ajaxKullaniciAdi")
		ajaxKullaniciParola = request.POST.get("ajaxKullaniciParola")
		ajaxCapce 			= request.POST.get("ajaxCapce")
		if(ajaxCapce == capce):
			if (ajaxKullaniciAdi != "" and ajaxKullaniciParola != ""):
				encryptionParola = encryption_h(ajaxKullaniciAdi, ajaxKullaniciParola)
				try:
					sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciAdi=ajaxKullaniciAdi, KullaniciParola=encryptionParola)
					if(sqlKullanicilar.KullaniciDurumu == True):
						sqlKullanicilar.SonGiris = timezone.now()
						sqlKullanicilar.save()
						request.session["KullaniciKodu"] = sqlKullanicilar.KullaniciKodu
						request.session["KullaniciAdi"]  = sqlKullanicilar.KullaniciAdi
						ajaxMesaj = True
					if(sqlKullanicilar.KullaniciDurumu == False):
						ajaxMesaj = "Kullanıcı Pasifize Edilmiş !"	
				except:
					ajaxMesaj = "Böyle Bir Kullanici Yok !"	
			else:
				ajaxMesaj = "Kullanıcı Adı Ve Parola Boş Bırakılamaz !"
		else:
			ajaxMesaj = "Girmiş Olduğunuz Kod Doğrulanamadı !"
		context = {"ajaxMesaj" : ajaxMesaj}
		return JsonResponse(context)
	global capce	
	capce = Capce()
	context = {"capce" : capce,}
	return render(request, "kullanicilar/giris.html", context)

def KullaniciCikis(request):
	request.session.clear()
	return redirect ("kullanicilar:giris")

def KullaniciKayit(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session['KullaniciKodu'],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsKullanicilar == True):
			islemlerKontrol = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
			if(islemlerKontrol.IsKullaniciOlustur == True):			
				if request.is_ajax():
					ajaxKullaniciKodu 			 = request.POST.get("ajaxKullaniciKodu")
					ajaxKullaniciAdi 			 = request.POST.get("ajaxKullaniciAdi")
					ajaxKullaniciParola 		 = request.POST.get("ajaxKullaniciParola")
					ajaxKullaniciParolaDogrulama = request.POST.get("ajaxKullaniciParolaD")
					ajaxKullaniciTipi   		 = request.POST.get("ajaxKullaniciTipi")
					ajaxKullaniciGrubu  		 = request.POST.get("ajaxKullaniciGrubu")
					ajaxKullaniciDurumu 		 = request.POST.get("ajaxKullaniciDurumu")
					if(ajaxKullaniciKodu and ajaxKullaniciAdi and ajaxKullaniciParola and ajaxKullaniciParolaDogrulama and ajaxKullaniciTipi and ajaxKullaniciDurumu):	
						if(ajaxKullaniciParola == ajaxKullaniciParolaDogrulama):
							try:
								sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciKodu=ajaxKullaniciKodu)
								ajaxMesaj = "Kayıtlı Kullanıcı Kodu !"
								key = 0
							except:
								key = 1
							try:
								sqlKullanicilar = get_object_or_404(Kullanicilar, KullaniciAdi=ajaxKullaniciAdi)
								ajaxMesaj = "Kayıtlı Kullanıcı Adı !"
								key1 = 0
							except:
								key1 = 1	
							if(key and key1 == 1):
								encryptionParola = encryption_h(ajaxKullaniciAdi, ajaxKullaniciParola)
								sqlKullanicilar  = Kullanicilar()
								sqlKullanicilar.KullaniciKodu   = ajaxKullaniciKodu
								sqlKullanicilar.KullaniciAdi    = ajaxKullaniciAdi
								sqlKullanicilar.KullaniciParola = encryptionParola
								sqlKullanicilar.KullaniciTipi   = ajaxKullaniciTipi
								sqlKullanicilar.KullaniciGrubu  = ajaxKullaniciGrubu	
								sqlKullanicilar.KullaniciDurumu = ajaxKullaniciDurumu
								sqlKullanicilar.KayitTarihi 	= timezone.now()
								sqlKullanicilar.KayitYapan 		= request.session["KullaniciKodu"]
								sqlKullanicilar.save()
								context = {"ajaxMesaj" : True}
								return JsonResponse(context)
						else:
							ajaxMesaj = "Parolalar Eşleşmiyor !"
						context = {"ajaxMesaj" : ajaxMesaj}
						return JsonResponse(context)
					else:
						ajaxMesaj = "Lütfen Formu Boş Bırakmayınız !"
						context = {"ajaxMesaj" : ajaxMesaj}
						return JsonResponse(context)		
				sqlKullaniciTipiModel = KullaniciTipiModel.objects.all()
				sqlKullaniciGrubuModel = KullaniciGrubuModel.objects.all()
				context = {
					"modulYetkisi" 			 : modulYetkisi,
					"sqlKullaniciTipiModel"  : sqlKullaniciTipiModel,
					"sqlKullaniciGrubuModel" : sqlKullaniciGrubuModel,
				}
				return render(request, "kullanicilar/kayit.html",context)	
			else:		
				messages.success(request, "Kullanıcı Oluşturma Yetkiniz Yok !")
				return redirect("anasayfa")
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")

def KullaniciListele(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session["KullaniciKodu"],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsKullanicilar == True):
			islemlerKontrol = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
			if(islemlerKontrol.IsKullaniciListele == True):
				if request.is_ajax():
					ajaxDetay = request.POST.get("ajaxDetay")
					if(ajaxDetay):
						sqlKullanicilarDetay = get_object_or_404(Kullanicilar,KullaniciKodu=ajaxDetay)
						context = {
							"ajaxKullaniciKodu"   : sqlKullanicilarDetay.KullaniciKodu,
							"ajaxKullaniciAdi"    : sqlKullanicilarDetay.KullaniciAdi,
							"ajaxKullaniciTipi"   : sqlKullanicilarDetay.KullaniciTipi,
							"ajaxKullaniciGrubu"  : sqlKullanicilarDetay.KullaniciGrubu,
							"ajaxKullaniciDurumu" : sqlKullanicilarDetay.KullaniciDurumu,
							"ajaxSonGiris"        : sqlKullanicilarDetay.SonGiris,
							"ajaxKayitTarihi"     : sqlKullanicilarDetay.KayitTarihi,
							"ajaxKayitYapan"      : sqlKullanicilarDetay.KayitYapan,
							"ajaxDuzeltmeTarihi"  : sqlKullanicilarDetay.DuzeltmeTarihi,
							"ajaxDuzeltmeYapan"   : sqlKullanicilarDetay.DuzeltmeYapan,
						}
						return JsonResponse(context)
					ajaxGuncelle = request.POST.get("ajaxGuncelle")
					if(ajaxGuncelle):
						sqlKullanicilarGuncelle = get_object_or_404(Kullanicilar,KullaniciKodu=ajaxGuncelle)
						if(sqlKullanicilarGuncelle.KullaniciDurumu == True):
							varKullaniciDurumu = 1
						if(sqlKullanicilarGuncelle.KullaniciDurumu == False):
							varKullaniciDurumu = 0	
						context = {
							"ajaxKullaniciIdGuncelle"     : sqlKullanicilarGuncelle.id,
							"ajaxKullaniciKoduGuncelle"   : sqlKullanicilarGuncelle.KullaniciKodu,
							"ajaxKullaniciAdiGuncelle"    : sqlKullanicilarGuncelle.KullaniciAdi,
							"ajaxKullaniciTipiGuncelle"   : sqlKullanicilarGuncelle.KullaniciTipi,
							"ajaxKullaniciGrubuGuncelle"  : sqlKullanicilarGuncelle.KullaniciGrubu,
							"ajaxKullaniciDurumuGuncelle" : varKullaniciDurumu,
							"ajaxKullaniciParolaGuncelle" : sqlKullanicilarGuncelle.KullaniciParola,
						}
						return JsonResponse(context)

					ajaxKullaniciIdKaydet      = request.POST.get("ajaxKullaniciIdKaydet")
					ajaxKullaniciKoduKaydet    = request.POST.get("ajaxKullaniciKoduKaydet")
					ajaxKullaniciAdiKaydet 	   = request.POST.get("ajaxKullaniciAdiKaydet")
					ajaxKullaniciParolaKaydet  = request.POST.get("ajaxKullaniciParolaKaydet")
					ajaxKullaniciParolaDKaydet = request.POST.get("ajaxKullaniciParolaDKaydet")
					ajaxKullaniciTipiKaydet    = request.POST.get("ajaxKullaniciTipiKaydet")
					ajaxKullaniciGrubuKaydet   = request.POST.get("ajaxKullaniciGrubuKaydet")
					ajaxKullaniciDurumuKaydet  = request.POST.get("ajaxKullaniciDurumuKaydet")
					if(ajaxKullaniciIdKaydet):
						if(ajaxKullaniciKoduKaydet and ajaxKullaniciAdiKaydet and ajaxKullaniciParolaKaydet and ajaxKullaniciParolaDKaydet and ajaxKullaniciTipiKaydet and ajaxKullaniciDurumuKaydet):
							if(ajaxKullaniciParolaKaydet == ajaxKullaniciParolaDKaydet):
								encryptionPassword = encryption_h(ajaxKullaniciAdiKaydet, ajaxKullaniciParolaKaydet)
								sqlKaydet = get_object_or_404(Kullanicilar,id=ajaxKullaniciIdKaydet)
								sqlKaydet.KullaniciKodu   = ajaxKullaniciKoduKaydet
								sqlKaydet.KullaniciAdi 	  = ajaxKullaniciAdiKaydet
								sqlKaydet.KullaniciParola = encryptionPassword
								sqlKaydet.KullaniciTipi   = ajaxKullaniciTipiKaydet
								sqlKaydet.KullaniciGrubu  = ajaxKullaniciGrubuKaydet
								sqlKaydet.KullaniciDurumu = ajaxKullaniciDurumuKaydet
								sqlKaydet.DuzeltmeTarihi  = timezone.now()
								sqlKaydet.DuzeltmeYapan   = request.session["KullaniciKodu"]
								sqlKaydet.save()
								ajaxMesaj = True
							else:
								ajaxMesaj = "Parolalar Eşleşmiyor !"
							context = {"ajaxMesaj" : ajaxMesaj}
							return JsonResponse(context)
						else:
							ajaxMesaj = "Lütfen Formu Boş Bırakmayınız !"
							context = {"ajaxMesaj" : ajaxMesaj}
							return JsonResponse(context)	
					ajaxSil = request.POST.get("ajaxSil")
					if(ajaxSil):
						sqlKullanicilarSil = get_object_or_404(Kullanicilar,KullaniciKodu=ajaxSil)
						sqlKullanicilarSil.IsDeleted = True
						sqlKullanicilarSil.save()
						context = {"ajaxMesaj":"Silme İşlemi Başarılı !",}
						return JsonResponse(context)				
				sqlKullanicilar = Kullanicilar.objects.filter(IsDeleted=False)
				sqlKullaniciTipi = KullaniciTipiModel.objects.all()
				sqlKullaniciGrubu = KullaniciGrubuModel.objects.all()
				context = {
					"modulYetkisi"      : modulYetkisi,
					"islemlerKontrol"   : islemlerKontrol,
					"sqlKullanicilar"   : sqlKullanicilar,
					"sqlKullaniciTipi"  : sqlKullaniciTipi,
					"sqlKullaniciGrubu" : sqlKullaniciGrubu,
				}
				return render (request, "kullanicilar/listele.html", context)
			else:		
				messages.success(request, "Kullanıcı Listesini Görüntüleme Yetkiniz Yok !")
				return redirect("anasayfa")
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")

def Tanimlamalar(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session['KullaniciKodu'],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if (modulYetkisi.IsKullanicilar == True):
			if request.is_ajax():
				ajaxKullaniciGrubuKodu = request.POST.get("ajaxKullaniciGrubuKodu")
				ajaxKullaniciGrubu     = request.POST.get("ajaxKullaniciGrubu")
				if(ajaxKullaniciGrubu):
					sqlKullaniciTanimlamalari = KullaniciGrubuModel()
					sqlKullaniciTanimlamalari.KullaniciGrubuKodu = ajaxKullaniciGrubuKodu
					sqlKullaniciTanimlamalari.KullaniciGrubu     = ajaxKullaniciGrubu
					sqlKullaniciTanimlamalari.save()
					context = {"ajaxMesaj" : "Kayıt Başarılı !",}
					return JsonResponse(context)

				ajaxKullaniciTipleri = request.POST.get("ajaxKullaniciTipleri")	
				if(ajaxKullaniciTipleri):
					sqlModulYetkileri  = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					modulYetkileriList = []
					if(sqlModulYetkileri.IsAnaSayfa == True):
						modulYetkileriList.append("Anasayfa")
					if(sqlModulYetkileri.IsKullanicilar == True):
						modulYetkileriList.append("Kullanıcılar")
					if(sqlModulYetkileri.IsPersoneller == True):
						modulYetkileriList.append("Personeller")
					if(sqlModulYetkileri.IsHareketler == True):
						modulYetkileriList.append("Hareketler")
					if(sqlModulYetkileri.IsTanimlamalar == True):
						modulYetkileriList.append("Tanımlamalar")

					sqlAnasayfaYetkileri  = get_object_or_404(AnasayfaYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					anasayfaYetkileriList = []
					if(sqlAnasayfaYetkileri.IsDuyuruOlustur == True):
						anasayfaYetkileriList.append("Duyuru Oluştur")
					if(sqlAnasayfaYetkileri.IsGorevOlustur == True):
						anasayfaYetkileriList.append("Görev Oluştur")
					if(sqlAnasayfaYetkileri.IsHatirlatmaOlustur == True):
						anasayfaYetkileriList.append("Hatırlatma Oluştur")
					if(sqlAnasayfaYetkileri.IsDuyuruGoruntule == True):
						anasayfaYetkileriList.append("Duyuru Görüntüle")
					if(sqlAnasayfaYetkileri.IsGorevGoruntule == True):
						anasayfaYetkileriList.append("Görev Görüntüle")
					if(sqlAnasayfaYetkileri.IsHatirlatmaGoruntule == True):
						anasayfaYetkileriList.append("Hatırlatma Görüntüle")
					
					sqlKullaniciYetkileri  = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					kullaniciYetkileriList = []
					if(sqlKullaniciYetkileri.IsKullaniciOlustur == True):
						kullaniciYetkileriList.append("Kullanıcı Oluştur")
					if(sqlKullaniciYetkileri.IsKullaniciListele == True):
						kullaniciYetkileriList.append("Kullanıcı Listele")
					if(sqlKullaniciYetkileri.IsKullaniciDetay == True):
						kullaniciYetkileriList.append("Kullanıcı Detay")
					if(sqlKullaniciYetkileri.IsKullaniciGuncelle == True):
						kullaniciYetkileriList.append("Kullanıcı Güncelle")
					if(sqlKullaniciYetkileri.IsKullaniciSil == True):
						kullaniciYetkileriList.append("Kullanıcı Sil")		

					sqlPersonelYetkileri  = get_object_or_404(PersonelYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					personelYetkileriList = []
					if(sqlPersonelYetkileri.IsPersonelOlustur == True):
						personelYetkileriList.append("Personel Oluştur")
					if(sqlPersonelYetkileri.IsPersonelListele == True):
						personelYetkileriList.append("Personel Listele")
					if(sqlPersonelYetkileri.IsPersonelDetay == True):
						personelYetkileriList.append("Personel Detay")
					if(sqlPersonelYetkileri.IsPersonelGuncelle == True):
						personelYetkileriList.append("Personel Güncelle")
					if(sqlPersonelYetkileri.IsPersonelSil == True):
						personelYetkileriList.append("Personel Sil")

					sqlHareketYetkileri  = get_object_or_404(HareketYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					hareketYetkileriList = []
					if(sqlHareketYetkileri.IsHareketOlustur == True):
						hareketYetkileriList.append("Personel Oluştur")
					if(sqlHareketYetkileri.IsHareketListele == True):
						hareketYetkileriList.append("Personel Listele")
					if(sqlHareketYetkileri.IsHareketDetay == True):
						hareketYetkileriList.append("Personel Detay")
					if(sqlHareketYetkileri.IsHareketGuncelle == True):
						hareketYetkileriList.append("Personel Güncelle")
					if(sqlHareketYetkileri.IsHareketSil == True):
						hareketYetkileriList.append("Personel Sil")

					sqlTanimlamaYetkileri  = get_object_or_404(TanimlamaYetkileri,KullaniciTipiKodu=ajaxKullaniciTipleri)
					tanimlamaYetkileriList = []
					if(sqlTanimlamaYetkileri.IsTanimlamaOlustur == True):
						tanimlamaYetkileriList.append("Personel Oluştur")
					if(sqlTanimlamaYetkileri.IsTanimlamaListele == True):
						tanimlamaYetkileriList.append("Personel Listele")
					if(sqlTanimlamaYetkileri.IsTanimlamaDetay == True):
						tanimlamaYetkileriList.append("Personel Detay")
					if(sqlTanimlamaYetkileri.IsTanimlamaGuncelle == True):
						tanimlamaYetkileriList.append("Personel Güncelle")
					if(sqlTanimlamaYetkileri.IsTanimlamaSil == True):
						tanimlamaYetkileriList.append("Personel Sil")								

					context = {
						"ajaxModulYetkileri"     : modulYetkileriList,
						"ajaxAnasayfaYetkileri"  : anasayfaYetkileriList,
						"ajaxKullaniciYetkileri" : kullaniciYetkileriList,
						"ajaxPersonelYetkileri"  : personelYetkileriList,
						"ajaxHareketYetkileri"   : hareketYetkileriList,
						"ajaxTanimlamaYetkileri" : tanimlamaYetkileriList,
					}
					return JsonResponse(context)

				ajaxKullaniciTipiKodu  = request.POST.get("ajaxKullaniciTipiKodu")
				ajaxKullaniciTipi      = request.POST.get("ajaxKullaniciTipi")
				
				ajaxIsAnaSayfa     = request.POST.get("ajaxIsAnaSayfa")
				ajaxIsKullanicilar = request.POST.get("ajaxIsKullanicilar")
				ajaxIsPersoneller  = request.POST.get("ajaxIsPersoneller")
				ajaxIsHareketler   = request.POST.get("ajaxIsHareketler")
				ajaxIsTanimlamalar = request.POST.get("ajaxIsTanimlamalar")

				ajaxIsDuyuruOlustur       = request.POST.get("ajaxIsDuyuruOlustur")
				ajaxIsGorevOlustur        = request.POST.get("ajaxIsGorevOlustur")
				ajaxIsHatirlatmaOlustur   = request.POST.get("ajaxIsHatirlatmaOlustur")
				ajaxIsDuyuruGoruntule     = request.POST.get("ajaxIsDuyuruGoruntule")
				ajaxIsGorevGoruntule	  = request.POST.get("ajaxIsGorevGoruntule")
				ajaxIsHatirlatmaGoruntule = request.POST.get("ajaxIsHatirlatmaGoruntule")

				ajaxIsKullaniciOlustur  = request.POST.get("ajaxIsKullaniciOlustur")
				ajaxIsKullaniciListele  = request.POST.get("ajaxIsKullaniciListele")
				ajaxIsKullaniciDetay    = request.POST.get("ajaxIsKullaniciDetay")
				ajaxIsKullaniciGuncelle = request.POST.get("ajaxIsKullaniciGuncelle")
				ajaxIsKullaniciSil	    = request.POST.get("ajaxIsKullaniciSil")

				ajaxIsPersonelOlustur  = request.POST.get("ajaxIsPersonelOlustur")
				ajaxIsPersonelListele  = request.POST.get("ajaxIsPersonelListele")
				ajaxIsPersonelDetay    = request.POST.get("ajaxIsPersonelDetay")
				ajaxIsPersonelGuncelle = request.POST.get("ajaxIsPersonelGuncelle")
				ajaxIsPersonelSil	   = request.POST.get("ajaxIsPersonelSil")

				ajaxIsHareketOlustur  = request.POST.get("ajaxIsHareketOlustur")
				ajaxIsHareketListele  = request.POST.get("ajaxIsHareketListele")
				ajaxIsHareketDetay    = request.POST.get("ajaxIsHareketDetay")
				ajaxIsHareketGuncelle = request.POST.get("ajaxIsHareketGuncelle")		
				ajaxIsHareketSil	  = request.POST.get("ajaxIsHareketSil")

				ajaxIsTanimlamaOlustur  = request.POST.get("ajaxIsTanimlamaOlustur")
				ajaxIsTanimlamaListele  = request.POST.get("ajaxIsTanimlamaListele")
				ajaxIsTanimlamaDetay    = request.POST.get("ajaxIsTanimlamaDetay")
				ajaxIsTanimlamaGuncelle = request.POST.get("ajaxIsTanimlamaGuncelle")			
				ajaxIsTanimlamaSil	    = request.POST.get("ajaxIsTanimlamaSil")

				if(ajaxKullaniciTipi):
					sqlKullaniciTanimlamalari = KullaniciTipiModel()
					sqlKullaniciTanimlamalari.KullaniciTipiKodu = ajaxKullaniciTipiKodu
					sqlKullaniciTanimlamalari.KullaniciTipi     = ajaxKullaniciTipi
					sqlKullaniciTanimlamalari.save()

					sqlModulYetkileri =  ModulYetkileri()
					sqlModulYetkileri.KullaniciTipiKodu  = ajaxKullaniciTipiKodu
					sqlModulYetkileri.IsAnaSayfa         = ajaxIsAnaSayfa
					sqlModulYetkileri.IsKullanicilar     = ajaxIsKullanicilar
					sqlModulYetkileri.IsPersoneller      = ajaxIsPersoneller
					sqlModulYetkileri.IsHareketler 		 = ajaxIsHareketler
					sqlModulYetkileri.IsTanimlamalar     = ajaxIsTanimlamalar		
					sqlModulYetkileri.save()

					sqlKullanicilarYetkileri = KullaniciYetkileri()
					sqlKullanicilarYetkileri.KullaniciTipiKodu   = ajaxKullaniciTipiKodu
					sqlKullanicilarYetkileri.IsKullaniciOlustur  = ajaxIsKullaniciOlustur
					sqlKullanicilarYetkileri.IsKullaniciListele  = ajaxIsKullaniciListele
					sqlKullanicilarYetkileri.IsKullaniciDetay    = ajaxIsKullaniciDetay
					sqlKullanicilarYetkileri.IsKullaniciGuncelle = ajaxIsKullaniciGuncelle
					sqlKullanicilarYetkileri.IsKullaniciSil      = ajaxIsKullaniciSil
					sqlKullanicilarYetkileri.save()

					sqlAnasayfaYetkileri = AnasayfaYetkileri()
					sqlAnasayfaYetkileri.KullaniciTipiKodu     = ajaxKullaniciTipiKodu
					sqlAnasayfaYetkileri.IsDuyuruOlustur       = ajaxIsDuyuruOlustur
					sqlAnasayfaYetkileri.IsGorevOlustur        = ajaxIsGorevOlustur
					sqlAnasayfaYetkileri.IsHatirlatmaOlustur   = ajaxIsHatirlatmaOlustur
					sqlAnasayfaYetkileri.IsDuyuruGoruntule     = ajaxIsDuyuruGoruntule
					sqlAnasayfaYetkileri.IsGorevGoruntule      = ajaxIsGorevGoruntule
					sqlAnasayfaYetkileri.IsHatirlatmaGoruntule = ajaxIsHatirlatmaGoruntule
					sqlAnasayfaYetkileri.save()	

					sqlPersonelYetkileri = PersonelYetkileri()
					sqlPersonelYetkileri.KullaniciTipiKodu  = ajaxKullaniciTipiKodu
					sqlPersonelYetkileri.IsPersonelOlustur  = ajaxIsPersonelOlustur
					sqlPersonelYetkileri.IsPersonelListele  = ajaxIsPersonelListele
					sqlPersonelYetkileri.IsPersonelDetay    = ajaxIsPersonelDetay
					sqlPersonelYetkileri.IsPersonelGuncelle = ajaxIsPersonelGuncelle
					sqlPersonelYetkileri.IsPersonelSil      = ajaxIsPersonelSil
					sqlPersonelYetkileri.save()

					sqlHareketYetkileri = HareketYetkileri()
					sqlHareketYetkileri.KullaniciTipiKodu = ajaxKullaniciTipiKodu
					sqlHareketYetkileri.IsHareketOlustur  = ajaxIsHareketOlustur
					sqlHareketYetkileri.IsHareketListele  = ajaxIsHareketListele
					sqlHareketYetkileri.IsHareketDetay    = ajaxIsHareketDetay
					sqlHareketYetkileri.IsHareketGuncelle = ajaxIsHareketGuncelle
					sqlHareketYetkileri.IsHareketSil      = ajaxIsHareketSil
					sqlHareketYetkileri.save()

					sqlTanimlamaYetkileri = TanimlamaYetkileri()
					sqlTanimlamaYetkileri.KullaniciTipiKodu   = ajaxKullaniciTipiKodu
					sqlTanimlamaYetkileri.IsTanimlamaOlustur  = ajaxIsTanimlamaOlustur
					sqlTanimlamaYetkileri.IsTanimlamaListele  = ajaxIsTanimlamaListele
					sqlTanimlamaYetkileri.IsTanimlamaDetay    = ajaxIsTanimlamaDetay
					sqlTanimlamaYetkileri.IsTanimlamaGuncelle = ajaxIsTanimlamaGuncelle
					sqlTanimlamaYetkileri.IsTanimlamaSil      = ajaxIsTanimlamaSil
					sqlTanimlamaYetkileri.save()

					context = {"ajaxMesaj" : "Kayıt Başarılı !",}
					return JsonResponse(context)
				
			varKullaniciTipiModel = KullaniciTipiModel.objects.all()
			varKullaniciGrubuModel = KullaniciGrubuModel.objects.all()
			
			context = {
				"modulYetkisi"           : modulYetkisi,
				"varKullaniciTipiModel"  : varKullaniciTipiModel,
				"varKullaniciGrubuModel" : varKullaniciGrubuModel,
			}		
			return render (request, "kullanicilar/tanimlamalar.html", context)	
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")		