
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.pages.urls'))# sends url calls to the pages urls file cw
]
