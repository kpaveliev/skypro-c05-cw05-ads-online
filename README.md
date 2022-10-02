# SkyPro.Python course
## CW05. Skymarket - avito-like ads site

### Implementation

1. Backend: django restframework
2. Database: postgresql 
3. Backend-server: gunicorn
4. Web-server: nginx (from docker image)
5. Frontend: react (was provided)

frontend available at: localhost:3000  
backend at: localhost:8000

### How to launch django project in development

1. Create virtual environment
2. Install dependencies
3. Set environment variables in .env file
   - create .env file in backend_django folder
   - you can copy the default variables from backend_django/.env.example
4. Launch database from deploy folder
   - `cd deploy`
   - `docker compose --env-file ../backend_django/.env -f docker-compose.db.yaml up -d`
5. Make migrations from todolist folder
   - `cd backend_django`
   - `./manage.py makemigraitons`
   - `./manage.py migrate`
6. Launch project
   - `./manage.py runserver`

### How to launch dockerized project

`cd deploy`
`docker-compose --env-file ./backend_django/.env -f docker-compose.dev.yaml up -d`

### How to deploy to prod


Kirill Paveliev  
September 2022