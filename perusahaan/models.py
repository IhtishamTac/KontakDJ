from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class KategoriPerusahaan(models.TextChoices):
        Pemerintahan = 'Pem', _('Pemerintahan')
        Negeri = 'Neg', _('Negeri')

class BidangPerusahaan(models.TextChoices):
        PerusahaanEkstraktif = 'PE', _('Perusahaan Ekstraktif')
        PerusahaanAgraris = 'PA', _('Perusahaan Agraris')
        PerusahaanDagang = 'PD', _('Perusahaan Dagang')
        PerusahaanJasa = 'PJ', _('Perusahaan Jasa')
        PerusahaanIndustri = 'PI', _('Perusahaan Industri')

class JabatanPerusahaan(models.TextChoices):
        CEO = 'CEO', _('CEO')
        KabagTU = 'KBTU', _('Kabag TU')
        
class perusahaan(models.Model):
    nama = models.CharField(max_length=50)
    kategori = models.CharField(
        max_length=3,
        choices=KategoriPerusahaan.choices,
        default='',
    )
    bidang = models.CharField(
        max_length=2,
        choices=BidangPerusahaan.choices,
        blank=True,
        null=True,
    )
    alamat = models.TextField()
    nama_pic = models.CharField(max_length=254, blank=True, null=True)
    jabatan = models.CharField(
        max_length=4,
        choices=JabatanPerusahaan.choices,
        blank=True,
        null=True,
    )
    no_tlp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    #default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="perusahaan_created_by", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.nama