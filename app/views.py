from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .decorators import allowed_users, admin_only


# ----------------------------------
# Authentication Views
# ----------------------------------

def login_user(request):
    """
    Authenticate user and start a session.
    Redirect to dashboard on successful login.
    """

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return HttpResponse(
            "Invalid username or password"
        )

    return render(request, "login.html")


def logout_user(request):
    """
    End user session and redirect to login page.
    """

    logout(request)
    return redirect("login")


# ----------------------------------
# Protected Views
# ----------------------------------

@login_required(login_url="login")
@allowed_users(
    allowed_roles=[
        "admin",
        "manager",
        "employee"
    ]
)
def dashboard(request):
    """
    Accessible by:
    - Admin
    - Manager
    - Employee
    """

    response = f"""
    Username: {request.user.username}<br>
    Role: {request.user.role.role}<br>
    Dashboard Access Granted
    """

    return HttpResponse(response)


@login_required(login_url="login")
@allowed_users(
    allowed_roles=[
        "admin",
        "manager"
    ]
)
def create_project(request):
    """
    Accessible by:
    - Admin
    - Manager
    """

    response = f"""
    Username: {request.user.username}<br>
    Role: {request.user.role.role}<br>
    Create Project Access Granted
    """

    return HttpResponse(response)


@login_required(login_url="login")
@allowed_users(
    allowed_roles=[
        "manager",
        "employee"
    ]
)
def assign_tasks(request):
    """
    Accessible by:
    - Manager
    - Employee
    """

    response = f"""
    Username: {request.user.username}<br>
    Role: {request.user.role.role}<br>
    Task Assignment Access Granted
    """

    return HttpResponse(response)


@login_required(login_url="login")
@allowed_users(
    allowed_roles=[
        "manager",
        "employee"
    ]
)
def update_tasks(request):
    """
    Accessible by:
    - Manager
    - Employee
    """

    response = f"""
    Username: {request.user.username}<br>
    Role: {request.user.role.role}<br>
    Task Updation Access Granted
    """

    return HttpResponse(response)


@login_required(login_url="login")
@admin_only
def manage_users(request):
    """
    Accessible by:
    - Admin Only
    """

    response = f"""
    Username: {request.user.username}<br>
    Role: {request.user.role.role}<br>
    Manage Users Access Granted
    """

    return HttpResponse(response)