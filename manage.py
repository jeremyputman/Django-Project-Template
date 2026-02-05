# manage.py
import os
import sys
from pathlib import Path

# 👇 load .env BEFORE touching Django
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        os.environ.get(
            "DJANGO_SETTINGS_MODULE",
            "{{ project_name }}.settings.development",
        ),
    )
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()