from kullanicilar.views import *
from kullanicilar.models import *
from personel.models_personel import *
from personel.models_tanimlamalar import *
from personel.models_hareketler import *
from django.shortcuts import render
from kullanicilar.encryption import encryption_h
from django.utils import timezone
from django.http import JsonResponse

def BordroOlustur(request):
	try:
		kullaniciKontrol = get_object_or_404(Kullanicilar,KullaniciKodu=request.session["KullaniciKodu"],KullaniciDurumu=True)
		modulYetkisi = get_object_or_404(ModulYetkileri,KullaniciTipiKodu=kullaniciKontrol.KullaniciTipi)
		if(modulYetkisi.IsPersoneller == True):
			if request.is_ajax():
				ajaxPersonel	 = request.POST.get("ajaxPersonel")
				if(ajaxPersonel != None):
					toplamBrutTutar	= 0
					sqlPersonel = get_object_or_404(Personel,id=ajaxPersonel)
					try:
						sqlMesaiTipi = get_object_or_404(TanimlamaMesaiTipleri,Kodu=sqlPersonel.MesaiTipi)
						mesaiSuresi = str(sqlMesaiTipi.Deger)
					except:
						mesaiSuresi = 0
					try:
						yardimlar = []
						for sqlHareketYardimlar in HareketYardimlar.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							sqlTanimlamaYardimlar = TanimlamaYardimlar.objects.filter(Kodu=sqlHareketYardimlar.YardimKodu)
							yardimlistesi = []
							for i in sqlTanimlamaYardimlar:
								toplamBrutTutar	= toplamBrutTutar + i.Deger
								yardim = "\
									<tr>\
					 					<th>"+i.Icerik+"</th>\
						 				<td>"+str(i.Deger)+"</td>\
									</tr>\
								"
								yardimlistesi.append(yardim)
							yardimlar.append(yardimlistesi)
					except:
						yardimlar = []
					try:
						avans = 0
						for sqlHareketAvanslar in HareketlerAvanslar.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							#sqlTanimlamaAvanslar = get_object_or_404(TanimlamaAvanslar,Kodu=sqlHareketAvanslar.AvansTuru)
							#"+sqlTanimlamaAvanslar.Icerik+"
							avans = avans + sqlHareketAvanslar.AvansMiktari
							
						avanslar = "\
							<tr>\
			 					<th>Avans</th>\
				 				<td>"+str(avans)+"</td>\
							</tr>\
						"
					except:
						avanslar = ""
					try:
						prim = 0
						for sqlHareketPrimler in HareketPrimler.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							#sqlTanimlamaPrimler = get_object_or_404(TanimlamaPrimler,Kodu=sqlHareketPrimler.PrimTuru)
							prim = prim + sqlHareketPrimler.PrimMiktari
							toplamBrutTutar	= toplamBrutTutar + sqlHareketPrimler.PrimMiktari
						primler = "\
							<tr>\
			 					<th>Prim</th>\
				 				<td>"+str(prim)+"</td>\
							</tr>\
						"
					except:
						primler = ""
					try:
						ikramiye = 0
						for sqlHareketIkramiyeler in HareketlerIkramiyeler.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							#sqlTanimlamaIkramiyeler = get_object_or_404(TanimlamaIkramiyeler,Kodu=sqlHareketIkramiyeler.IkramiyeTuru)
							ikramiye = ikramiye + sqlHareketIkramiyeler.IkramiyeMiktari
							toplamBrutTutar	= toplamBrutTutar + sqlHareketIkramiyeler.IkramiyeMiktari
						ikramiyeler = "\
							<tr>\
			 					<th>İkramiye</th>\
				 				<td>"+str(ikramiye)+"</td>\
							</tr>\
						"
					except:
						ikramiyeler = ""

					try:
						kesinti = 0
						for sqlHareketKesintiler in HareketKesintiler.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							#sqlTanimlamaKesintiler = get_object_or_404(TanimlamaKesintiler,Kodu=sqlHareketKesintiler.KesintiTuru)
							kesinti = kesinti + sqlHareketKesintiler.KesintiMiktari
							toplamBrutTutar	= toplamBrutTutar - sqlHareketKesintiler.KesintiMiktari
							
						kesintiler = "\
							<tr>\
			 					<th>Kesinti</th>\
				 				<td>"+str(kesinti)+"</td>\
							</tr>\
						"
					except:
						kesintiler = ""
						
					try:
						sqlMaasTipi         = get_object_or_404(TanimlamaMaasTipleri,Kodu=sqlPersonel.UcretTipi)
						toplamBrutTutar	    = toplamBrutTutar + sqlMaasTipi.Deger
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
							for sqlAileBilgileri in HareketAileBilgileri.objects.filter(PersonelKodu=sqlPersonel.Kodu):
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
						agi = agiYillikBrut * (0.50 + esi + cocugu) * 0.15 / 12
						#netTutar = agiHaricNetTutar + agi
						agiTutar = "\
							<tr>\
			 					<th>Asgari Geçim İndirimi</th>\
				 				<td>"+str(agi)+"</td>\
							</tr>\
						"
					except:
						agiTutar = ""
					
					try:
						fazlaMesaiSaati = 0
						fazlaMesaiUcreti = 0
						for sqlHareketFazlaMesailer in HareketFazlaMesailer.objects.filter(PersonelKodu=sqlPersonel.Kodu):
							#sqlTanimlamaFazlaMesailer = get_object_or_404(TanimlamaFazlaMesailer,Kodu=sqlHareketFazlaMesailer.MesaiTuru)
							fazlaMesaiSaati = fazlaMesaiSaati + float(sqlHareketFazlaMesailer.Saati)
							fazlaMesaiUcreti = fazlaMesaiUcreti + float(sqlHareketFazlaMesailer.MesaiUcreti)
							toplamBrutTutar	= float(toplamBrutTutar) + float(sqlHareketFazlaMesailer.MesaiUcreti)
						fazlaMesaiSaatleri = "\
			 				<th>Fazla Mesai Saati</th>\
				 			<td>"+str(fazlaMesaiSaati)+"</td>\
						"
						fazlaMesaiTutarlari = "\
							<tr>\
			 					<th>Fazla Mesai Tutari</th>\
				 				<td>"+str(fazlaMesaiUcreti)+"</td>\
							</tr>\
						"
					except:
						fazlaMesaiSaatleri  = ""
						fazlaMesaiTutarlari = ""
					try:
						if sqlPersonel.OzurDerecesi == "1":
							indirim = 1200 * 0.15
						elif sqlPersonel.OzurDerecesi == "2":
							indirim = 650 * 0.15
						elif sqlPersonel.OzurDerecesi == "3":
							indirim = 290 * 0.15
						#toplamBrutTutar	= toplamBrutTutar + indirim
						engelliIndirimi =  "\
							<tr>\
			 					<th>Engelli İndirimi</th>\
				 				<td>"+str(indirim)+"</td>\
							</tr>\
						"
					except:
						engelliIndirimi = ""
					try:
						sqkIsciKesK = "\
							<tr>\
			 					<th style='width: 19%;'>Sgk İşçi Kesintisi</th>\
				 				<td style='width: 20%;'>"+str(sgkIsciKes)+"</td>\
	 						</tr>\
						"	
						sqkIsvKesK = "\
							<tr>\
			 					<th>Sgk İşveren Kesintisi</th>\
				 				<td>"+str(sgkIsverenKes)+"</td>\
	 						</tr>\
						"	
						isIsciKesK = "\
							<tr>\
			 					<th>İşsizlik İşçi Kesintisi</th>\
				 				<td>"+str(issizlikIsciKes)+"</td>\
	 						</tr>\
						"	
						isIsvKesK = "\
							<tr>\
			 					<th>İşsizlik İşveren Kesintisi</th>\
				 				<td>"+str(issizlikIsverenKes)+"</td>\
	 						</tr>\
						"	
						gelirVerMatK = "\
							<tr>\
			 					<th>Gelir Vergisi Matrahı</th>\
				 				<td>"+str(gelirVergisiMatrahi)+"</td>\
	 						</tr>\
						"	
						gelirVerKesK = "\
							<tr>\
			 					<th>Gelir Vergisi Tutarı</th>\
				 				<td>"+str(gelirVergisiKes)+"</td>\
	 						</tr>\
						"
						damgaVerKesK = "\
							<tr>\
			 					<th>Damga Vergisi Tutarı</th>\
				 				<td>"+str(damgaVerKes)+"</td>\
	 						</tr>\
						"
					except:
						sqkIsciKesK  = ""
						sqkIsvKesK   = ""
						isIsciKesK   = ""
						isIsvKesK    = ""
						gelirVerMatK = ""
						gelirVerKesK = ""
						damgaVerKesK = ""
					brutUcret = "\
						<tr>\
		 					<th style='width: 19%;'>Brüt Ücret</th>\
			 				<td id='brutUcret' style='width: 20%;'>"+str(toplamBrutTutar)+"</td>\
 						</tr>\
 						"	
					context = {
						"ajaxYardimlar"           : yardimlar,
						"ajaxAvanslar"            : avanslar,
						"ajaxPrimler"             : primler,
						"ajaxIkramiyeler"         : ikramiyeler,
						"ajaxKesintiler"          : kesintiler,
						"ajaxFazlaMesaiSaatleri"  : fazlaMesaiSaatleri,
						"ajaxFazlaMesaiTutarlari" : fazlaMesaiTutarlari,
						"ajaxAgiTutar"            : agiTutar,
						"ajaxMesaiSuresi"         : str(mesaiSuresi),
						"ajaxBrutTutar"           : str(brutTutar),
						"ajaxSgkIsciKes"          : sqkIsciKesK,
						"ajaxSgkIsverenKes"       : sqkIsvKesK,
						"ajaxIssizlikIsciKes"     : isIsciKesK,
						"ajaxIssizlikIsverenKes"  : isIsvKesK,
						"ajaxGelirVergisiMatrahi" : gelirVerMatK,
						"ajaxGelirVergisiKes"     : gelirVerKesK,
						"ajaxDamgaVerKes"         : damgaVerKesK,
						"ajaxIseGirisTarihi"      : sqlPersonel.IseGirisTarihi,
						"ajaxMeslek"              : sqlPersonel.Meslek,
						"ajaxKimlikNo"            : sqlPersonel.KimlikNo, 
						"ajaxUcretTipi"           : sqlPersonel.UcretTipi,
						"ajaxUcret"               : str(sqlMaasTipi.Deger),
						"ajaxBrutUcret"           : brutUcret,
						"ajaxEngelliIndirimi"     : engelliIndirimi,
					}
					return JsonResponse(context)
							
			sqlPersoneller = Personel.objects.filter(IsDeleted=False)
			context = {
				"modulYetkisi"   : modulYetkisi,
				"suan"           : timezone.now(),
				"sqlPersoneller" : sqlPersoneller,
			}
			return render (request, "bordro/bordro.html",context)
		else:
			messages.success(request, "Bu Modüle Girmeye Yetkiniz Yok !")
			return redirect("kullanicilar:giris")
	except:
		messages.success(request, "Böyle Bir Kullanıcı Yok !")
		return redirect ("kullanicilar:giris")