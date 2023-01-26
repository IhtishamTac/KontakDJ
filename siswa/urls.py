from django.urls import include, path

from siswa import views

urlpatterns = [
    path('', views.siswa, name='siswa'),
]
