# Calendar api

The calendar feature provides functionality to manage and view events based on different date ranges. It includes the ability to retrieve events for specific days, weeks, months, and years.

## 🚀 Features

- **User Authentication:** Secure user registration and token-based authentication.
- **Event Management:** Retrieve events for specific days, weeks, months, and years.
- **API Documentation:** Redoc-powered documentation for a smooth developer experience.

## 🛠️ Tech Stack

- **Backend:** Python, Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Containerization:** Docker

## 📂 URL Endpoints
#### Authentication & User Management
- **User Registration:** `/api/user/create/`
- **User Login (Token Creation):** `/api/user/token/`
- **User Profile:** `/api/user/me/`
#### Events
- **Daily Events:** `/api/events/day/`
- **Weekly Events:** `/api/events/week/`
- **Monthly Events:** `/api/events/month/`
- **Yearly Events:** `/api/events/year/`
- **Create Event:** `/api/events/create/`
- **Retrieve, Update & Delete Event:** `/api/events/<uuid:id>/`

#### API Documentation
- **Redoc Documentation:** `/redoc/`

## 📦 Installation 
Clone the repository:
```bash
git clone https://github.com/YaroslavMarkivskyi/calendar-app.git
```
Navigate to the project directory:
```bash
cd calendar-app
```
Set up and run the application using Docker Compose:
```bash
docker-compose up --build
```
Access the application at:
- API Documentation - [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Admin Panel - [http://localhost:8000/admin/](http://localhost:8000/admin/)
##### To create a superuser after setting up the application with Docker, follow these steps:
Run the following command to enter the Docker container for your Django application:
```bash
docker-compose run --rm app sh
```
Inside the container, create a superuser using Django's createsuperuser command:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter your desired superuser credentials (username, email, and password).

Once complete, exit the container by typing:
```bash
exit
```
