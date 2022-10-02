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

1. Create virtual environment and install dependencies
- `poetry install`
2. Set environment variables in .env file
   - create .env file in backend_django folder
   - you can copy the default variables from backend_django/.env.example
3. Launch database from deploy folder
   - `cd deploy`
   - `docker compose --env-file ../backend_django/.env -f docker-compose.db.yaml up -d`
4. Make migrations from todolist folder
   - `cd backend_django`
   - `./manage.py makemigraitons`
   - `./manage.py migrate`
5. Launch project
   - `./manage.py runserver`

### How to launch dockerized project

`cd deploy`
`docker-compose --env-file ./backend_django/.env -f docker-compose.dev.yaml up -d`

### Deploy to prod

1. Deploy is configured through github actions
   - both front and back images are built
2. Results are available at:
   - http://kpaveliev-skypro.cf




Kirill Paveliev  
September 2022