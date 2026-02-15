from django.urls import path
from . import views

urlpatterns = [
    # ===============================
    # DASHBOARD
    # ===============================
    path('', views.dashboard, name='dashboard'),

    # ===============================
    # KIB A - TANAH
    # ===============================
    path('tanah/', views.tanah_list, name='tanah_list'),
    path('tanah/tambah/', views.tanah_tambah, name='tanah_tambah'),
    path('tanah/<int:pk>/edit/', views.tanah_edit, name='tanah_edit'),
    path('tanah/<int:pk>/hapus/', views.tanah_hapus, name='tanah_hapus'),
    path('tanah/cetak/pdf/', views.tanah_cetak_pdf, name='tanah_cetak_pdf'),

    # ===============================
    # KIB B - PERALATAN & MESIN
    # ===============================
    path('peralatan/', views.peralatan_list, name='peralatan_list'),
    path('peralatan/tambah/', views.peralatan_tambah, name='peralatan_tambah'),
    path('peralatan/<int:id>/edit/', views.peralatan_edit, name='peralatan_edit'),
    path('peralatan/<int:id>/hapus/', views.peralatan_hapus, name='peralatan_hapus'),   
    path('peralatan/rekap/', views.peralatan_rekap, name='peralatan_rekap'),
    path('peralatan/import/', views.peralatan_import, name='peralatan_import'),
    path('peralatan/export/excel/', views.peralatan_export_excel, name='peralatan_export_excel'),
    path('peralatan/cetak/pdf/', views.peralatan_cetak_pdf, name='peralatan_cetak_pdf'),


    #peminjamanan alat
    #=============================================================================

    path('peminjaman/', views.peminjaman_list, name='peminjaman_list'),
    path('peminjaman/tambah/', views.peminjaman_create, name='peminjaman_create'),

    path('peminjaman/kembali/<int:id>/', views.peminjaman_kembali, name='peminjaman_kembali'),
    path('pengembalian/', views.pengembalian_list, name='pengembalian_list'),

#===============================
# Cetak Surat Peminjaman
#===============================

path(
    'peminjaman/cetak/<int:id>/',
    views.cetak_surat_peminjaman,
    name='cetak_surat_peminjaman'
),

    # ===============================
    # KIB C - GEDUNG & BANGUNAN
    # ===============================
    path('gedung/', views.gedung_list, name='gedung_list'),
    path('gedung/tambah/', views.gedung_tambah, name='gedung_tambah'),
    path('gedung/<int:pk>/edit/', views.gedung_edit, name='gedung_edit'),
    path('gedung/<int:pk>/hapus/', views.gedung_hapus, name='gedung_hapus'),
    path('gedung/cetak/pdf/', views.gedung_cetak_pdf, name='gedung_cetak_pdf'),

    #-------------------------
    #ruangan
    path('aset-per-ruangan/', views.aset_per_ruangan, name='aset_per_ruangan'),

    path('ruangan/', views.ruangan_list, name='ruangan_list'),
    path('ruangan/tambah/', views.ruangan_tambah, name='ruangan_tambah'),
    path('ruangan/edit/<int:pk>/', views.ruangan_edit, name='ruangan_edit'),
    path('ruangan/hapus/<int:pk>/', views.ruangan_hapus, name='ruangan_hapus'),


    # ===============================
    # KIB D - JALAN, IRIGASI & JARINGAN
    # ===============================
    path('jalan/', views.jalan_list, name='jalan_list'),
    path('jalan/tambah/', views.jalan_tambah, name='jalan_tambah'),
    path('jalan/<int:pk>/edit/', views.jalan_edit, name='jalan_edit'),
    path('jalan/<int:pk>/hapus/', views.jalan_hapus, name='jalan_hapus'),
    path('jalan/cetak/pdf/', views.jalan_cetak_pdf, name='jalan_cetak_pdf'),


    # ===============================
    # KIB E - BUKU
    # ===============================
    path('buku/', views.buku_list, name='buku_list'),
    path('buku/tambah/', views.buku_tambah, name='buku_tambah'),
    path('buku/<int:pk>/edit/', views.buku_edit, name='buku_edit'),
    path('buku/<int:pk>/hapus/', views.buku_hapus, name='buku_hapus'),
    path('buku/import/', views.buku_import, name='buku_import'),
    path('buku/export/excel/', views.buku_export_excel, name='buku_export_excel'),
    path('buku/cetak/pdf/', views.buku_cetak_pdf, name='buku_cetak_pdf'),
    path('buku/rekap/', views.buku_rekap, name='buku_rekap'),
    


#==================================
#cetak semua kib PDF
#==================================
path('cetak/semua-kib/', views.semua_kib_cetak_pdf, name='semua_kib_cetak_pdf'),


#====================================================================
# barang Habis pakai
#====================================================================

 path('bhp/', views.bhp_list, name='bhp_list'),
 path('bhp/tambah/', views.bhp_tambah, name='bhp_tambah'),
 path('bhp/masuk/', views.bhp_masuk, name='bhp_masuk'),
 path('bhp/keluar/', views.bhp_keluar, name='bhp_keluar'),

 path('bhp/', views.bhp_list, name='bhp_list'),
 path('bhp/import/', views.bhp_import, name='bhp_import'),

 path('bhp/transaksi/', views.bhp_transaksi, name='bhp_transaksi'),
 path('bhp/transaksi/pdf/', views.bhp_transaksi_pdf, name='bhp_transaksi_pdf'),
 path('bhp/<int:barang_id>/riwayat/',views.bhp_barang_riwayat, name='bhp_barang_riwayat'),

 path('ruangan/<int:id>/cetak/', views.cetak_kir, name='cetak_kir'),






]

