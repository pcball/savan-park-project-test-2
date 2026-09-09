# Deploying to cPanel (Passenger / Setup Python App)

Django is a **Python WSGI app** — it will never show up under a "PHP + LAMP"
static-file deploy path. On cPanel it must go through **Setup Python App**
(Phusion Passenger), which is a separate tool from the PHP/static site flow.
That mismatch is what caused the "Could not detect a directory containing
static files ... for the project on PHP + LAMP" error.

## 1. Create the Python app in cPanel

1. cPanel → **Setup Python App** (not Site Publisher / File Manager's PHP flow).
2. Click **Create Application**:
   - Python version: 3.11 or 3.12 (whatever's newest available)
   - Application root: e.g. `savanpark` (creates `/home/<user>/savanpark`)
   - Application URL: your domain or subdomain
   - Application startup file: `passenger_wsgi.py`
   - Application Entry point: `application`
3. Save. cPanel creates a virtualenv and shows an **"Enter to the virtual
   environment"** command — copy it, you'll need it below.

## 2. Upload the project

Upload everything **except** `venv/`, `db.sqlite3`, `__pycache__/`,
`staticfiles/` into the Application root (via Git, or File Manager/FTP/SFTP).
This repo's `passenger_wsgi.py` (project root, next to `manage.py`) is
already set up as the Passenger entry point — don't move or rename it.

## 3. Install dependencies

In cPanel's terminal, run the "enter virtualenv" command it gave you, then:

```bash
cd ~/savanpark   # your Application root
pip install -r requirements.txt
```

## 4. Set environment variables

In the Setup Python App screen for this app, add:

| Variable | Value |
|---|---|
| `DJANGO_SECRET_KEY` | a long random string (generate one, don't reuse the dev default) |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | your domain, e.g. `savanpark.example.com` |

## 5. Run Django setup commands

Still inside the virtualenv:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py createsuperuser
```

Static files are served by **whitenoise** (already wired into
`MIDDLEWARE`/`STATICFILES_STORAGE` in `settings.py`), so no separate Apache
static-file mapping is required — collectstatic + whitenoise handles it
inside the Python process itself.

## 6. Restart the app

Back in the Setup Python App screen, click **Restart**. Visit your domain —
it should redirect to `/lo/` and show the Savan Park landing page.

## Notes

- SQLite (the default here) works for testing, but for anything real, prefer
  MySQL (available on the same LAMP host) — create a database in cPanel's
  **MySQL Databases**, then update `DATABASES` in `settings.py` to use
  `django.db.backends.mysql` with `mysqlclient` added to `requirements.txt`.
- If the app doesn't reload after code changes, touch a restart file:
  `touch tmp/restart.txt` inside the Application root, or use the Restart
  button in Setup Python App.
