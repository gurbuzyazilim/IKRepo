from django.db import models


class Kullanicilar(models.Model):
	KullaniciKodu 	 = models.CharField(max_length=10)
	KullaniciAdi 	 = models.CharField(max_length=50)
	KullaniciParola  = models.CharField(max_length=100)
	KullaniciTipi    = models.CharField(max_length=50)
	KullaniciGrubu   = models.CharField(max_length=50, null=True)
	KullaniciDurumu	 = models.BooleanField(default=False)
	SonGiris 		 = models.DateTimeField(null=True)
	KayitTarihi 	 = models.DateTimeField(null=True)
	KayitYapan		 = models.CharField(max_length=50,null=True)
	DuzeltmeTarihi 	 = models.DateTimeField(null=True)
	DuzeltmeYapan	 = models.CharField(max_length=50,null=True)
	IsSaved 		 = models.BooleanField(default=False)
	IsVerified		 = models.BooleanField(default=False)
	IsDeleted		 = models.BooleanField(default=False)
	IsCanceled       = models.BooleanField(default=False)
	IsTransferred	 = models.BooleanField(default=False)
	IsTransferCache	 = models.BooleanField(default=False)

	def __str__(self):
		return self.KullaniciKodu

class KullaniciTipiModel(models.Model):
	KullaniciTipiKodu  = models.CharField(max_length=10)
	KullaniciTipi      = models.CharField(max_length=50)

class KullaniciGrubuModel(models.Model):
	KullaniciGrubuKodu = models.CharField(max_length=10)
	KullaniciGrubu     = models.CharField(max_length=50)	

class ModulYetkileri(models.Model):
	KullaniciTipiKodu  = models.CharField(max_length=10)
	IsAnaSayfa	       = models.BooleanField(default=True)
	IsKullanicilar     = models.BooleanField(default=False)
	IsPersoneller      = models.BooleanField(default=False)
	IsHareketler       = models.BooleanField(default=False)
	IsTanimlamalar     = models.BooleanField(default=False)

class AnasayfaYetkileri(models.Model):
	KullaniciTipiKodu 	  = models.CharField(max_length=10)
	IsDuyuruOlustur       = models.BooleanField(default=False)
	IsGorevOlustur        = models.BooleanField(default=False)
	IsHatirlatmaOlustur   = models.BooleanField(default=False)
	IsDuyuruGoruntule     = models.BooleanField(default=False)
	IsGorevGoruntule      = models.BooleanField(default=False)
	IsHatirlatmaGoruntule = models.BooleanField(default=False)

class KullaniciYetkileri(models.Model):
	KullaniciTipiKodu 	= models.CharField(max_length=10)
	IsKullaniciOlustur  = models.BooleanField(default=False)
	IsKullaniciListele  = models.BooleanField(default=False)
	IsKullaniciDetay    = models.BooleanField(default=False)
	IsKullaniciGuncelle = models.BooleanField(default=False)
	IsKullaniciSil      = models.BooleanField(default=False)		

class PersonelYetkileri(models.Model):
	KullaniciTipiKodu  = models.CharField(max_length=10)
	IsPersonelOlustur  = models.BooleanField(default=False)
	IsPersonelListele  = models.BooleanField(default=False)
	IsPersonelDetay    = models.BooleanField(default=False)
	IsPersonelGuncelle = models.BooleanField(default=False)
	IsPersonelSil      = models.BooleanField(default=False)

class HareketYetkileri(models.Model):
	KullaniciTipiKodu = models.CharField(max_length=10)
	IsHareketOlustur  = models.BooleanField(default=False)
	IsHareketListele  = models.BooleanField(default=False)
	IsHareketDetay    = models.BooleanField(default=False)
	IsHareketGuncelle = models.BooleanField(default=False)
	IsHareketSil      = models.BooleanField(default=False)

class TanimlamaYetkileri(models.Model):
	KullaniciTipiKodu   = models.CharField(max_length=10)
	IsTanimlamaOlustur  = models.BooleanField(default=False)
	IsTanimlamaListele  = models.BooleanField(default=False)
	IsTanimlamaDetay    = models.BooleanField(default=False)
	IsTanimlamaGuncelle = models.BooleanField(default=False)
	IsTanimlamaSil      = models.BooleanField(default=False)