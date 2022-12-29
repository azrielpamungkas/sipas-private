from django.urls import path

from .views import (
    incoming_list,
    incoming_detail,
    incoming_create,
    incoming_update,
    incoming_delete,
    incoming_search,
    outgoing_list,
    outgoing_search,
    outgoing_detail,
    outgoing_create,
    outgoing_update,
    outgoing_delete,
)

urlpatterns = [
    path("i/", incoming_list, name="incoming-mail-list"),
    path("i/search/", incoming_search, name="incoming-search"),
    path("i/<int:pk>/", incoming_detail, name="incoming-mail-detail"),
    path("i/create/", incoming_create, name="incoming-mail-create"),
    path("i/<int:pk>/edit/", incoming_update, name="incoming-mail-update"),
    path("i/<int:pk>/delete/", incoming_delete, name="incoming-mail-delete"),
    path("o/", outgoing_list, name="outgoing-mail-list"),
    path("o/search/", outgoing_search, name="outgoing-search"),
    path("o/<int:pk>/", outgoing_detail, name="outgoing-mail-detail"),
    path("o/create/", outgoing_create, name="outgoing-mail-create"),
    path("o/<int:pk>/edit/", outgoing_update, name="outgoing-mail-update"),
    path("o/<int:pk>/delete/", outgoing_delete, name="outgoing-mail-delete"),
]
