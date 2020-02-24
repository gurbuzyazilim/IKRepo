from kullanicilar.models import *
from .models_personel import *
from .models_tanimlamalar import *
from .models_hareketler import *
from .sehirler import *
from .meslekler import *
from .milletler import *
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone


def PersonelOlustur(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session["KullaniciKodu"],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsKullanicilar == True):
			islemlerKontrol = get_object_or_404(KullaniciYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
			if(islemlerKontrol.IsKullaniciOlustur == True):
				if request.is_ajax():
					ajaxArguman          = request.POST.get("ajaxArguman")
					ajaxArguman2         = request.POST.get("ajaxArguman2")
					ajaxKodu             = request.POST.get("ajaxKodu")
					ajaxIsim             = request.POST.get("ajaxIsim")
					ajaxSoyIsim          = request.POST.get("ajaxSoyIsim")
					ajaxEskiSoyisim      = request.POST.get("ajaxEskiSoyisim")
					ajaxOrjDilIsSoyisim  = request.POST.get("ajaxOrjDilIsSoyisim")
					ajaxTel1             = request.POST.get("ajaxTel1")
					ajaxTel2             = request.POST.get("ajaxTel2")
					ajaxTel3             = request.POST.get("ajaxTel3")
					ajaxEmail            = request.POST.get("ajaxEmail")
					ajaxKEP              = request.POST.get("ajaxKEP")
					ajaxAcilDurKisi1     = request.POST.get("ajaxAcilDurKisi1")
					ajaxAcilDurKisi1Tel  = request.POST.get("ajaxAcilDurKisi1Tel")
					ajaxAcilDurKisi2     = request.POST.get("ajaxAcilDurKisi2")
					ajaxAcilDurKisi2Tel  = request.POST.get("ajaxAcilDurKisi2Tel")
					ajaxReferansKisi1    = request.POST.get("ajaxReferansKisi1")
					ajaxReferansKisi1Tel = request.POST.get("ajaxReferansKisi1Tel")
					ajaxReferansKisi2    = request.POST.get("ajaxReferansKisi2")
					ajaxReferansKisi2Tel = request.POST.get("ajaxReferansKisi2Tel")
					ajaxKimlikNo         = request.POST.get("ajaxKimlikNo")
					ajaxUyruk            = request.POST.get("ajaxUyruk")
					ajaxCinsiyet         = request.POST.get("ajaxCinsiyet")
					ajaxMedeniHal        = request.POST.get("ajaxMedeniHal")
					ajaxKanGrubu         = request.POST.get("ajaxKanGrubu")
					ajaxDogumTarihi      = request.POST.get("ajaxDogumTarihi")
					ajaxDogumYeri        = request.POST.get("ajaxDogumYeri")
					ajaxKimlikteDin      = request.POST.get("ajaxKimlikteDin")
					ajaxKimlikSeriNo     = request.POST.get("ajaxKimlikSeriNo")
					ajaxIl               = request.POST.get("ajaxIl")
					ajaxIlce             = request.POST.get("ajaxIlce")
					ajaxMahalle          = request.POST.get("ajaxMahalle")
					ajaxKoy              = request.POST.get("ajaxKoy")
					ajaxCiltNo           = request.POST.get("ajaxCiltNo")
					ajaxSayfaNo          = request.POST.get("ajaxSayfaNo")
					ajaxKutukNo          = request.POST.get("ajaxKutukNo")
					ajaxVerilisNedeni    = request.POST.get("ajaxVerilisNedeni")
					ajaxKimlikKayitNo    = request.POST.get("ajaxKimlikKayitNo")
					ajaxOzelNot          = request.POST.get("ajaxOzelNot")
					ajaxMaasTipi         = request.POST.get("ajaxMaasTipi")
					ajaxDovizTipi        = request.POST.get("ajaxDovizTipi")
					ajaxDepartmanKodu    = request.POST.get("ajaxDepartmanKodu")
					ajaxGrupKodu         = request.POST.get("ajaxGrupKodu")
					ajaxIdariAmirKodu    = request.POST.get("ajaxIdariAmirKodu")
					ajaxTeknikAmirKodu   = request.POST.get("ajaxTeknikAmirKodu")
					ajaxMuhasebeKodu     = request.POST.get("ajaxMuhasebeKodu")
					ajaxSigortaKodu      = request.POST.get("ajaxSigortaKodu")
					ajaxSigortaBelgeTipi = request.POST.get("ajaxSigortaBelgeTipi")
					ajaxIseGirisTarihi   = request.POST.get("ajaxIseGirisTarihi")
					ajaxOgrenimDurumu    = request.POST.get("ajaxOgrenimDurumu")
					ajaxMeslek           = request.POST.get("ajaxMeslek")
					ajaxMevsim           = request.POST.get("ajaxMevsim")
					ajaxKapsam           = request.POST.get("ajaxKapsam")
					ajaxServisNo         = request.POST.get("ajaxServisNo")
					ajaxOzurDerecesi     = request.POST.get("ajaxOzurDerecesi")
					ajaxIzinGunu         = request.POST.get("ajaxIzinGunu")
					ajaxMesaiTipi        = request.POST.get("ajaxMesaiTipi")
					ajaxMesaiYapabilir   = request.POST.get("ajaxMesaiYapabilir")
					ajaxSeyehatEngeli    = request.POST.get("ajaxSeyehatEngeli")
					ajaxGeceVardiyasi    = request.POST.get("ajaxGeceVardiyasi")
					ajaxIbadetIzni       = request.POST.get("ajaxIbadetIzni")
					ajaxCikisTarihi      = request.POST.get("ajaxCikisTarihi")
					ajaxCikisNedeni      = request.POST.get("ajaxCikisNedeni")
					if(ajaxKodu != None):
						mesaiYapabilir = False
						if(ajaxMesaiYapabilir == "1"):
							mesaiYapabilir = True
						#else:
							#mesaiYapabilir = False
						geceVardiyasi = False
						if(ajaxGeceVardiyasi == "1"):
							geceVardiyasi = True
						#else:
							#geceVardiyasi = False
						ibadetIzni = False
						if(ajaxIbadetIzni == "1"):
							ibadetIzni = True
						#else:
							#ibadetIzni = False
						seyehatEngeli = False
						if(ajaxSeyehatEngeli == "1"):
							seyehatEngeli = True	
						#else:
							#seyehatEngeli = False
						if(ajaxArguman == "1"):
							sqlPersonelGuncelle = get_object_or_404(Personel,id=ajaxArguman2)
							sqlPersonelGuncelle.LastUpUser              = request.session["KullaniciKodu"]
							sqlPersonelGuncelle.LastUpDate              = timezone.now()
							sqlPersonelGuncelle.Kodu                    = ajaxKodu
							sqlPersonelGuncelle.Isim                    = ajaxIsim
							sqlPersonelGuncelle.Soyisim                 = ajaxSoyIsim
							sqlPersonelGuncelle.EskiSoyisim             = ajaxEskiSoyisim
							sqlPersonelGuncelle.OrjinalDildeIsimSoyisim = ajaxOrjDilIsSoyisim
							sqlPersonelGuncelle.KimlikNo                = ajaxKimlikNo
							sqlPersonelGuncelle.Uyruk                   = ajaxUyruk
							sqlPersonelGuncelle.Cinsiyet                = ajaxCinsiyet
							sqlPersonelGuncelle.MedeniHal               = ajaxMedeniHal
							sqlPersonelGuncelle.KanGrubu                = ajaxKanGrubu
							sqlPersonelGuncelle.DogumTarihi             = ajaxDogumTarihi
							sqlPersonelGuncelle.DogumYeri               = ajaxDogumYeri
							sqlPersonelGuncelle.KimlikteDin             = ajaxKimlikteDin
							sqlPersonelGuncelle.KimlikSeriNo            = ajaxKimlikSeriNo
							sqlPersonelGuncelle.Il                      = ajaxIl
							sqlPersonelGuncelle.Ilce                    = ajaxIlce
							sqlPersonelGuncelle.Mahalle                 = ajaxMahalle
							sqlPersonelGuncelle.Koy                     = ajaxKoy
							sqlPersonelGuncelle.CiltNo                  = ajaxCiltNo
							sqlPersonelGuncelle.SayfaNo                 = ajaxSayfaNo
							sqlPersonelGuncelle.KutukNo                 = ajaxKutukNo
							sqlPersonelGuncelle.VerilisNedeni           = ajaxVerilisNedeni
							sqlPersonelGuncelle.KayitNo                 = ajaxKimlikKayitNo
							sqlPersonelGuncelle.Tel1                    = ajaxTel1
							sqlPersonelGuncelle.Tel2                    = ajaxTel2
							sqlPersonelGuncelle.Tel3                    = ajaxTel3
							sqlPersonelGuncelle.Email                   = ajaxEmail
							sqlPersonelGuncelle.KEP                     = ajaxKEP
							sqlPersonelGuncelle.AcilDurumKisi1          = ajaxAcilDurKisi1
							sqlPersonelGuncelle.AcilDurumKisi1Tel       = ajaxAcilDurKisi1Tel
							sqlPersonelGuncelle.AcilDurumKisi2          = ajaxAcilDurKisi2
							sqlPersonelGuncelle.AcilDurumKisi2Tel       = ajaxAcilDurKisi2Tel
							sqlPersonelGuncelle.ReferansKisi1           = ajaxReferansKisi1
							sqlPersonelGuncelle.ReferansKisi1Tel        = ajaxReferansKisi1Tel
							sqlPersonelGuncelle.ReferansKisi2           = ajaxReferansKisi2
							sqlPersonelGuncelle.ReferansKisi2Tel        = ajaxReferansKisi2Tel
							sqlPersonelGuncelle.OzelNot                 = ajaxOzelNot
							sqlPersonelGuncelle.UcretTipi               = ajaxMaasTipi
							sqlPersonelGuncelle.DovizCinsi              = ajaxDovizTipi
							sqlPersonelGuncelle.ServisNo                = ajaxServisNo
							sqlPersonelGuncelle.OzurDerecesi            = ajaxOzurDerecesi
							sqlPersonelGuncelle.IzinGunu                = ajaxIzinGunu
							sqlPersonelGuncelle.SeyehatEngeli           = seyehatEngeli
							sqlPersonelGuncelle.MesaiYapabilir          = mesaiYapabilir
							sqlPersonelGuncelle.MesaiTipi               = ajaxMesaiTipi
							sqlPersonelGuncelle.GeceVardiyasi           = geceVardiyasi
							sqlPersonelGuncelle.IbadetIzni              = ibadetIzni
							sqlPersonelGuncelle.DepartmanKodu           = ajaxDepartmanKodu
							sqlPersonelGuncelle.GrupKodu                = ajaxGrupKodu
							sqlPersonelGuncelle.MuhasebeKodu            = ajaxMuhasebeKodu
							sqlPersonelGuncelle.IdariAmirKodu           = ajaxIdariAmirKodu
							sqlPersonelGuncelle.TeknikAmirKodu          = ajaxTeknikAmirKodu
							sqlPersonelGuncelle.SigortaKodu             = ajaxSigortaKodu
							sqlPersonelGuncelle.SigortaBelgeTuru        = ajaxSigortaBelgeTipi
							sqlPersonelGuncelle.Mevsim                  = ajaxMevsim
							sqlPersonelGuncelle.Kapsam                  = ajaxKapsam
							sqlPersonelGuncelle.IseGirisTarihi          = ajaxIseGirisTarihi
							sqlPersonelGuncelle.OgrenimDurumu           = ajaxOgrenimDurumu
							sqlPersonelGuncelle.Meslek                  = ajaxMeslek
							if(ajaxCikisTarihi != ""):
								sqlPersonelGuncelle.CikisTarihi         = ajaxCikisTarihi
							sqlPersonelGuncelle.CikisNedeni             = ajaxCikisNedeni
							sqlPersonelGuncelle.save()
						else:
							sqlPersonel = Personel()
							sqlPersonel.CreateUser              = request.session["KullaniciKodu"]
							sqlPersonel.CreateDate              = timezone.now()
							sqlPersonel.Kodu                    = ajaxKodu
							sqlPersonel.Isim                    = ajaxIsim
							sqlPersonel.Soyisim                 = ajaxSoyIsim
							sqlPersonel.EskiSoyisim             = ajaxEskiSoyisim
							sqlPersonel.OrjinalDildeIsimSoyisim = ajaxOrjDilIsSoyisim
							sqlPersonel.KimlikNo                = ajaxKimlikNo
							sqlPersonel.Uyruk                   = ajaxUyruk
							sqlPersonel.Cinsiyet                = ajaxCinsiyet
							sqlPersonel.MedeniHal               = ajaxMedeniHal
							sqlPersonel.KanGrubu                = ajaxKanGrubu
							sqlPersonel.DogumTarihi             = ajaxDogumTarihi
							sqlPersonel.DogumYeri               = ajaxDogumYeri
							sqlPersonel.KimlikteDin             = ajaxKimlikteDin
							sqlPersonel.KimlikSeriNo            = ajaxKimlikSeriNo
							sqlPersonel.Il                      = ajaxIl
							sqlPersonel.Ilce                    = ajaxIlce
							sqlPersonel.Mahalle                 = ajaxMahalle
							sqlPersonel.Koy                     = ajaxKoy
							sqlPersonel.CiltNo                  = ajaxCiltNo
							sqlPersonel.SayfaNo                 = ajaxSayfaNo
							sqlPersonel.KutukNo                 = ajaxKutukNo
							sqlPersonel.VerilisNedeni           = ajaxVerilisNedeni
							sqlPersonel.KayitNo                 = ajaxKimlikKayitNo
							sqlPersonel.Tel1                    = ajaxTel1
							sqlPersonel.Tel2                    = ajaxTel2
							sqlPersonel.Tel3                    = ajaxTel3
							sqlPersonel.Email                   = ajaxEmail
							sqlPersonel.KEP                     = ajaxKEP
							sqlPersonel.AcilDurumKisi1          = ajaxAcilDurKisi1
							sqlPersonel.AcilDurumKisi1Tel       = ajaxAcilDurKisi1Tel
							sqlPersonel.AcilDurumKisi2          = ajaxAcilDurKisi2
							sqlPersonel.AcilDurumKisi2Tel       = ajaxAcilDurKisi2Tel
							sqlPersonel.ReferansKisi1           = ajaxReferansKisi1
							sqlPersonel.ReferansKisi1Tel        = ajaxReferansKisi1Tel
							sqlPersonel.ReferansKisi2           = ajaxReferansKisi2
							sqlPersonel.ReferansKisi2Tel        = ajaxReferansKisi2Tel
							sqlPersonel.OzelNot                 = ajaxOzelNot
							sqlPersonel.UcretTipi               = ajaxMaasTipi
							sqlPersonel.DovizCinsi              = ajaxDovizTipi
							sqlPersonel.ServisNo                = ajaxServisNo
							sqlPersonel.OzurDerecesi            = ajaxOzurDerecesi
							sqlPersonel.IzinGunu                = ajaxIzinGunu
							sqlPersonel.SeyehatEngeli           = seyehatEngeli
							sqlPersonel.MesaiYapabilir          = mesaiYapabilir
							sqlPersonel.MesaiTipi               = ajaxMesaiTipi
							sqlPersonel.GeceVardiyasi           = geceVardiyasi
							sqlPersonel.IbadetIzni              = ibadetIzni
							sqlPersonel.DepartmanKodu           = ajaxDepartmanKodu
							sqlPersonel.GrupKodu                = ajaxGrupKodu
							sqlPersonel.MuhasebeKodu            = ajaxMuhasebeKodu
							sqlPersonel.IdariAmirKodu           = ajaxIdariAmirKodu
							sqlPersonel.TeknikAmirKodu          = ajaxTeknikAmirKodu
							sqlPersonel.SigortaKodu             = ajaxSigortaKodu
							sqlPersonel.SigortaBelgeTuru        = ajaxSigortaBelgeTipi
							sqlPersonel.Mevsim                  = ajaxMevsim
							sqlPersonel.Kapsam                  = ajaxKapsam
							sqlPersonel.IseGirisTarihi          = ajaxIseGirisTarihi
							sqlPersonel.OgrenimDurumu           = ajaxOgrenimDurumu
							sqlPersonel.Meslek                  = ajaxMeslek
							sqlPersonel.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					ajaxDetay = request.POST.get("ajaxDetay")
					if(ajaxDetay != None):
						sqlDetay = Personel.objects.values_list().get(id=ajaxDetay)
						personelListesi = []
						for i in sqlDetay[11:]:
							if(i == None):
								personelListesi.append("")
							elif(i == True):
								personelListesi.append("Evet")
							elif(i == False):
								personelListesi.append("Hayır")		
							else:
								personelListesi.append(i)
						personelBaslik = ["id","Kodu","İşe Giriş Tarihi","OgrenimDurumu","Meslek","Departman Kodu",\
							"Grup Kodu","Muhasebe Kodu","İdari Amir Kodu","Teknik Amir Kodu","Sigorta Kodu",\
							"Sigorta Belge Türü","Mevsim","Kapsam","Maaş Tipi","Döviz Cinsi","Servis Numarası",\
							"Özür Derecesi","İzin Günü","Seyehat Engeli","Mesai Yapabilir","Mesai Tipi",\
							"Gece Vardiyası","Nafile İbadet İzni","İşten Çıkış Tarihi","Çıkış Nedeni",\
							"İsim","Soyisim","Eski Soyisim","Orjinal Dilde İsim Soyisim","Kimlik Numarası",\
							"Uyruk","Cinsiyet","Medeni Hal","Kan Grubu","Kimlik Doğum Tarihi","Kimlik Doğum Yeri",\
							"Din","Kimlik Seri Numarası","İl","İlçe","Mahalle","Köy","Kimlik Cilt Numarası",\
							"Kimlik Sayfa Numarası","Kimlik Kütük No","Kimlik Veriliş Nedeni","Kimlik Kayıt Numarası",\
							"Tel1","Tel2","Tel3","Email","KEP","Acil Durum Kişi 1","Acil Durum Kişi 1 Telefon",\
							"Acil Durum Kişi 2","Acil Durum Kişi 2 Telefon","Referans Kişi 1","Referans Kişi 1 Telefon",\
							"Referans Kişi 2","Referans Kişi 2 Telefon","Özel Not"]
						context = {
							"ajaxPersonelListesi" : personelListesi,
							"ajaxPersonelBaslik"  : personelBaslik,
						}
						return JsonResponse(context)

					ajaxSil = request.POST.get("ajaxSil")
					if(ajaxSil != None):
						sqlPersonelSil = get_object_or_404(Personel,id=ajaxSil)
						sqlPersonelSil.IsDeleted = True
						sqlPersonelSil.save()
						context = {"ajaxMesaj" : "Başarılı"}
						return JsonResponse(context)
					ajaxGuncelle = request.POST.get("ajaxGuncelle")
					if(ajaxGuncelle != None):
						sqlPersonelGuncelle = Personel.objects.values_list().get(id=ajaxGuncelle)
						context = {"ajaxPerGunc" : sqlPersonelGuncelle}
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

				departmanlar   = TanimlamaDepartmanlar.objects.all()
				gruplar        = TanimlamaGruplar.objects.all()
				mesaiTipleri   = TanimlamaMesaiTipleri.objects.all()
				dovizler       = TanimlamaDovizler.objects.all()
				maasTipleri    = TanimlamaMaasTipleri.objects.all()
				tasimaTipleri  = TanimlamaTasimaTipleri.objects.all()		
				sqlPersoneller = Personel.objects.filter(IsDeleted=False)

				context = {
					"modulYetkisi"   : modulYetkisi,
					"suan"           : timezone.now(),
					"iller"          : iller,
					"sqlPersoneller" : sqlPersoneller,
					"mesaiTipleri"   : mesaiTipleri,
					"departmanlar"   : departmanlar,
					"gruplar"   	 : gruplar,
					"dovizler"       : dovizler,
					"maasTipleri"    : maasTipleri,
					"tasimaTipleri"  : tasimaTipleri,
					"meslekler"      : meslekler,
					"milletler"      : milletler,
				}
				return render (request, "personel/personel.html", context)
			else:		
				messages.success(request, "Kullanıcı Oluşturma Yetkiniz Yok !")
				return redirect("anasayfa")
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect("kullanicilar:giris")		