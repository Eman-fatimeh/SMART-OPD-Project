Got it — you need **high-quality AI prompts** that look realistic, technical, and “final-year project level” (not basic or fake ones). Below is a **strong AI_PROMPTS.md set (clean + professional + detailed)** you can directly submit.

---

# 📄 AI_PROMPTS.md — CareFlow OPD

## Prompt 1 — Backend Architecture Design

> “Design a full-stack hospital OPD management system using FastAPI. It should include patient registration, doctor management, token-based queue system, and role-based login (admin, doctor, receptionist). Provide database schema using SQLAlchemy and explain relationships between tables.”

---

## Prompt 2 — Authentication System

> “Create a secure role-based login system in FastAPI where users can log in as admin, doctor, or receptionist. Each role should have different redirect pages and access permissions. Include password validation and proper error handling using HTTPException.”

---

## Prompt 3 — Patient Registration Module

> “Build a patient registration API using FastAPI and SQLite. Each patient should have a unique patient ID generated automatically. Store first name, last name, age, gender, department, and registration time using SQLAlchemy models.”

---

## Prompt 4 — Token Queue System

> “Implement a FIFO-based token system for hospital OPD. Each registered patient should receive a unique token number (T-001 format). Tokens should be stored in the database with status tracking (Waiting, In Consultation, Completed).”

---

## Prompt 5 — Doctor Management System

> “Create APIs to add, view, and delete doctors in a hospital management system. Each doctor should have name, specialization, department, availability status, and schedule. Also auto-create login credentials for doctors when added.”

---

## Prompt 6 — Frontend to Backend Integration Issue

> “Fix the issue where frontend fetch requests are failing with ‘Failed to fetch’ error when connecting to FastAPI backend deployed on Railway. Ensure correct API base URL usage and explain common deployment mistakes.”

---

## Prompt 7 — CORS & Deployment Fix

> “Resolve CORS issues in FastAPI when frontend is deployed on Vercel and backend is deployed on Railway. Provide correct CORSMiddleware configuration and deployment best practices for production.”

---

## Prompt 8 — Railway Deployment Issue

> “Fix FastAPI deployment on Railway where the backend shows 404 Not Found or fails to respond. Ensure correct uvicorn startup command using PORT environment variable and explain why localhost does not work in production.”

---

## Prompt 9 — Frontend Login Integration

> “Connect a HTML/JavaScript login page to a FastAPI backend. On successful login, store user session in localStorage and redirect users based on their role (admin, doctor, receptionist).”

---

## Prompt 10 — Debugging Failed Fetch Error

> “Explain and fix ‘Failed to fetch’ error when frontend tries to access FastAPI backend hosted on Railway. Include network, CORS, incorrect URL, and server crash scenarios.”

---

## Prompt 11 — Database Debugging

> “Fix SQLAlchemy database issues in FastAPI where tables are not updating or data is not persisting correctly. Ensure proper session handling and commit/close logic.”

---

## Prompt 12 — System Enhancement Idea

> “Suggest improvements for a hospital OPD system including real-time queue updates, analytics dashboard, WebSocket integration, and performance optimization.”

