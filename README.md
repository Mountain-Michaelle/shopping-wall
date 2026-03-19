# Shopping Wall

A RESTful API backend for managing a multi-store shopping platform. Built with **FastAPI**, **SQLAlchemy**, and **SQLite** (swappable to PostgreSQL).

---

## Get Started

### What is this?

Shopping Wall is a backend API that allows:
- **Users** to register and authenticate
- **Store owners** to create and manage their stores
- **Products** to be listed under stores

The API is versioned under `/api/v1/` and follows REST conventions. All primary keys use **UUID** for global uniqueness. Every model tracks `created_at`, `updated_at`, and `is_active` automatically via a shared mixin.

---

### Installation

> Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+

**1. Clone the repository**

```bash
git clone https://github.com/your-username/shoppingwall.git
cd shoppingwall
```

**2. Install dependencies with uv**

```bash
uv sync
```

**3. Set up environment variables**

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

At minimum, set:

```env
DATABASE_URL=sqlite:///./test.db
```

**4. Run the development server**

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

**5. Explore the docs**

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Health check: `http://localhost:8000/health`

---

## Project Structure

```
shoppingwall/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/    # Route handlers (per resource)
│   ├── core/
│   │   └── config.py         # App settings (env vars via pydantic-settings)
│   ├── db/
│   │   ├── base.py           # SQLAlchemy Base + TimestampMixin (id, timestamps, is_active)
│   │   ├── session.py        # Engine and SessionLocal
│   │   ├── deps.py           # get_db() dependency for FastAPI routes
│   │   └── init_db.py        # Creates all tables on startup
│   ├── models/
│   │   ├── user.py           # User ORM model
│   │   ├── store.py          # Store ORM model
│   │   └── product.py        # Product ORM model
│   ├── schemas/
│   │   ├── user.py           # Pydantic schemas for User
│   │   └── store.py          # Pydantic schemas for Store
│   └── utils/
│       ├── uuid.py           # generate_uuid() helper
│       └── timenow.py        # utcnow() helper
├── main.py                   # Root entry (scaffold)
├── pyproject.toml            # Project metadata and dependencies (uv)
├── uv.lock                   # Locked dependency versions
├── .env                      # Local environment variables (not committed)
├── .gitignore
└── README.md
```

---

## Contributing

Contributions, issues, and feature requests are welcome!

**Steps to contribute:**

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/shoppingwall.git
   ```
3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies:**
   ```bash
   uv sync
   ```
5. **Make your changes** — follow the existing code style and structure
6. **Commit** with a clear message:
   ```bash
   git commit -m "feat: add product search endpoint"
   ```
7. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Open a Pull Request** against the `main` branch of this repository

### Guidelines

- Keep PRs focused — one feature or fix per PR
- Follow the existing folder structure (models → schemas → endpoints)
- All new models should inherit from `TimestampMixin, Base`
- Do not commit `.env` or `test.db` files

---

## 🍴 Forking

If you want to use this as a base for your own project:

1. Click **Fork** on GitHub
2. Clone your fork and rename the project in [`pyproject.toml`](pyproject.toml)
3. Update `DATABASE_URL` in your `.env` to point to your own database
4. Swap SQLite for PostgreSQL by changing the URL to `postgresql+psycopg2://user:pass@host/dbname` — no other code changes needed

---