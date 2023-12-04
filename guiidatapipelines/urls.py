from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("datapipeline/", include("datapipeline.urls")),
    path('admin/', admin.site.urls),
]
