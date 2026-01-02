---
description: Repository Information Overview
alwaysApply: true
---

# NeuroScan Project Information

## Summary
NeuroScan is a Django-based web application designed for research management, data analysis, and community engagement. It features a comprehensive blog system, user account management with profile customization, and specialized tools for scientific research and data repository management. The project supports multi-language capabilities including English, French, and Arabic.

## Structure
- **NeuroScan/**: Core project configuration, including settings, main URL routing, and WSGI/ASGI definitions.
- **account/**: Manages user authentication, profiles, and specialized dashboard tools (scientific, analysis, database, tools).
- **blog_app/**: Handles the blogging platform, including posts, tags (via `django-taggit`), comments, and research article management.
- **locale/**: Contains translation files for internationalization (ar, fr).
- **media/**: Centralized storage for user-uploaded content such as post images and research PDFs.
- **static/**: Directory for project-wide static assets (CSS, JavaScript, images).

## Language & Runtime
**Language**: Python  
**Version**: 3.10+ (Inferred from Django 5.0.14 requirements)  
**Build System**: Django  
**Package Manager**: pip

## Dependencies
**Main Dependencies**:
- `Django==5.0.14`
- `django-taggit`: Tagging functionality for blog posts.
- `easy-thumbnails`: Image processing and thumbnail generation.
- `psycopg2` or `psycopg`: PostgreSQL database adapter.
- `django-sitemaps`: Sitemap generation for SEO.

## Build & Installation
```bash
# Install dependencies (assuming requirements.txt is generated)
pip install django django-taggit easy-thumbnails psycopg2

# Apply database migrations
python manage.py migrate

# Load initial data (if applicable)
python manage.py loaddata blog_data.json

# Start the development server
python manage.py runserver
```

## Testing
**Framework**: Django Test Framework (built-on unittest)
**Test Location**: 
- `account/tests.py`
- `blog_app/tests.py`
**Naming Convention**: Standard Django `tests.py` files.
**Run Command**:
```bash
python manage.py test
```

## Main Files & Resources
- **manage.py**: Entry point for administrative tasks.
- **NeuroScan/settings.py**: Main configuration file including database and app settings.
- **NeuroScan/urls.py**: Root URL configuration with i18n support.
- **blog_data.json**: Data file likely used for seeding or backup of blog content.
- **find_migration.py**: Utility script for migration management.
