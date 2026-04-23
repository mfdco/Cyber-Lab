# Cyber-Lab

A Django-based cybersecurity learning platform where users can register, solve CTF-style challenges, and track their progress. Built for educational use with a structured challenge system, flag submission grading, and a set of built-in encoding/decoding tools.

---

## Features

- **User Authentication** — Register, log in, log out, and change your password
- **Challenge System** — Beginner, intermediate, and advanced problems with descriptions, puzzle content, hints, and optional downloadable files
- **Flag Submission & Grading** — Flags are hashed with PBKDF2 on creation; submissions are verified securely without storing plaintext answers
- **Progress Tracking** — Dashboard tracks which challenges have been completed per user
- **Submission History** — Full log of all flag submissions (correct and incorrect)
- **Cyber Tools Panel** — Built-in Base64 and Binary encode/decode utilities
- **Profile Page** — View account details and activity
- **Admin Interface** — Create and manage problems, users, and submissions through Django's admin panel

---

## Tech Stack

- **Backend:** Python / Django
- **Frontend:** HTML, CSS (custom styles)
- **Database:** SQLite (local, not tracked in version control)
- **Auth:** Django's built-in auth system with PBKDF2 password hashing

---

## Project Structure

```
cyberlab/
├── accounts/       # Auth views, login, signup, password change
├── challenges/     # Problem models, flag grading, submissions
├── core/           # Homepage, base templates, global styles
├── dashboard/      # Dashboard, progress, history, profile pages
├── submissions/    # Submission tracking app
├── tools/          # Encode/decode utility panel
└── cyberlab/       # Project settings and root URLs
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
# Clone the repo
git clone git@github.com:mfdco/Cyber-Lab.git
cd Cyber-Lab/cyberlab

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install django

# Apply migrations
python manage.py migrate

# Load challenge fixtures (optional)
python manage.py loaddata challenges/fixtures/challenges.json

# Create an admin user
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

---

## Adding Problems

Problems are managed through the Django admin panel at `/admin/`. When creating a problem, enter the plaintext flag in the **Flag** field — it will be automatically hashed before saving. The plaintext flag is never stored.

---

## Branches

| Branch | Purpose |
|---|---|
| `main` | Stable base |
| `development` | Latest release (v1.0.0) |
| `feature/grading-logic` | Grading, submissions, progress tracking |
| `feature/auth` | Authentication features |
| `feature/cyber-tools` | Encoding/decoding tools panel |
| `logic/grading` | Grading logic foundation |

---

## Release

**v1.0.0** — Final release on the `development` branch. Includes full challenge system, grading, progress tracking, submission history, tools panel, and user auth.
