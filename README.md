# Savan Park

Django test project for evaluating hosting deployment.

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the public listing and `http://127.0.0.1:8000/admin/`
for the admin (local dev login: `admin` / `savanpark-dev123` — change before deploying anywhere shared).

## Deployment note

This is a **Django (Python/WSGI)** project, not PHP. A classic LAMP stack
(Linux + Apache + MySQL + PHP) won't run it as-is — it needs to go through a
Python-capable path (cPanel's Setup Python App / Passenger, or Gunicorn +
Nginx). See `DEPLOY_CPANEL.md` for step-by-step cPanel deployment, and
`server-access-request.md` for a draft message to request hosting access.
