import sys
import os

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "make sure django is installed and a virtual environment is active"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
