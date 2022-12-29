from django.urls import path
from .views import (
    SignUpView,
    UserListView,
    UserDeleteView,
    ResetAdminPassword,
    new_password,
    HomeView,
    UserUpdateView,
    SearchUser,
)

urlpatterns = [
    path("daftar/", SignUpView.as_view(), name="admin-add"),
    path("admin-list/", UserListView.as_view(), name="admin-list"),
    path("admin-list/search/", SearchUser.as_view(), name="admin-search"),
    path("admin-list/<int:pk>/delete", UserDeleteView.as_view(), name="admin-delete"),
    path("admin-list/<int:pk>/reset", ResetAdminPassword.as_view(), name="admin-reset"),
    path("admin-list/<int:pk>/edit", UserUpdateView.as_view(), name="admin-update"),
    path("new-password/", new_password, name="new-password"),
    path("", HomeView.as_view(), name="home"),
]
