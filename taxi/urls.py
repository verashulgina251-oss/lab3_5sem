from django.urls import path
from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:order_id>/", views.DetailView.as_view(), name="detail"),
]