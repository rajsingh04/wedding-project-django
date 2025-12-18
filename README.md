# Deploying to Vercel (guide)

This repo is prepared for a Vercel deployment using a WSGI entrypoint. Below are the minimal steps and important notes.

- Install Vercel CLI: `npm i -g vercel` or use the dashboard.
- Ensure you have a Python runtime in your environment (deployment uses `requirements.txt`).

Recommended environment variables to set in the Vercel dashboard for the project:

- `DJANGO_SECRET_KEY` — secure secret key
- `DEBUG` — set to `False` for production
- `ALLOWED_HOSTS` — comma-separated allowed hostnames (e.g. `your-domain.vercel.app`)
- If using a production DB, set `DATABASE_URL` and update settings to use it.

Important notes:

- SQLite is included by default in this project (`db.sqlite3`). Vercel serverless functions have ephemeral filesystem and are not suited to a persistent SQLite DB. For production, use a managed DB (Postgres) and configure `DATABASES` accordingly.
- Static files are configured to use WhiteNoise. Run `python manage.py collectstatic` during build or configure a build hook to collect static files.

Quick deploy (after signing in with `vercel login`):

1. Install dependencies locally (optional check):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Link and deploy with Vercel CLI:
   ```bash
   vercel link
   vercel --prod
   ```

If you want, I can:
- Add `dj-database-url` and switch settings to read a `DATABASE_URL` environment variable.
- Add a Vercel build hook to run `collectstatic` and other build steps.
