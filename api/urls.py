from django.urls import path

from api.views import CreateVisitView, ListRetailOutletsView

app_name = "retail_outlets"

urlpatterns = [
    path("", ListRetailOutletsView.as_view(), name="retail_outlets-list"),
    path("visit", CreateVisitView.as_view(), name="retail_outlets-visit"),
]
