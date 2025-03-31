from django.urls import path
from .views import NatalChartView

urlpatterns = [
    path('', NatalChartView.as_view(), name='natal_chart'),
] 