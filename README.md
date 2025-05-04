# codingsphereprj
A project implementing a RESTful API using FastAPI with JWT authentication and Role-Based Access Control

## The main Features includes :
A User registration and authentication with JWT tokens and Role-based access control (admin and user roles)
CRUD operations for projects
PostgreSQL database using SQLModel ORM
Secure password hashing with bcrypt


## The Project was developed using

>Python 3.8+ (FAST API)
>PostgreSQL database


The project was initialized bu creating a virtual environment and install dependencies:
The steps to run the code begins as follows
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Then Create a .env file with your configuration:
DATABASE_URL=postgresql://postgres:password@localhost:5432/jwt_rbac_db
SECRET_KEY=your_super_secret_key_change_this_in_production
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True

Move on to create the Database in the pgAdmin or the shell sql 
Create the database:
bash# In PostgreSQL
CREATE DATABASE jwt_rbac_db;


Running the Application
Start the FastAPI server:
> uvicorn app.main:app --reload
The API will be available at http://localhost:8000.
API Documentation
Once the application is running, you can access:

Interactive API docs: http://localhost:8000/docs
Alternative API docs: http://localhost:8000/redoc

API Endpoints
Authentication

POST /api/v1/register - Register a new user
POST /api/v1/login - Login and get access token
GET /api/v1/me - Get current user information

Projects

GET /api/v1/projects/ - Get all projects (all authenticated users)
POST /api/v1/projects/ - Create a new project (admin only)
GET /api/v1/projects/{project_id} - Get a specific project (all authenticated users)
PUT /api/v1/projects/{project_id} - Update a project (admin only)
DELETE /api/v1/projects/{project_id} - Delete a project (admin only)

You can commit some curl operation via terminal as well 

This completes the Role-Based Access Control Project

Regular users can only read resources
