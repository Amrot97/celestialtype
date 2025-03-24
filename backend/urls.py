from django.contrib import admin
from django.urls import path, include
from .views import home_view, endpoints_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # Enabling the natal chart URLs since we now have Python 3.10+
    path('natal-chart/', include('natal_chart.urls')),
    path('', home_view, name='home'),
    path('endpoints/', endpoints_view, name='endpoints'),
]
