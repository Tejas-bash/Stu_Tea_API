from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_data, create_teacher_data

urlpatterns = [
    path("api/get_view/", view_data, name="view_data"),
    path("api/create_teacher_data/", create_teacher_data, name="create_teacher_data"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
