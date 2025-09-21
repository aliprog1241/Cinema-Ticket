from django.contrib import admin
from django.urls import path, include
from app.views import signup, stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('stats/', stats, name='stats'),
]

