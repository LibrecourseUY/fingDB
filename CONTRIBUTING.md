# Contributing to fingDB

Thank you for your interest in contributing to fingDB! This guide will walk you through how to contribute.

## What is fingDB?

fingDB is the centralized database that provides information to all Fingdev projects. Any data that Fingcomms, Fingmap, or other apps need to share goes through here.

## Why Contribute?

- Learn about REST APIs
- Understand how to design databases
- Work with Python and FastAPI
- Help the engineering student community

## Code of Conduct

Be respectful to all contributors. Let's keep the community open and welcoming.

## Contribution Workflow (Standard Git Flow)

### Step 1: Fork

1. Go to: https://github.com/fingdev/fingdb
2. Click "Fork"
3. Select your account

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/fingdb.git
cd fingdb
```

### Step 3: Create a New Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

### Step 4: Work on Your Code

Edit the necessary files. Make sure to:
- Not add secrets or passwords
- Follow project conventions
- Add tests if possible

### Step 5: Commit

```bash
git add .
git commit -m "type: description of changes"
```

#### Commit Types

| Type | Description |
|------|-------------|
| `feat:` | New feature or endpoint |
| `fix:` | Bug fix |
| `docs:` | Documentation |
| `refactor:` | Rewrite code |
| `test:` | Tests |
| `migration:` | Database changes |

**Examples:**
```
feat: add endpoint to get building list
fix: correct user data validation
migration: add faculties table
```

### Step 6: Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a Pull Request.

## Development Requirements

- Python 3.11+
- PostgreSQL (optional for local development)
- uv (package manager)

### Local Setup

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv install

# Copy configuration
cp .env.example .env

# Run migrations
uv run alembic upgrade head

# Start server
uv run uvicorn app.main:app --reload
```

## Code Structure

```
fingdb/
├── app/
│   ├── main.py           # Entry point
│   ├── models/           # Database models
│   ├── routers/          # API endpoints
│   ├── schemas/          # Validation schemas
│   └── database.py      # Database connection
├── migrations/           # Alembic migrations
└── pyproject.toml       # Configuration
```

## Testing

Run tests with:

```bash
uv run pytest
```

## API Conventions

- RESTful endpoints (GET, POST, PUT, DELETE)
- English names for endpoints
- Appropriate HTTP codes:
  - 200: Success
  - 201: Created
  - 400: Client error
  - 404: Not found
  - 500: Server error

## Code Review

Your PR will be reviewed by a maintainer. They may request changes. Don't worry! It's normal.

## Signed Commits (Required)

All commits must be signed. This is a mandatory requirement for contributing.

### Why Signed Commits?

- **Security**: Verifies that you are who you claim to be
- **Integrity**: Guarantees the commit wasn't modified after creation
- **Trust**: Other contributors know changes genuinely come from you
- **Professionalism**: Industry best practice for open source projects

### Setup

Follow our Git Guide to set up your SSH key:
- [SSH Key Setup](https://fingdev.github.io/git)

Configure Git to sign commits by default:
```bash
git config --global commit.gpgsign true
```

## Questions?

Questions? Create an Issue and we'll help you.
