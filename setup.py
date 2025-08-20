from setuptools import setup, find_packages

setup(
    name="django-calculator-app",          # Project name
    version="0.2.0",                       # Updated version
    author="Ankul Kumar",
    author_email="ankulmaurya88@gmail.com",
    description="A Django Calculator web application with CI/CD and Docker setup",
    packages=find_packages(),
    include_package_data=True,             # Includes templates and static folders
    install_requires=[
        "Django==4.2",
        "gunicorn==23.0.0",      # Updated valid version
        "pytest-django==4.5.2"            # For testing
    ],
    entry_points={
        "console_scripts": [
            # Optional: illustrative, Django usually runs via manage.py
            "runserver=manage:main",
        ],
    },
)
