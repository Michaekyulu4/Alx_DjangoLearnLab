# Django Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):
- `can_view` → View book list/details
- `can_create` → Add new books
- `can_edit` → Edit existing books
- `can_delete` → Delete books

## Groups
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → All permissions

## Enforcement
Views use `@permission_required` decorators in `bookshelf/views.py`.
Unauthorized users will get a **403 Forbidden** response.