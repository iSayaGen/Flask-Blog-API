# Flask Blog API

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Swagger](https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?logo=swagger&logoColor=000000)](https://swagger.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A simple RESTful Blog API built with **Python and Flask**, with a lightweight frontend.

## Features

- CRUD operations for blog posts
- Search posts by title and content
- Sort posts by title or content
- Interactive Swagger API documentation
- CORS support
- Simple web frontend

## Tech Stack

**Backend:** Python · Flask · Flask-CORS  
**Frontend:** HTML · CSS · JavaScript  
**Documentation:** Swagger UI

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Flask-Blog-API
```

### 2. Create a virtual environment

A virtual environment keeps the project's dependencies isolated from other Python projects.

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend

```bash
python backend/backend_app.py
```

The API runs at:

```text
http://localhost:5002
```

The frontend runs separately using `frontend/frontend_app.py`.

## API Documentation

Interactive Swagger documentation:

**http://localhost:5002/api/docs**

The Swagger UI contains the complete API documentation, including parameters, request bodies, and responses.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/posts` | List posts |
| `POST` | `/api/posts` | Create a post |
| `GET` | `/api/posts/search` | Search posts |
| `PUT` | `/api/posts/{post_id}` | Update a post |
| `DELETE` | `/api/posts/{post_id}` | Delete a post |

## Project Structure

```text
Flask-Blog-API/
├── backend/
│   ├── static/
│   │   └── masterblog.json
│   └── backend_app.py
├── frontend/
│   ├── static/
│   │   ├── main.js
│   │   └── styles.css
│   ├── templates/
│   │   └── index.html
│   └── frontend_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.