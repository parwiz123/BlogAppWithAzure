Django Blog App with Azure Deployment
This is a Django Blog Application deployed on Microsoft Azure Web App.
It allows users to create, edit, and manage blog posts with full authentication support.

Features
User Registration & Login
Create, Update, Delete Blog Posts
Admin Dashboard
Responsive UI
Azure Cloud Deployment
Static file handling with WhiteNoise

Tech Stack
Django (Python)
HTML, CSS, Bootstrap
SQLite (default)
Azure Web App
Gunicorn + WhiteNoise

Local Setup
Clone Repository
git clone [https://github.com/your-username/your-repo.git](https://github.com/parwiz123/BlogAppWithAzure)
cd your-repo
Create Virtual Environment
python -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Migrations
python manage.py migrate
Run Server
python manage.py runserver

Deploy to Azure
1. Create Azure Web App
Go to Azure Portal
Create → Web App
Choose Python Runtime

2. Connect GitHub Repo
Open Deployment Center
Select GitHub
Choose your repository

Azure will automatically deploy your app from GitHub ()

3. Set Startup Command
gunicorn blog_project.wsgi

License
MIT License
