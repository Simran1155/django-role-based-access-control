from django.http import HttpResponse


def allowed_users(allowed_roles=None):
    """
    Allow access only to users whose role is present
    in the allowed_roles list.
    """

    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_fn):

        def wrapper_fn(request, *args, **kwargs):

            # User has no role assigned
            if request.user.role is None:
                return HttpResponse(
                    "User does not have a role assigned."
                )

            user_role = request.user.role.role

            if user_role in allowed_roles:
                return view_fn(request, *args, **kwargs)

            return HttpResponse(
                "You are not authorized to view this page."
            )

        return wrapper_fn

    return decorator


def admin_only(view_fn):
    """
    Allow access only to Admin users.
    """

    def wrapper_fn(request, *args, **kwargs):

        if request.user.role is None:
            return HttpResponse(
                "User does not have a role assigned."
            )

        if request.user.role.role == "admin":
            return view_fn(request, *args, **kwargs)

        return HttpResponse(
            "Only administrators can access this page."
        )

    return wrapper_fn