# 📌 CareFlow OPD — Smart Patient Management System

A full-stack **Hospital Outpatient Department (OPD) Management System** built using:

* ⚡ FastAPI (Backend)
* 🗄️ SQLite + SQLAlchemy (Database)
* 🌐 HTML, CSS, JavaScript (Frontend)
* ☁️ Railway (Deployment backend)
* 🌍 Vercel / Static Hosting (Frontend optional)

---

## 🚀 Features

### 👨‍⚕️ User Roles

* Admin
* Doctor
* Receptionist

### 🏥 Core Modules

* Patient Registration
* Token Queue System (FIFO)
* Doctor Management
* Login Authentication (Role-based)
* Real-time OPD Queue View
* Admin Dashboard Support

---

## 🏗️ Tech Stack

| Layer      | Technology                                          |
| ---------- | --------------------------------------------------- |
| Frontend   | HTML, CSS, JavaScript                               |
| Backend    | FastAPI (Python)                                    |
| Database   | SQLite (SQLAlchemy ORM)                             |
| Deployment | Railway (Backend), Vercel/Static Hosting (Frontend) |

---

## 📂 Project Structure

```
CareFlow-OPD/
│
├── backend/
│   ├── main.py
│   ├── patients.db
|   |__test_main.py
│   ├── models (SQLAlchemy tables)
│
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── login.html
│   ├── doctor.html
│   ├── receptionist.html
├── tests/
│   │   ├── test_login.py
│   │   ├── test_patients.py
│   │   ├── test_doctors.py
│   │   └── test_tokens.py   
│
└── README.md
|___AI_prompts.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/careflow-opd.git
cd careflow-opd
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend
pip install fastapi uvicorn sqlalchemy
```

Run server locally:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### 🔐 Authentication

```
POST /login
```

### 👤 Patients

```
POST /register-patient
GET  /patients
```

### 👨‍⚕️ Doctors

```
POST /add-doctor
GET  /doctors
DELETE /delete-doctor/{id}
```

### 🎟 Tokens

```
POST /generate-token/{patient_id}
GET  /tokens
```

---

## 🌍 Deployment

### 🚀 Backend (Railway)

1. Push backend to GitHub
2. Connect Railway
3. Add Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

4. Copy Railway URL:

```
https://your-app.up.railway.app
```

---

### 🌐 Frontend (Vercel / Netlify)

Update API base in frontend:

```js
const API_BASE = "https://your-railway-url.up.railway.app";
```

Then deploy static files.

---

## 🔐 Login Credentials (Demo)

| Role         | Username     | Password |
| ------------ | ------------ | -------- |
| Admin        | admin        | 12345@   |
| Receptionist | reception    | 12345@   |
| Doctor       | shanzaymalik | 12345@   |

---

## ⚠️ Important Notes

* ❗ Do NOT use `127.0.0.1` in production
* ❗ Ensure CORS is enabled in FastAPI
* ❗ Railway provides dynamic PORT → must use `$PORT`
* ❗ Frontend must use Railway backend URL

---

## 🧠 Common Issues

### ❌ Failed to fetch

✔ Wrong API URL
✔ Backend not running
✔ CORS issue

### ❌ 404 Not Found

✔ Wrong endpoint (/login vs /api/auth/login)

---

## 👨‍💻 Author

Eman Fatima,
Zainab Rafaqat
**CareFlow OPD — Smart Hospital Queue Management System**

---

## 📌 Future Improvements

* JWT Authentication
* Real-time WebSockets queue updates
* MongoDB / PostgreSQL upgrade
* Mobile app (Flutter / Kotlin)
* Analytics dashboard


