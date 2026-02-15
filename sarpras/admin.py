from django.contrib import admin
from django.utils.html import format_html

# import model satu per satu (aman & jelas)
from .models import (
    Tanah,
    PeralatanMesin,
    Gedung,
    Jalan,
    Buku,   
    Peminjaman,
    BarangHabisPakai,
    BarangHabisPakaiMasuk,
    BarangHabisPakaiKeluar,
    Ruangan
            
)

# =====================================================
# KIB B - PERALATAN & MESIN (ADA GAMBAR)
# =====================================================
@admin.register(PeralatanMesin)
class PeralatanMesinAdmin(admin.ModelAdmin):
    # kolom yang tampil di list admin
    list_display = (
        'kode_barang',
        'nama',
        'jumlah',
        'kondisi',
        'tahun_perolehan',
        'gambar_preview',   # kolom gambar
    )

    search_fields = ('kode_barang', 'nama')
    list_filter = ('kondisi', 'tahun_perolehan')

    # fungsi untuk menampilkan thumbnail gambar
    def gambar_preview(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="70" style="border-radius:6px;" />',
                obj.gambar.url
            )
        return '-'

    gambar_preview.short_description = 'Gambar'

#==================================================================
# habis pakai disisni
#==================================================================

@admin.register(BarangHabisPakai)
class BarangHabisPakaiAdmin(admin.ModelAdmin):
    list_display = ('kode_barang', 'nama_barang', 'stok', 'satuan')
    search_fields = ('kode_barang', 'nama_barang')


@admin.register(BarangHabisPakaiMasuk)
class BarangMasukAdmin(admin.ModelAdmin):
    list_display = ('barang', 'jumlah', 'tanggal', 'sumber')
    list_filter = ('tanggal', 'sumber')


@admin.register(BarangHabisPakaiKeluar)
class BarangKeluarAdmin(admin.ModelAdmin):
    list_display = ('barang', 'jumlah', 'tanggal', 'pengguna', 'keperluan')
    list_filter = ('tanggal', 'pengguna')

# =====================================================
# MODEL LAIN (REGISTRASI SIMPEL, TIDAK DIUBAH)
# =====================================================
admin.site.register(Tanah)
admin.site.register(Gedung)
admin.site.register(Jalan)
admin.site.register(Buku)
admin.site.register(Peminjaman)
admin.site.register(Ruangan)

