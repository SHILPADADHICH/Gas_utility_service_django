# Gas Utility Service Request Management

A Django-based web application designed for a gas utility company to handle customer service requests efficiently. This platform allows customers to submit service requests, track their status, and manage account information while providing support representatives with tools to manage and resolve requests effectively.

## Features

### For Customers:
- 📝 **Submit Service Requests**: Choose request type, provide details, and attach files.
- 🔄 **Track Request Status**: View submission time, progress updates, and resolution status.
- 📂 **Manage Account**: Update personal details and view service history.

### For Customer Support:
- 📊 **Admin Dashboard**: Manage and monitor incoming service requests.
- 📅 **Request Tracking & Resolution**: Update request status, assign support agents, and resolve queries efficiently.

## Technologies Used
- 🐍 **Django** - Backend framework.
- 🗄 **SQLite/PostgreSQL** - Database for storing requests and user data.
- 🎨 **Bootstrap & CSS** - Responsive UI.
- 📧 **Django Email System** - For service notifications.

## Installation

### 1️⃣ Clone the repository:
```bash
git clone <your-repo-url>
cd gas_utility_service_django
```

### 2️⃣ Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply database migrations:
```bash
python manage.py migrate
```

### 5️⃣ Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server:
```bash
python manage.py runserver
```

## Usage
1. Open `http://127.0.0.1:8000/` in your browser.
2. Register/Login as a customer to submit and track service requests.
3. Use the admin panel (`/admin/`) to manage service requests.

## Project Structure
```
├── gas_utility/                # Main project directory
│   ├── service_requests/       # App handling service requests
│   │   ├── templates/          # HTML templates
│   │   ├── static/             # CSS and JavaScript
│   │   ├── views.py            # Business logic
│   │   ├── models.py           # Database models
│   │   ├── urls.py             # URL routing
│   ├── templates/              # Base templates
│   ├── static/                 # Global static files
│   ├── settings.py             # Django settings
│   ├── manage.py               # Django CLI tool
```





## Contributing
Contributions are welcome! Fork the repository and submit a pull request. 🚀


