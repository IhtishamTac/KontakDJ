from django.contrib import admin
from .models import siswa


# Register your models here.
class dataSiswa(admin.ModelAdmin):
    list_display = ['id', 'nisn', 'nama', 'jenis_kelamin', 'sekolah', 'no_tlp', 'email', 'alamat','tempat_lahir', 'tanggal_lahir', 'created_by', 'created_at', 'updated_at' ]

admin.site.register(siswa,dataSiswa)