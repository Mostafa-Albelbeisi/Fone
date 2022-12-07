from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Fone


# Create your views here.


class FoneListView(ListView):
    template_name = "Fone/Fone-List.html"
    model = Fone


class FoneDetailView(DetailView):
    template_name = "Fone/Fone-Detail.html"
    model = Fone


class FoneCreateView(CreateView):
    template_name = "Fone/Fone-Create.html"
    model = Fone
    context_object_name = "countries"
    fields = ["carName", "carModel", "carFactory", "driver"]


class FoneUpdateView(UpdateView):
    template_name = "Fone/Fone-Update.html"
    model = Fone
    fields = ["carName", "carModel", "carFactory", "driver"]
    success_url = reverse_lazy("fone-list")


class FoneDeleteView(DeleteView):
    template_name = "Fone/Fone-Delete.html"
    model = Fone
    success_url = reverse_lazy("fone-list")
