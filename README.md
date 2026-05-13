# FastAPI Project

This project is a FastAPI application for managing **Users, Products, and Orders**, including relationships between them.

---

## Getting Started

Follow these instructions to set up and run the project locally.

---

## Prerequisites

Make sure you have the following installed:

* Python **3.14**
* `pip` package manager
* MySQL Server

---

## Installation

1. **Clone the repository:**

```bash
git clone <repository_url>
```

2. **Navigate into the project directory:**

```bash
cd <project_directory>
```

3. **Create a virtual environment:**

```bash
python -m venv venv
```

4. **Activate the virtual environment:**

* On Windows:

```bash
venv\Scripts\activate
```

* On macOS/Linux:

```bash
source venv/bin/activate
```

5. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Database Setup

1. Open your MySQL client (CLI or any GUI tool you prefer).

2. Create a database:

```sql
CREATE DATABASE basic_fastapi;
```

3. Create a `.env` file in the root of your project and add your database URL in the following format:

```env
DATABASE_URL="mysql+pymysql://fastapi_user:pass@localhost/basic_fastapi"
```

* Replace `fastapi_user` and `pass` with your MySQL username and password.
* `basic_fastapi` should match the database name you created.

---

## Running the Application

1. Make sure your virtual environment is activated.

2. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

3. Open your browser and go to:

* App URL:
  http://127.0.0.1:8000/

* API Documentation (Swagger UI):
  http://127.0.0.1:8000/docs

---

## Features

* User management (CRUD)
* Product management (CRUD)
* Order management (linked with users and products)
* Relational database design using MySQL
* Automatic interactive API docs via FastAPI

---

## Project Structure 

```
FastAPI_BasicCrud/
├── models/        # SQLAlchemy models
├── schemas/       # Pydantic schemas
├── services/      # Business logic
├── api/           # Routes
├── core/          # Config & database setup
├── repository/    # Database Queries
```

---

## Usage

* Use `/docs` to explore and test all endpoints interactively.
* Each entity (**User, Product, Order**) has its own set of APIs.
* Relationships allow linking orders to users and products.

---

## Notes

* Ensure MySQL is running before starting the app.
* If you change models, remember to handle migrations or recreate tables accordingly.
* Keep your `.env` file out of version control if it contains credentials.

---

