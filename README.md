# Health Insurance Claim Project

This project is a Django-based web application designed to manage health insurance claims. The primary goal is to use this project as a learning experience to understand Django's core concepts, including models, views, templates, and PostgreSQL integration.

## Features
- Patient Registration & Management
- CRUD operations for patient records
- PostgreSQL Database Integration
- Django Admin Customization
- URL Routing & Views Implementation
- ASGI & WSGI Concepts
- Deployment Readiness

## Learning Objectives
Through this project, I am gaining hands-on experience with:
- **Django Models:** Understanding how to define models and interact with the database.
- **Views & Templates:** Learning how to fetch and display data dynamically.
- **PostgreSQL Database:** Connecting Django with PostgreSQL for efficient data storage.
- **Admin Panel Customization:** Enhancing Django’s admin panel for better record management.
- **ASGI vs WSGI:** Learning the difference between synchronous and asynchronous Django applications.
- **Static & Media Files:** Managing CSS, JavaScript, and images in Django projects.

## Setup & Installation
To run this project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/health-insurance-claim.git
   cd health-insurance-claim
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure PostgreSQL Database:**
   - Update `settings.py` with your PostgreSQL credentials.
5. **Apply migrations & create superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   Open `http://127.0.0.1:8000/` in your browser.

## Future Enhancements
- Implement user authentication & authorization.
- Add an API using Django REST Framework.
- Enhance UI with Bootstrap or TailwindCSS.

## Contributing
If you’d like to contribute, feel free to fork the repository and create a pull request!

## License
This project is licensed under the MIT License.

