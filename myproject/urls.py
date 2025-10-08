from django.contrib import admin
from django.urls import path, include   # include qo‘shamiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),     # asosiy app’ga yo‘naltiramiz
]
