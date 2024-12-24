# Django + Tailwind CSS + Authentication System

This project is a boilerplate/template that integrates **Django** with **Tailwind CSS** and includes a basic authentication system. It's designed for beginners who want to learn how to combine Django's backend with modern frontend styling tools like Tailwind CSS.

## Features

- **Django Framework**: Backend logic and template rendering.
- **Tailwind CSS**: Modern utility-first CSS framework for styling.
- **Authentication System**:
  - User registration
  - User login
  - User logout
  - Password reset
- **Responsive Design**: Styled using Tailwind CSS to look great on all devices.
- **Template Structure**: Preconfigured templates for easy customization.

## Prerequisites

- Python 3.8+
- Django 4.0+
- Node.js (for Tailwind CSS installation)

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/tailwind-django-auth.git
cd tailwind-django-auth
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Tailwind CSS Dependencies
```bash
npm install
```

### 5. Configure the Database
Run the following commands to apply migrations and create a superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### 7. Build Tailwind CSS (Optional)
If you make changes to Tailwind configuration or CSS files, run:
```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

## Folder Structure
```
project/
├── templates/          # HTML templates (includes base.html, auth templates)
├── static/             # Static files (Tailwind CSS, JS)
│   ├── src/            # Source CSS for Tailwind
│   └── css/            # Compiled CSS
├── app/                # Main Django app (authentication views)
├── manage.py           # Django entry point
└── requirements.txt    # Python dependencies
```

## Authentication Pages

1. **Login**: `http://127.0.0.1:8000/login/`
2. **Register**: `http://127.0.0.1:8000/register/`
3. **Logout**: `http://127.0.0.1:8000/logout/`
4. **Password Reset**: `http://127.0.0.1:8000/password-reset/`

## Customization

### Modify Tailwind CSS
Edit the Tailwind configuration file (`tailwind.config.js`) or the source CSS file (`static/src/input.css`) to customize styles.

### Templates
Update templates in the `templates/` folder to fit your design.

## Contribution

Feel free to fork the repository and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

---

Happy coding! 🚀

