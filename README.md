📇 Contact Management App using Django
This is a simple Contact Management Application built with Django and styled using Tailwind CSS. It allows users to add, edit, delete, and view contact details including name, phone number, and email address.

🔧 Features
➕ Add a new contact
✏️ Edit existing contact details
🗑️ Delete a contact
📜 View a list of all contacts
🎨 Modern UI with Tailwind CSS
⚙️ Django Admin support for managing contacts

🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML + Tailwind CSS
Database: SQLite (default Django DB, can be configured)


🚀 Getting Started
📦 Installation
Clone the repository:
git clone https://github.com/your-username/contact-management-app.git
cd contact-management-app
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Start the development server:

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to use the app.

🧪 Sample Contact Fields
Name: John Doe
Email: john@example.com
Phone: 9876543210

🔑 Admin Panel Access
To access Django’s admin panel:
Create a superuser:

python manage.py createsuperuser
Log in at http://127.0.0.1:8000/admin/

👨‍💻 Author
Abhishek A Shetty
shettyabhi0318@gmail.com
