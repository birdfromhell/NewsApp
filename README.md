# News Website V2

A professional news website built with Django, featuring separate admin and author dashboards with role-based access control.

## Features

- **Custom Authentication System**

  - Role-based access control (Admin and Author roles)
  - Profile management with picture upload
  - Secure login/logout functionality

- **Dashboard System**

  - Admin dashboard for site management
  - Author dashboard for content management
  - Dynamic sidebar menu based on user role
  - Profile customization

- **Content Management**

  - Create, update, and delete news articles
  - Category management
  - Media uploads for article images
  - Draft and publish workflow

- **Modern UI**
  - DaisyUI and Tailwind CSS integration
  - Responsive design works on all devices
  - Dracula theme for dark mode aesthetics
  - Material icons support

## Tech Stack

- **Backend**: Django 4.x
- **Database**: MySQL
- **Frontend**:
  - Tailwind CSS
  - DaisyUI components
  - JavaScript with modern ES6+ features

## Project Structure

```
NewsApp/
├── Auth/           # Authentication & user management
├── Dashboard/      # Dashboard views & templates
│   ├── static/     # CSS, JS, and other static assets
│   ├── templates/  # HTML templates for dashboard
├── NewsApp/        # Main project settings
```

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- Node.js and npm (for Tailwind CSS)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/News-Website-V2.git
   cd News-Website-V2
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Configure the database in `NewsApp/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'newsapp',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Run migrations:

   ```
   python manage.py migrate
   ```

6. Create a superuser:

   ```
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```
   python manage.py runserver
   ```

8. Access the site at http://127.0.0.1:8000/

## Usage

### Admin Access

- Log in with superuser credentials
- Access the admin dashboard at `/dashboard/admin/`
- Manage authors, categories, and website settings

### Author Access

- Log in with author credentials (staff=True, superuser=False)
- Access the author dashboard at `/dashboard/author/`
- Create, edit, and manage articles

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI](https://daisyui.com/)
