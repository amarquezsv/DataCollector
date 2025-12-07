
from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("extract/", views.extract_data, name="extract_data"),
    path("data/", views.show_data, name="show_data"),
    path("", views.show_data, name="home"),  # 👈 root URL now shows data
]
