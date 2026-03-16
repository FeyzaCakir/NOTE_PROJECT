# NOTE_PROJECT
A simple agenda and note-taking web application built with Flask, featuring user authentication, CRUD operations, and SQLite database integration.
# 📝 Agenda App (Flask)

A simple **agenda / note management web application** built with **Flask**.
Users can register, log in, and manage their personal notes by creating, updating, deleting, and marking them as completed.

The project demonstrates basic **backend development concepts**, including authentication, CRUD operations, session management, and database interaction using SQLite.

---

## 🚀 Features

* 🔐 User Authentication (Register / Login / Logout)
* 📝 Create new notes
* ✏️ Update existing notes
* ❌ Delete notes
* ✅ Mark notes as completed
* 📅 Date formatting for notes
* 👤 User profile page
* 🔒 Password hashing for security

---

## 🛠 Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **Werkzeug Security**
* **Jinja2 Templates**
* **HTML / CSS**
* **dotenv**

---

## 📂 Project Structure

```
agenda-app/
│
├── app.py
├── agenda.db
├── .env
│
├── templates/
│   ├── index.html
│   ├── ekle.html
│   ├── update.html
│   ├── login.html
│   ├── register.html
│   └── profile.html
│
└── static/
    └── css/
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/agenda-app.git
cd agenda-app
```

2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac / Linux

```bash
source venv/bin/activate
```

3️⃣ Install dependencies

```bash
pip install flask python-dotenv werkzeug
```

4️⃣ Create a `.env` file

```
SECRET_KEY=your_secret_key
```

5️⃣ Run the application

```bash
python app.py
```

Application will run at:

```
http://127.0.0.1:5000
```

---

## 🗄 Database

The project uses **SQLite** as the database.

Main tables:

### users

| Field    | Type    |
| -------- | ------- |
| id       | INTEGER |
| username | TEXT    |
| password | TEXT    |

### notes

| Field   | Type    |
| ------- | ------- |
| id      | INTEGER |
| title   | TEXT    |
| content | TEXT    |
| date    | TEXT    |
| done    | INTEGER |

---

## 🔐 Authentication

Authentication is implemented using:

* Flask **sessions**
* **password hashing** with `werkzeug.security`
* user validation during login

Passwords are never stored as plain text.

---

## 🎯 Learning Objectives

This project was built to practice:

* Flask routing
* CRUD operations
* Database operations with SQLite
* Session-based authentication
* Password hashing
* Template rendering with Jinja2
* Basic backend project structure

---

## 📸 Future Improvements

Possible improvements for the project:

* User-specific notes
* REST API version of the application
* Frontend improvements (JavaScript / React)
* Pagination for notes
* Search functionality
* Deployment (Docker / Cloud)

---

## 👩‍💻 Author

Developed by **Feyza Çakır**
