from django.urls import path
from .views import create_contact , list_user , list_contact , \
    userinformation , create_user , upload , uploadlist , delete_upload

urlpatterns = [
    path("listcontact/" , list_contact.as_view() , name = "listcontact"),
    path("createcontact/" , create_contact.as_view() , name = "createcontact"),
    path("createuser/" , create_user.as_view() , name = "createuser"),
    path("listuser/" , list_user.as_view() , name = "listuser"),
    path("userinformation/<int:pk>/" , userinformation.as_view() , name = "userinformation"),
    path("upload/" , upload.as_view() , name = "upload"),
    path("uploadlist/" , uploadlist.as_view() , name = "uploadlist"),
    path("delete_upload/<int:pk>/" , delete_upload.as_view() , name = "deleteupload"),


]

