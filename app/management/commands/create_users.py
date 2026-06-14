from django.core.management.base import BaseCommand
from app.models import User, Role


class Command(BaseCommand):
    help = "Create sample users for testing"

    def handle(self, *args, **kwargs):

        admin_role = Role.objects.get(role="admin")
        manager_role = Role.objects.get(role="manager")
        employee_role = Role.objects.get(role="employee")

        users_created = 0

        # Create Admins
        for i in range(1, 6):

            user, created = User.objects.get_or_create(
                username=f"admin{i}",
                defaults={
                    "email": f"admin{i}@test.com",
                    "role": admin_role,
                }
            )

            if created:
                user.set_password("password123")
                user.save()
                users_created += 1

        # Create Managers
        for i in range(1, 6):

            user, created = User.objects.get_or_create(
                username=f"manager{i}",
                defaults={
                    "email": f"manager{i}@test.com",
                    "role": manager_role,
                }
            )

            if created:
                user.set_password("password123")
                user.save()
                users_created += 1

        # Create Employees
        for i in range(1, 6):

            user, created = User.objects.get_or_create(
                username=f"employee{i}",
                defaults={
                    "email": f"employee{i}@test.com",
                    "role": employee_role,
                }
            )

            if created:
                user.set_password("password123")
                user.save()
                users_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {users_created} users."
            )
        )