# API Views Documentation

This API handles CRUD operations for the `Book` model using Django REST Framework generic views.

## Endpoints

| Endpoint | Method | Description | Permission |
|-----------|---------|--------------|-------------|
| `/api/books/` | GET | Retrieve all books | Public |
| `/api/books/<id>/` | GET | Retrieve a single book by ID | Public |
| `/api/books/create/` | POST | Create a new book | Authenticated |
| `/api/books/<id>/update/` | PUT/PATCH | Update a book | Authenticated |
| `/api/books/<id>/delete/` | DELETE | Delete a book | Authenticated |

## Customization
- `perform_create()` and `perform_update()` allow pre-save customization.
- Filtering by title or author name is supported through `?search=` query params.
- Permissions use DRF’s `IsAuthenticated` and `AllowAny` classes.
