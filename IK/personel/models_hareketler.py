from django.db import models

class HareketAdresler(models.Model):
	#----------------------- Varsayılan Kolonlar -----------------------
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu = models.CharField(max_length=10)
	AdresKodu    = models.CharField(max_length=10,null=True)
	KapiNo       = models.CharField(max_length=10,null=True)
	ApartmanNo   = models.CharField(max_length=10,null=True)   
	ApartmanAdi  = models.CharField(max_length=50,null=True)
	Sokak        = models.CharField(max_length=50,null=True)
	Cadde        = models.CharField(max_length=50,null=True)
	Mahalle      = models.CharField(max_length=50,null=True)
	Ilce         = models.CharField(max_length=50,null=True)
	Il           = models.CharField(max_length=50,null=True)
	Bolge        = models.CharField(max_length=50,null=True)
	Ulke         = models.CharField(max_length=50,null=True)
	PostaKodu    = models.CharField(max_length=50,null=True)
	Tel          = models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.AdresKodu

class HareketBankaHesaplari(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu = models.CharField(max_length=10)
	BankaKodu    = models.CharField(max_length=10)
	Iban         = models.CharField(max_length=20)
	HesapNo      = models.IntegerField()
	IsimSoyisim  = models.CharField(max_length=50)

	def __str__(self):
		return self.BankaKodu

class HareketDestekler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu    = models.CharField(max_length=10)
	DestekTuru      = models.CharField(max_length=20)
	Miktar          = models.DecimalField(max_digits=20,decimal_places=2)
	BaslangicTarihi = models.DateField()
	BitisTarihi     = models.DateField()

	def __str__(self):
		return self.DestekTuru

class HareketDigerKimlikler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu     = models.CharField(max_length=10)
	KimlikKodu       = models.CharField(max_length=10,null=True)
	BelgeNo          = models.CharField(max_length=10,null=True)
	TurSinif         = models.CharField(max_length=10,null=True)
	VerenMakam       = models.CharField(max_length=10,null=True)
	DuzenlemeTarihi  = models.DateField(null=True)
	GecerlilikTarihi = models.DateField(null=True)

	def __str__(self):
		return self.KimlikKodu

class HareketAileBilgileri(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu          = models.CharField(max_length=10)
	AileFerdiAdiSoyadi    = models.CharField(max_length=50,null=True)
	AileFerdiDogumTarihi  = models.DateField(null=True)
	AileFerdiTuru         = models.CharField(max_length=50,null=True)
	AileFerdiTelefon      = models.CharField(max_length=20,null=True)
	AileFerdiPersonelKodu = models.CharField(max_length=10,null=True)
	Calisiyor             = models.BooleanField(default=False)
	Meslek                = models.CharField(max_length=50,null=True)
 
	def __str__(self):
		return self.AileFerdiAdiSoyadi

class HareketVizeler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu        = models.CharField(max_length=10)
	VizeKodu            = models.CharField(max_length=10,null=True)
	VizeUlkeBolge       = models.CharField(max_length=50,null=True)
	VizeBelgeNo         = models.CharField(max_length=10,null=True)
	VizeBaslangicTarihi = models.DateField(null=True)
	VizeBitisTarihi     = models.DateField(null=True)

	def __str__(self):
		return self.VizeKodu		

class HareketDernekler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu         = models.CharField(max_length=10)
	DernekAdi            = models.CharField(max_length=100,null=True)
	DernekFaaliyetDetayi = models.CharField(max_length=150,null=True)
	UyeNo                = models.CharField(max_length=50,null=True)
	UyePozisyon          = models.CharField(max_length=50,null=True)
	UyelikTarihi         = models.DateField(null=True)

	def __str__(self):
		return self.DernekAdi

class HareketHukumlulukler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)	

	PersonelKodu          = models.CharField(max_length=10)
	CezaeviTuru           = models.CharField(max_length=50,null=True)
	CezaeviTipi           = models.CharField(max_length=50,null=True)
	IsnadEdilenFiil       = models.CharField(max_length=100,null=True)
	IsnadEdilenFiilDetayi = models.CharField(max_length=150,null=True)
	HapisSuresi           = models.CharField(max_length=50,null=True)
	HapishaneBaslangic    = models.DateField(null=True)
	HapishaneBitis        = models.DateField(null=True)
	TamamlananHapisSuresi = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.CezaeviTuru

class HareketMeslekler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu       = models.CharField(max_length=10)
	MeslekAdi          = models.CharField(max_length=50,null=True)
	MeslekDetayi       = models.CharField(max_length=100,null=True)
	Tecrubesi          = models.CharField(max_length=50,null=True)
	OkulKursKodu       = models.CharField(max_length=10,null=True)
	BelgeSertifikaKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.MeslekAdi

class HareketIsGecmisi(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu    = models.CharField(max_length=10)
	SirketAdi       = models.CharField(max_length=100,null=True)
	SirketUlke      = models.CharField(max_length=50,null=True)
	SirketSehir     = models.CharField(max_length=50,null=True)
	SirketTel       = models.CharField(max_length=50,null=True)
	CalismaTuru     = models.CharField(max_length=50,null=True)
	Departman       = models.CharField(max_length=50,null=True)
	Pozisyon        = models.CharField(max_length=50,null=True)
	BaslangicTarihi = models.DateField(null=True)
	BitisTarihi     = models.DateField(null=True)
	AyrilikSebebi   = models.CharField(max_length=150,null=True)

	def __str__(self):
		return self.SirketAdi

class HareketOkullarKurslar(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)	

	PersonelKodu    = models.CharField(max_length=10)
	OkulKursAdi     = models.CharField(max_length=10,null=True)
	Ulke            = models.CharField(max_length=50,null=True)
	Sehir           = models.CharField(max_length=50,null=True)
	BolumAdi        = models.CharField(max_length=50,null=True)
	BaslangicTarihi = models.DateField(null=True)
	BitisTarihi     = models.DateField(null=True)
	BelgeAdi        = models.CharField(max_length=50,null=True)
	BelgeTuru       = models.CharField(max_length=50,null=True)
	BelgeTarihi     = models.DateField(null=True)
	BelgeKaynak     = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.OkulKursAdi

class HareketNitelikler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu     = models.CharField(max_length=10)
	NitelikKodu      = models.CharField(max_length=10,null=True)
	NitelikTecrubesi = models.CharField(max_length=10,null=True)
	NitelikSeviyesi  = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.NitelikKodu

class HareketDiller(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)	

	PersonelKodu       = models.CharField(max_length=10)
	DilKodu            = models.CharField(max_length=10,null=True)
	OgrenimTuru        = models.CharField(max_length=50,null=True)
	OkumaSeviyesi      = models.CharField(max_length=50,null=True)
	YazmaSeviyesi      = models.CharField(max_length=50,null=True)
	KonusmaSeviyesi    = models.CharField(max_length=50,null=True)
	OkulKursKodu       = models.CharField(max_length=50,null=True)
	BelgeSertifikaKodu = models.CharField(max_length=50,null=True)
 
	def __str__(self):
		return self.DilKodu

class HareketFazlaMesailer(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu  = models.CharField(max_length=10)
	MesaiTuru     = models.CharField(max_length=10)
	MesaiTarihi   = models.DateField()
	SaatAraligi1  = models.TimeField()
	SaatAraligi2  = models.TimeField()
	Saati         = models.CharField(max_length=3)
	ArttirimOrani = models.DecimalField(max_digits=10,decimal_places=2)
	MesaiUcreti   = models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.MesaiTuru

class HareketGorevler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu     = models.CharField(max_length=10)
	GorevKodu        = models.CharField(max_length=10,null=True)
	DepartmanKodu    = models.CharField(max_length=10,null=True)
	GorevAmiriKodu   = models.CharField(max_length=10,null=True)
	BaslangicTarihi  = models.DateField(null=True)
	BitisTarihi      = models.DateField(null=True)
	GorevSonuc       = models.CharField(max_length=50,null=True)
	GorevSonucDetayi = models.CharField(max_length=150,null=True)

	def __str__(self):
		return self.GorevKodu		

class HareketPerformanslar(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu             = models.CharField(max_length=10)
	PerformansKodu           = models.CharField(max_length=10,null=True)
	DegerlendirmeyiYapan     = models.CharField(max_length=10,null=True)
	PerformansPeriyodu       = models.CharField(max_length=20,null=True)
	DegerlendirmePuani       = models.CharField(max_length=50,null=True)
	DegerlendirmePuaniDetayi = models.CharField(max_length=150,null=True)

	def __str__(self):
		return self.PerformansKodu		

class HareketYardimlar(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	YardimKodu        = models.CharField(max_length=10,null=True)
	YardimTarihi      = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.YardimKodu	

class HareketIzinler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	IzinTuru          = models.CharField(max_length=50,null=True)
	IzinSebebi        = models.CharField(max_length=150,null=True)
	BaslangicTarihi   = models.DateField(null=True)
	BitisTarihi       = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)
 
	def __str__(self):
		return self.IzinTuru

class HareketlerAvanslar(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	AvansTuru         = models.CharField(max_length=50,null=True)
	AvansSebebi       = models.CharField(max_length=150,null=True)
	AvansMiktari      = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	AvansTarihi       = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.AvansTuru
	
class HareketPrimler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	PrimTuru          = models.CharField(max_length=50,null=True)
	PrimSebebi        = models.CharField(max_length=150,null=True)
	PrimMiktari       = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	PrimTarihi        = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.PrimTuru	

class HareketTahakkuklar(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	TahakkukTuru      = models.CharField(max_length=50,null=True)
	TahakkukSebebi    = models.CharField(max_length=150,null=True)
	TahakkukMiktari   = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	TahakkukTarihi    = models.DateField(null=True)
	TahakkukPeriyodu  = models.CharField(max_length=50,null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.TahakkukTuru	

class HareketlerIkramiyeler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	IkramiyeTuru      = models.CharField(max_length=50,null=True)
	IkramiyeSebebi    = models.CharField(max_length=150,null=True)
	IkramiyeMiktari   = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	IkramiyeTarihi    = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.IkramiyeTuru		

class HareketKesintiler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	KesintiTuru       = models.CharField(max_length=50,null=True)
	KesintiSebebi     = models.CharField(max_length=150,null=True)
	KesintiMiktari    = models.DecimalField(max_digits=20,decimal_places=2,null=True) #Kesinti Miktarı
	KesintiTarihi     = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10)

	def __str__(self):
		return self.KesintiTuru

class HareketZimmetler(models.Model):
	IsSaved    = models.BooleanField(default=False)
	IsVerified = models.BooleanField(default=False)
	IsDeleted  = models.BooleanField(default=False)
	IsCanceled = models.BooleanField(default=False)
	IsActive   = models.BooleanField(default=False)
	IsHidden   = models.BooleanField(default=False)
	CreateUser = models.CharField(max_length=50)
	CreateDate = models.DateTimeField()
	LastUpUser = models.CharField(max_length=50,null=True)
	LastUpDate = models.DateTimeField(null=True)

	PersonelKodu      = models.CharField(max_length=10)
	Kategori          = models.CharField(max_length=50)
	Marka             = models.CharField(max_length=50)
	Model             = models.CharField(max_length=50)
	Miktar            = models.DecimalField(max_digits=20,decimal_places=2,null=True)
	AlanKisi          = models.CharField(max_length=100)
	VerenKisi         = models.CharField(max_length=100)
	Aciklama1         = models.CharField(max_length=100,null=True)
	Aciklama2         = models.CharField(max_length=100,null=True)
	Aciklama3         = models.CharField(max_length=100,null=True)
	BaslangicTarihi   = models.DateField()
	BitisTarihi       = models.DateField(null=True)
	MuhasebeIslemKodu = models.CharField(max_length=10)

	def __str__(self):
		return self.Kategori