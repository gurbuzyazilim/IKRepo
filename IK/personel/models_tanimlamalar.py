from django.db import models

class TanimlamaAdresler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaAileFerdiTurleri(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaBankaHesaplari(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaDestekler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		

class TanimlamaGruplar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaIzinler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaPrimler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaTahakkuklar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaIkramiyeler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaKesintiler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu										

class TanimlamaDepartmanlar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaAvanslar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		

class TanimlamaNitelikler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaFazlaMesailer(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		

class TanimlamaPerformanslar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		

class TanimlamaBedenler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaBagimliliklar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaDiller(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaGorevler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaBasvuruPuanlari(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaYetkiler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaDigerKimlikler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaTasimaTipleri(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaDovizler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		

class TanimlamaYardimlar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		


class TanimlamaMaasTipleri(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu	

class TanimlamaVizeler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu
	
class TanimlamaYemekKartlari(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50,null=True)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu	

class TanimlamaOkullarKurslar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu	

class TanimlamaSertifikalar(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu		
		
class TanimlamaMesaiTipleri(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu

class TanimlamaZimmetler(models.Model):
	Kodu   = models.CharField(max_length=10)
	Icerik = models.CharField(max_length=50)
	Deger  = models.DecimalField(max_digits=10,decimal_places=2,null=True)

	def __str__(self):
		return self.Kodu			