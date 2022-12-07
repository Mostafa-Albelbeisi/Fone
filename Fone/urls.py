from django.urls import path
from .views import FoneListView, FoneDetailView, FoneCreateView, FoneUpdateView, FoneDeleteView

urlpatterns = [
    path("fone/", FoneListView.as_view(), name="fone-list"),
    path("fone/<int:pk>/", FoneDetailView.as_view(), name="fone-detail"),
    path("fone/create/", FoneCreateView.as_view(), name="fone-create"),
    path("fone/<int:pk>/update/", FoneUpdateView.as_view(), name="fone-update"),
    path("fone/<int:pk>/delete/", FoneDeleteView.as_view(), name="fone-delete"),
]
