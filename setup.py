from setuptools import setup, find_packages

setup(
    name="django-calculator-app",          # Project name
    version="0.2.0",                       # Updated version
    author="Ankul kumar",
    author_email="ankulmaurya88@gmail.com.com",
    description="A Django Calculator web application with CI/CD and Docker setup",
    packages=find_packages(),
    include_package_data=True,             # Includes templates, static folders
    install_requires=[
        "Django==4.2",
        "gunicorn==22.3.0",               # For production server
        "pytest-django==4.5.2"            # For testing
    ],
    entry_points={
        "console_scripts": [
            # Optional: run Django server with manage.py
            "runserver=manage:main",      # This is illustrative; Django usually uses `python manage.py runserver`
        ],
    },
)
