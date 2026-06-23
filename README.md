# CouponCrate

CouponCrate is a full‑stack **coupon** manager built with a Django backend, SQL database, and a responsive SASS‑powered frontend. It helps users securely store, organize, and track discount coupons in one place instead of losing them across email, SMS, and paper.[page:1]

---

## Features

- Add, edit, and delete coupons with fields like code, store, expiry date, and discount type.
- Mark coupons as used or expired, and keep your list clean.
- Filter and search coupons by store, category, or expiry date.
- Responsive UI styled with SASS, optimized for both desktop and mobile.
- Django admin panel for quick data inspection and management.
- SQL database for reliable and persistent coupon storage.

---

## Tech Stack

- Backend: Django
- Database: SQL (e.g., SQLite/PostgreSQL depending on your settings)
- Frontend: HTML, CSS, SASS (compiled to CSS)
- Other: Django templates, static files for styling and assets

---

## Project Structure

A high‑level overview of the repository layout (adjust to match your exact tree):[page:1]

- `backend/` – Django project and app code (models, views, URLs, settings).
- `couponcrateapp/` – Main app containing the coupon models, views, and templates.
- `CouponCrate.html` – Main page template for listing and managing coupons.[page:1]
- `CouponCrateLogin.html` – Login template for authenticating users.[page:1]
- `CouponCrate.css` – Compiled stylesheet generated from SASS for the frontend UI.[page:1]

---

## Getting Started

### Prerequisites

- Python 3.9+
- pip and virtualenv (recommended)
- Git
- SQLite (bundled with Python) or another SQL database

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/HarrisonVincent-E/CouponCrate.git
   cd CouponCrate
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   # venv\Scripts\activate         # Windows (PowerShell or CMD)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for Django admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to:
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

---

## Usage

- Sign up or log in using the login page (`CouponCrateLogin.html`).[page:1]
- Add new coupons using the “Add coupon” form (store, code, expiry, discount, etc.).
- View all coupons in a list, filter by store or expiry, and mark them as used.
- Edit or delete coupons as needed to keep your list up‑to‑date.

Example workflow:

1. You receive a promo code from an online store.
2. Open CouponCrate, add a new coupon entry with the code and expiry date.
3. Before shopping, check CouponCrate to see all valid coupons for that store.

---

## SASS and Styling

- All custom styles are authored in SASS and compiled into `CouponCrate.css`.[page:1]
- To modify the design:
  - Edit the SASS source files (for example in a `sass/` or `scss/` directory if present).
  - Recompile them to CSS using your preferred SASS tool, for example:
    ```bash
    sass styles.scss CouponCrate.css
    ```

---

## Environment Configuration

- Default settings use a local SQL database (typically SQLite) for development.
- For production, configure:
  - `DATABASES` in `settings.py` for PostgreSQL/MySQL.
  - `ALLOWED_HOSTS` and `DEBUG` flags.
  - Static file serving (e.g., via `collectstatic` and a web server like Nginx).

---

## Roadmap / Ideas

- Add reminder notifications for coupons nearing expiry.
- Support image uploads for coupon screenshots.
- Tagging system (e.g., “Food”, “Clothing”, “Electronics”).
- API endpoints for mobile apps or third‑party integrations.
- Dark mode and improved accessibility.

---

## Contributing

Contributions, issues, and feature requests are welcome.

- Fork the repository.
- Create a new branch: `git checkout -b feature/my-feature`.
- Commit your changes: `git commit -m "Add my feature"`.
- Push to the branch: `git push origin feature/my-feature`.
- Open a pull request.

---

## Contact

Created and maintained by **Harrison** (`HarrisonVincent-E` on GitHub).[page:1]  
- GitHub: [HarrisonVincent-E](https://github.com/HarrisonVincent-E)
