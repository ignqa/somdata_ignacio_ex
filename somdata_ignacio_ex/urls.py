from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('somdata_ex.urls')),
    path('admin/', admin.site.urls),
]
