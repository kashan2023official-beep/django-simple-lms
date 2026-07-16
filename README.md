# Django Library Management System

A simple Library Management System built with Django, allowing staff to manage books, members, and borrow records — with automatic email notifications sent to members when they borrow a book.

## Features

- **Book Management** — Add, edit, delete, and list books (title, author, ISBN, total/available copies)
- **Member Management** — Add, edit, delete, and list members
- **Borrow Records** — Track which member borrowed which book, borrow date, due date, and return status
- **Email Notifications** — When a member borrows a book, an automatic confirmation email is sent to their registered email address (via Gmail SMTP), including the book's details
- **Return Handling** — Mark books as returned, automatically restoring available copy counts

## Tech Stack

- Python / Django
- SQLite (default database)
- Gmail SMTP (for sending emails)
- python-decouple (for managing environment variables/secrets)

## Project Structure

```
libraryproject/
├── library/               # Main app: models, views, forms, templates
│   ├── models.py          # Book, Member, BorrowRecord models
│   ├── views.py           # CRUD views + borrow/return logic + email sending
│   ├── forms.py
│   ├── urls.py
│   └── templates/library/
├── libraryproject/         # Project settings
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── .env                   # Local secrets (not tracked in Git)
```

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/kashan2023official-beep/django-simple-lms.git
cd django-simple-lms/libraryproject
```

### 2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
```

### 3. Install dependencies

```
pip install django python-decouple
```

### 4. Set up environment variables

Create a `.env` file in the same folder as `manage.py` with the following:

```
EMAIL_HOST_USER=your_gmail_address@gmail.com
EMAIL_HOST_PASSWORD=your_16_character_gmail_app_password
```

> Note: `EMAIL_HOST_PASSWORD` must be a Gmail **App Password**, not your regular Gmail password. Generate one from your Google Account → Security → App Passwords (requires 2-Step Verification to be enabled).

### 5. Apply migrations

```
python manage.py migrate
```

### 6. Run the development server

```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Email Notifications

When a member borrows a book, a confirmation email is automatically sent to the email address on their member record, including:
- Book title and author
- Borrow date
- A reminder to return the book on time

Emails are sent via Gmail SMTP, configured in `settings.py` using credentials pulled securely from the `.env` file.

## Notes

- `.env` and `db.sqlite3` are excluded from version control via `.gitignore` — each environment should generate its own database via migrations and set its own local credentials.
- This project was built as a learning exercise covering Django's MVT architecture, forms, the ORM, and email integration.
