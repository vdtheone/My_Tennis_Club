from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/details/<slug:slug>", views.details, name="details"),
    path("testing/", views.testing, name="testing"),
    # path("members/add_member", views.add_member, name="add_member"),
    path("members/add_new_member", views.add_new_member, name="add_new_member"),
    path("members/edit/<int:id>", views.update_member_details, name="edit"),
    path("members/delete/<int:id>", views.delete_member, name="delete"),
    path("logout/", views.logout_user, name="logout_user"),
]
