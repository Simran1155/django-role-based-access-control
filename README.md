# Django RBAC System (Demo Project)

A simple **Role-Based Access Control (RBAC)** system built with Django using a custom user model, roles, and decorators.

>  This is a **demo project**, so views currently return `HttpResponse`. In a real application, these can be replaced with proper HTML templates or frontend/API-based responses.

---

##  Features

- Custom User Model (`AbstractUser`)
- Role Model (Admin, Manager, Employee)
- Role-Based Access Control (RBAC)
- Custom decorators for permission handling:
  - `allowed_users()`
  - `admin_only()`
- Django data migration to auto-create roles
- Custom management command to seed users

---

##  Roles & Access

- **Admin** → Full access
- **Manager** → Project + task management
- **Employee** → Task updates & limited access

---

##  Example Routes

- `/dashboard/` → All roles
- `/create-project/` → Admin, Manager
- `/assign-tasks/` → Manager, Employee
- `/update-tasks/` → Manager, Employee
- `/manage-users/` → Admin only

---

##  Concepts Covered

- Django Authentication & Authorization
- Custom User Model
- ForeignKey relationships
- Decorators in Python
- Django Migrations (`RunPython`)
- Custom Management Commands

---

##  Run Project

```bash
python manage.py migrate
python manage.py create_users
python manage.py runserver
