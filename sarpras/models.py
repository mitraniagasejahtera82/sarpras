from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone


# =====================
# KIB A - TANAH
# =====================
class Tanah(models.Model):
    kode_barang = models.CharField(max_length=50)
    nama = models.CharField(max_length=200)
    luas = models.FloatField()
    lokasi = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    tahun_perolehan = models.IntegerField()

    def __str__(self):
        return self.nama

# =====================================================
# KIB B – PERALATAN & MESIN
# =====================================================
class PeralatanMesin(models.Model):
    kode_barang = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=200)
    jumlah = models.PositiveIntegerField(default=0)
    kondisi = models.CharField(max_length=100)
    tahun_perolehan = models.PositiveIntegerField()
    gambar = models.ImageField(
        upload_to='peralatan/',
        blank=True,
        null=True)

    # 🔥 INI HARUS DI DALAM CLASS
    ruangan = models.ForeignKey ('Ruangan',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='peralatan'        


    )

    def __str__(self):
        return f"{self.kode_barang} - {self.nama}"


# =====================================================
# PEMINJAMAN PERALATAN
# =====================================================
class Peminjaman(models.Model):
    STATUS_CHOICES = (
        ('dipinjam', 'Dipinjam'),
        ('kembali', 'Kembali'),
    )

    barang = models.ForeignKey(
        PeralatanMesin,
        on_delete=models.CASCADE,
        related_name='peminjaman'
    )
    peminjam = models.CharField(max_length=200)
    jumlah_pinjam = models.PositiveIntegerField()
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='dipinjam'
    )

    def __str__(self):
        return f"{self.barang.nama} - {self.peminjam}"

# =====================
# KIB C - GEDUNG & BANGUNAN
# =====================
class Gedung(models.Model):
    kode_barang = models.CharField(max_length=50)
    nama = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    luas = models.FloatField()
    kondisi = models.CharField(max_length=100)
    tahun_perolehan = models.IntegerField()

    def __str__(self):
        return self.nama
    


    #===========
    #ruangan ==========
    #====================

class Ruangan(models.Model):
    gedung = models.ForeignKey(
        Gedung,
        on_delete=models.CASCADE,
        related_name='ruangan'
    )
    nama = models.CharField(max_length=200)
    kode = models.CharField(max_length=50)
    penanggung_jawab = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.gedung.nama} - {self.nama}"


# =====================
# KIB D - JALAN / IRIGASI / JARINGAN
# =====================
class Jalan(models.Model):
    kode_barang = models.CharField(max_length=50)
    nama = models.CharField(max_length=200)
    panjang = models.FloatField()
    lokasi = models.CharField(max_length=200)
    kondisi = models.CharField(max_length=100)
    tahun_perolehan = models.IntegerField()

    def __str__(self):
        return self.nama

# =====================
# KIB E - ASET TETAP LAINNYA (BUKU)
# =====================
class Buku(models.Model):
    kode_barang = models.CharField(max_length=50)
    judul = models.CharField(max_length=255)
    pengarang = models.CharField(max_length=255)
    jumlah = models.IntegerField()
    kondisi = models.CharField(max_length=50)
    tahun_terbit = models.IntegerField()
    gambar = models.ImageField( upload_to='buku/', blank=True, null=True)

    def __str__(self):
        return self.judul
    
#====================================================
#Barang Habis Pakai bagian ini
#====================================================


class BarangHabisPakai(models.Model):
    kode_barang = models.CharField(max_length=50, unique=True)
    nama_barang = models.CharField(max_length=200)
    satuan = models.CharField(max_length=50, default='Unit')
    stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nama_barang} ({self.stok})"


class BarangHabisPakaiMasuk(models.Model):
    barang = models.ForeignKey(
        BarangHabisPakai,
        on_delete=models.CASCADE,
        related_name='masuk'
    )
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateField(default=timezone.now)
    sumber = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"Masuk {self.barang.nama_barang} ({self.jumlah})"


class BarangHabisPakaiKeluar(models.Model):
    barang = models.ForeignKey(
        BarangHabisPakai,
        on_delete=models.CASCADE,
        related_name='keluar'
    )
    jumlah = models.PositiveIntegerField()
    tanggal = models.DateField(default=timezone.now)
    pengguna = models.CharField(max_length=200)
    keperluan = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"Keluar {self.barang.nama_barang} ({self.jumlah})"
    



    
