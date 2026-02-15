from django.contrib import admin
from django.urls import path, include

# untuk handle media (gambar)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin django
    path('admin/', admin.site.urls),

    # routing ke app sarpras
    path('', include('sarpras.urls')),



  ]

# ===============================
# SETTING MEDIA FILE
# ===============================
# agar file gambar (ImageField) bisa diakses di browser
# HANYA aktif saat DEBUG = True
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )




