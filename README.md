# Django Simple LMS (Library Management System)

A web-based Library Management System built with Django, using server-rendered templates styled with Tailwind CSS. Supports full CRUD for books and members, a borrow/return workflow with automatic copy tracking, and email confirmation on borrow.

## Features

- **Book management** — add, edit, delete, and list books with title, author, ISBN, and copy counts
- **Member management** — add, edit, delete, and list members with active/inactive status
- **Borrow & return workflow**
  - Select a book and member to record a new borrow
  - Automatically decrements available copies on borrow, restores on return
  - Due dates calculated automatically
  - Borrow history table with status badges (Borrowed / Returned)
- **Email confirmation** — sends a borrow confirmation email to the member (via Django's `send_mail`)
- **Responsive UI** — Tailwind CSS (CDN) with a consistent navy/gold theme across all pages

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML templates + Tailwind CSS (CDN)
- **Database:** SQLite (default Django dev database)

## Project Structure
library_lms/
├── libraryproject/
│   ├── library/
│   │   ├── models.py        # Book, Member, BorrowRecord
│   │   ├── views.py         # CRUD + borrow/return logic
│   │   ├── forms.py         # BorrowRecordForms (ModelForm)
│   │   ├── urls.py          # App URL routing
│   │   └── templates/
│   │       └── library/     # All HTML templates
│   └── libraryproject/      # Project settings, root urls.py
└── manage.py

## Setup

1. Clone the repo
```bash
   git clone https://github.com/kashan2023official-beep/django-simple-lms.git
   cd django-simple-lms
```

2. Create and activate a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
```

3. Install dependencies
```bash
   pip install django
```

4. Apply migrations
```bash
   python manage.py migrate
```

5. (Optional) For local development without a real mail server, add this to `settings.py`:
```python
   EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

6. Run the development server
```bash
   python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/`

## Routes

| Path | Name | Description |
|---|---|---|
| `/` | `home` | Dashboard/landing page |
| `/books/` | `book_list` | List all books |
| `/books/add/` | `add_book` | Add a new book |
| `/books/edit/<id>/` | `edit_book` | Edit a book |
| `/books/delete/<id>/` | `delete_book` | Delete a book |
| `/members/` | `member_list` | List all members |
| `/members/add/` | `add_member` | Add a new member |
| `/members/edit/<id>/` | `edit_member` | Edit a member |
| `/members/delete/<id>/` | `delete_member` | Delete a member |
| `/borrow/` | `borrow_book` | Borrow a book |
| `/borrow-history/` | `borrow_list` | View borrow history |
| `/return/<record_id>/` | `return_book` | Mark a record as returned |

## Status

Under active development as a learning project — CRUD, forms, and email are complete. Planned: migrating delete/return actions from GET links to POST forms for safety.

## Author

Built by [kashan2023official-beep](https://github.com/kashan2023official-beep) — B.Sc. Data Science student.
