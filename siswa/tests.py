from django.test import TestCase
from django.urls import reverse

from .models import siswa
from sekolah.models import sekolah


# Create your tests here.

class ViewsSiswa(TestCase):
    def setUp(self):
        self.sekolah = sekolah.objects.create(
            id=1,
            npsn = '1241324',
            nama = 'SMKN 2 Sukabumi',
            email = 'sam@gmail.com',
            alamat = 'Jl. Sukabulan',
            provinsi = 'Jawa Barat',
            kabupaten_kota = 'Kota Sukabumi',
            kecamatan = 'Citamiang',
            status = 'Negeri',
            no_tlp = '08735288237',
            fax = '1253265',

        )
        self.siswa = siswa.objects.create(
            id=1,
            nisn="1247698",
            nama='Ihtisham Koernia',
            jenis_kelamin='Laki-Laki',
            sekolah_id=1,
            no_tlp='0832782368',
            email='sam@gmail.com',
            alamat='',
            tempat_lahir='Sukabumi, 2006',
            tanggal_lahir='2006-01-01',
        )


    def test_mengambil_semua_dasis_count(self):
        global siswa
        siswa = siswa.objects.all()
        sekolah = siswa[0].sekolah_id
        self.assertEqual(siswa.count(), 1)

    def test_update_email_siswa(self):
        global siswa
        siswa = siswa.objects.get(id=self.siswa.id)
        sekolah = siswa[0].sekolah_id
        siswa.email = 'ssam@gmail.com'
        siswa.save()
        updated_siswa = siswa.objects.get(id=self.siswa.id)
        self.assertEqual(updated_siswa.email, 'newemail@gmail.com')


    def test_hapus1_siswa(self):
        siswa_id = self.siswa.id
        sekolah_id = self.sekolah.id
        self.siswa.sekolah = None
        siswa.objects.get(id=siswa_id).delete()
        sekolah.objects.get(id=sekolah_id).delete()
        self.assertEqual(sekolah.objects.filter(id=sekolah_id).count(), 0)
        self.assertEqual(siswa.objects.filter(id=siswa_id).count(), 0)


    # def test_hapus_semua_siswa(self):
    #     siswa.objects.all().delete()
    #     self.assertEqual(siswa.objects.all().count(), 0)


    







    # def test_siswa_list_view(self):
    #     response = self.client.get(reverse('siswa_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'data_siswa.html')
    #     self.assertContains(response, 'siswa')

    # def test_siswa_create_view(self):
    #     response = self.client.post(reverse('siswa_create'), {
    #         'name': 'product3',
    #         'description': 'product3 description',
    #         'price': 30,
    #         'stock': 15
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('product_list'))
    #     self.assertEqual(Product.objects.count(), 3)
    #     self.assertEqual(Product.objects)