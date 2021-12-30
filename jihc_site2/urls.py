
from django.conf.urls.static import static
from jihc_site2 import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    
]+ static(settings. STATIC_URL,document_root=settings.MEDIA_ROOT) + static(settings. MEDIA_ROOT,document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('mainapp.urls'))
     )
