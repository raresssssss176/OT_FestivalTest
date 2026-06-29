import os
from pathlib import Path

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

load_dotenv(PROJECT_DIR / ".env")
load_dotenv(BASE_DIR / ".env")

# Folderul în care se află acest fișier: /python
BASE_DIR = Path(__file__).resolve().parent

# Folderul principal al proiectului
PROJECT_DIR = BASE_DIR.parent

# Folderul cu paginile HTML
HTML_DIR = PROJECT_DIR / "html"

# Folderul cu imaginile și asset-urile site-ului
STATIC_DIR = HTML_DIR

# Baza de date SQLite
DATABASE_URL = f"sqlite:///{BASE_DIR / 'festival.db'}"


# Setări JWT
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "schimba-aceasta-cheie-inainte-de-publicare-overthink-film-fest"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7


# Setări email
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")

EMAIL_FROM = os.getenv(
    "EMAIL_FROM",
    "Overthink Film Fest <noreply@overthink-jr.com>"
)


# Setări generale festival
FESTIVAL_NAME = "Overthink Film Fest"

CONTACT_EMAIL = "staff@overthink-jr.com"

SUBMISSION_DEADLINE = "2026-08-01"

print("DATABASE_URL FOLOSIT:", DATABASE_URL)