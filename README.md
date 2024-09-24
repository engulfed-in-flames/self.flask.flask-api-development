# Try Flask API Development

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

This project aims to establish a comprehensive understanding of Flask API development by creating a RESTful API utilizing the Flask framework, complemented by the integration of Docker for containerization, PostgreSQL for a robust database, and SQLAlchemy for efficient object-relational mapping.

## Table of Contents

- [Try Flask API Development](#try-flask-api-development)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Quick Start](#quick-start)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Run the API with Docker](#2-run-the-api-with-docker)
      - [a. Initialize Docker Environment](#a-initialize-docker-environment)
      - [b. Run the Flask Application](#b-run-the-flask-application)
    - [3. Additional Notes](#3-additional-notes)
  - [Features](#features)
  - [Copyright](#copyright)

## Prerequisites

- Python Installation: Ensure you have Python 3.10 or later installed on your system.
- Virtual Environment: Use tools like `venv` to create a virtual environment and isolate your project's dependencies.
- Docker Installation: Install Docker Desktop or Docker Engine from [the official site](https://docs.docker.com/engine/install/)

## Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/engulfedInFlames/youtube.flask.flask-api-development.git flask-api-development
```

### 2. Run the API with Docker

#### a. Initialize Docker Environment

```sh
cd flask-api-development
docker compose up -d
```

#### b. Run the Flask Application

```sh
cd server
flask run
```

### 3. Additional Notes

To stop the Docker containers, run:

```sh
docker compose down
```

## Features

- Routing requests: Design and build RESTful APIs for various applications.
- Data handling: Connect APIs to databases and manage data effectively.
- Database Designing: Create well-structured and optimized database schemas to store and manage data efficiently.
- Technology Stack: Utilize Docker for containerization to simplify deployment and management, and SQLAlchemy for object-relational mapping (ORM) to interact with databases in a Python-friendly way.

## Copyright

This project serves as the final learning material for the course ["Try Flask API Development"](https://www.youtube.com/watch?v=Nl47u8zx8oM&list=PLOLrQ9Pn6caxBM0vaSzJdN4uD9V-DZ82L&index=1). All copyrights are owned by the course creators, and this project is intended solely for educational purposes and personal use. Any replication or commercial use of this code is prohibited without proper authorization.
