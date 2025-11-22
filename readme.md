# LGS - Website

The scope of this project is the engineering of a secure, dedicated Customer Landing Page for Lazy Gusty Solutions. This web platform's primary function is lead generation, achieved by clearly articulating LGS's solutions and core capabilities. The page is designed to be highly conversion-focused, maximizing digital engagement metrics to directly support and fuel ongoing sales efforts.

---

## 🌐 Live Deployment

The site is deployed at [https://lazyguzty.com](https://lazyguzty.com)

---

## 🧭 Features

- ⭐ Hero Section 
- 🛠️ Services section highlighting core service offerings
- 💬 Testimonials from satisfied clients
- 📧 Contact Us form for general inquiries, project proposals, and newsletter subscription
- 🔔 Dynamic message display for form submissions (success/error feedback)
- 📱💻 Responsive design for various devices (implied by Django/HTML/CSS structure)

---

## ⚙️ Technologies Used
- **Backend:** Django 5.2.4
- **Frontend:** Bootstrap 5, CSS/JS
- **Database:** PostgreSQL 17.5
- **Deployment:** Pending

---

## 📁 Project Structure - Single App (Standard Structure)
```
lgs-website/
├── config/                     # Main Django project settings (settings.py, urls.py, wsgi.py,asgi.py)
├── webiste/                    # Core Django app for landing page features
│   ├── migrations/             # Database migration files
│   ├── static/webiste/         # App-specific static files (CSS, JS, images)
│   ├── templates/webiste/      # HTML templates for views (e.g., index.html, contact_us.html)
│   ├── views.py                # Business logic for rendering pages and handling requests
│   ├── urls.py                 # URL routing for the landing_page app
│   ├── models.py               # Database models (data structure via Django ORM)
│   └── admin.py                # Django Admin site configuration for models
├── venv/                       # Python Virtual Environment (ignored by Git)
├── .env                        # Environment variables (CRITICAL: ignored by Git)
├── .env.example                # Template for environment variables.
├── .gitignore                  # Specifies files and directories to be ignored by Git
├── manage.py                   # Django's command-line utility
└── requirements.txt            # Project dependencies
```

---

## 🚀 Getting Started

### Prerequisites
    - Python 3.11.7
    - PostgreSQL 17.5
    - Redis (for Celery message broker)
    - pip (Python package installer)
    - virtualenv

### Installation

1.  **Clone the repository:**
    ```bash
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create venv folder named "venv"
    python3 -m venv venv

    # Activate venv
    . venv/bin/activate # On macOS/Linux
    . venv/scripts/activate # On Windows (Command Prompt)
    . venv/scripts/activate # On Windows (PowerShell)
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up PostgreSQL Database:**
    * Install PostgreSQL:
        - macOS (using Homebrew): `brew install postgresql`
        - Linux (Debian/Ubuntu): `sudo apt update && sudo apt install postgresql postgresql-contrib`
        - Windows: Download the installer from the [PostgreSQL website](https://www.postgresql.org/download/windows/).
    * Create a PostgreSQL User and Database:
        Access the PostgreSQL prompt (e.g., `psql -U postgres or psql postgres`) and run:
        ```sql
        CREATE USER myuser WITH PASSWORD 'mypassword';          -- Choose your preferred username and password
        CREATE DATABASE mydatabase OWNER myuser;                -- Choose your preferred database name
        GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;  -- Make myuser a super-administrator
        \q                                                      -- Exit psql
        ```
        *Replace `myuser` and `mypassword` with your desired credentials, and `mydatabase` with your preferred database name (e.g., `ees_db`).*
     * Configure your `.env` file:
        Create `.env` file in your project's root directory and add/verify the following lines:
        ```dotenv
        # .env file - IMPORTANT: DO NOT COMMIT THIS FILE TO GIT!
        # Add this file to your .gitignore

        SECRET_KEY=<your_generated_secret_key>
        # Generate a unique key using:
        python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        DATABASE_URL=postgresql://<your_username>:<your_password>@localhost:5432/<your_database_name>
        DEBUG=True
        ALLOWED_HOSTS=127.0.0.1,localhost
        ```
        *Ensure the `DATABASE_URL` uses the exact username, password, and database name you created in the PostgreSQL steps above. For example, `postgresql://my_dev_user:my_secret_pass@localhost:5432/my_app_db`.*

5.  **Apply database migrations:**
     ```bash
    python manage.py migrate
    ```
     *Note: `makemigrations` is only needed when you create new models or modify existing ones. For initial setup, `migrate` is sufficient to apply existing migrations.*

6.  **Create a superuser (for Django Admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your admin credentials (username, email, password).
    *Note: This Django superuser is separate from your PostgreSQL database user (`<your_username>`). The credentials for your Django admin login do not need to match your database credentials.*