# Desk Booking App backend :computer: :office:

![Desk Booking App](https://img.shields.io/badge/Desk%20Booking%20App-v1.0-brightgreen) [![App hosted on GCP](https://img.shields.io/badge/App%20hosted%20on%20GCP-https%3A%2F%2Fexample--app.herokuapp.com%2F-brightgreen)](https://desk-booking-backend-ouh3cj4nwa-ew.a.run.app/docs)


Welcome to the amazing Computas Desk Booking App, a web application designed to allow users to easily book desks at work. This app is built using FastAPI for the backend, Next.js for the frontend, and MongoDB for the database. It is deployed using a CI/CD pipeline to Google Cloud.

This is a repo for the backend code.

## Features :sparkles:

- User authentication and authorization
- Desk booking and management
- Desk availability display
- User profile management
- Admin dashboard for desk management and user activity tracking

## Tech Stack :gear:

- FastAPI
- MongoDB
- Google Cloud Platform

## Installation :computer:

1. Clone the repository
```
git clone https://github.com/computas/desk-booking.git
```

Install packages

```
cd desk-booking
pip install -r requirements.txt
```

Start the app
```
uvicorn app.main:app --reload
```

View it on `http://127.0.0.1:8000`


## Deployment :rocket:

The application is automatically deployed to Google Cloud using a CI/CD pipeline. To deploy the app yourself, follow these steps:

1. Create a new project on Google Cloud

2. Configure your CI/CD pipeline to build and deploy the application

3. Set up your production environment variables

4. Push your changes to the repository

5. The pipeline will automatically build and deploy your application to Google Cloud

## Contributing :handshake:

Contributions are always welcome! If you have any ideas or suggestions for the project, please create an issue or submit a pull request.

## License :scroll:

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more information.



