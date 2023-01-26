from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class StatusSekolah(models.TextChoices):
        NEGERI = 'NGR', _('Negeri')
        SWASTA = 'SWST', _('Swasta')


class sekolah(models.Model):
    npsn = models.CharField(max_length=20, default='')
    nama = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=254, blank=True, null=True, default='')
    alamat = models.TextField(default='')
    provinsi = models.CharField(max_length=50, default='')
    kabupaten_kota = models.CharField(max_length=50, default='')
    kecamatan = models.CharField(max_length=50, default='')
    status = models.CharField(
        max_length=4,
        choices=StatusSekolah.choices,
        default=''
    )
    no_tlp = models.CharField(max_length=20, blank=True, null=True, default='')
    fax = models.CharField(max_length=20, default='')

    #default
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="sekolah_created_by", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.nama
