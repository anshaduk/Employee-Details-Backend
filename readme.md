##Employee Details Project##

This project allows employees to log in using Google Sign-In, register their details, view their profile, and edit their information. The application is built with a modern React.js frontend, a Django backend with SQLite database, and employs Django Rest Framework (DRF) for API handling.

##Features##

    Google Sign-In for secure and quick authentication.
    Register and manage employee details.
    View and edit employee profiles.
    Responsive and interactive user interface using React.js.
    Backend powered by Django and Django Rest Framework.
    Simple and lightweight SQLite database for data storage.

##Technologies Used##

    Frontend: React.js, Tailwind CSS
    Backend: Python, Django, Django Rest Framework
    Database: SQLite
    Authentication: Google OAuth
    API Development: Django Rest Framework

##Setup and Installation##
Follow these steps to set up and run the project on your local machine:

##Prerequisites##
Before you begin, ensure you have the following installed:

    Python 3.x
    Node.js (for React frontend)
    A virtual environment tool like venv or virtualenv
    Git

##Clone Repositories##
Frontend
1.Clone the React.js frontend repository
git clone https://github.com/anshaduk/Employee-Details-Frontend.git

2.Install dependencies:
npm install

3.Start the development server:
npm start



##Backend##
1. Clone the Django backend repository
git clone https://github.com/anshaduk/Employee-Details-Backend.git

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Start the Django development server:
python manage.py runserver

6. Open your browser and navigate to: http://127.0.0.1:8000







