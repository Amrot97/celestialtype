#!/usr/bin/env python
"""
Script to run Django with local settings (without database connection).
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.local_settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Run migrations to create SQLite database
    if len(sys.argv) == 1:
        execute_from_command_line(["manage.py", "migrate"])
        execute_from_command_line(["manage.py", "runserver", "8000"])
    else:
        execute_from_command_line(sys.argv) 