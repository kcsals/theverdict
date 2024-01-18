from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'The Verdict Admin'
admin.site.index_title = 'Admin Page'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("content/", include('content.urls')),
    path("tags/", include('tags.urls'))
]
