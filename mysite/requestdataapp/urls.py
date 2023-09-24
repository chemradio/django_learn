from django.urls import path

from .views import handle_upload_file, process_get_view, user_form

app_name = "requestdataapp"
urlpatterns = [
    path("get/", process_get_view, name="process_get_view"),
    path("bio/", user_form, name="user_form"),
    path("upload/", handle_upload_file, name="handle_upload_file"),
]
