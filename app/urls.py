from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-project/", views.create_project, name="create_project"),
    path("assign-tasks/", views.assign_tasks, name="assign_tasks"),
    path("update-tasks/", views.update_tasks, name="update_tasks"),
    path("manage-users/", views.manage_users, name="manage_users"),
]