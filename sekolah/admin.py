from django.contrib import admin
from .models import sekolah

# Register your models here.
class namaSekolah(admin.ModelAdmin):
    list_display = ['npsn', 'nama',  'email', 'alamat', 'provinsi', 'kabupaten_kota', 'kecamatan', 'status', 'no_tlp', 'fax', 'created_by', 'updated_at' ]

admin.site.register(sekolah, namaSekolah)