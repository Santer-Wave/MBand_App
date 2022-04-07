from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mband.urls')),
    # path('api/', get_schema_view(
    #     title="MBand",
    #     description="API приложения MBand",
    #     version="Просто знайте, что это лютый хардкод.."
    # ),
    #      name='openapi-schema'
    #      ),
    path('docs/', include_docs_urls(title='MBand'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
