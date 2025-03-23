from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.GenerateNatalChartView.as_view(), name="generate_natal_chart"),
    path("elements/", views.ElementAnalysisView.as_view(), name="element_analysis"),
    path("elements/relationships/", views.ElementRelationshipsView.as_view(), name="element_relationships"),
    path("modalities/", views.ModalityAnalysisView.as_view(), name="modality_analysis"),
    path("stelliums/", views.StelliumDetectionView.as_view(), name="stellium_detection"),
    path("test/", TemplateView.as_view(template_name="natal_chart/test_form.html"), name="test_form"),
]
