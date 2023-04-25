from django.contrib import admin
from django.urls import include, path
from test_task.yasg import urlpatterns as new_url
from coin.views import *
from coin import views

urlpatterns = [
    path('coin/', include('coin.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
urlpatterns += new_url