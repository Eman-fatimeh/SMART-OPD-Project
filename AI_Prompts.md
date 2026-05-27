# 📄 AI_PROMPTS.md — CareFlow OPD Management System

## Prompt 1 — Backend Architecture Design

> “Design a full-stack hospital OPD management system using FastAPI. The system should support patient registration, doctor management, token-based queue handling, and role-based authentication for admin, doctors, and receptionists. Generate SQLAlchemy database models and explain how tables should relate to each other.”

### AI Usage Summary

AI generated the initial backend architecture including FastAPI routes, SQLAlchemy models, and API structure.

### Manual Refinement

I modified database fields, improved endpoint naming, and customized role permissions according to project requirements.

---

## Prompt 2 — Authentication System

> “Create a secure role-based login system in FastAPI where users can log in as admin, doctor, or receptionist. Each role should redirect to a different dashboard page after login. Include proper validation, JSON responses, and HTTPException handling.”

### AI Usage Summary

AI generated login API logic and role checking functionality.

### Manual Refinement

I customized redirects for admin.html, doctor.html, and register.html and improved frontend integration with localStorage.

---

## Prompt 3 — Patient Registration Module

> “Build a patient registration API using FastAPI and SQLite. Each patient should receive an automatically generated patient ID. Store first name, last name, age, gender, department, and registration time using SQLAlchemy.”

### AI Usage Summary

AI generated the patient registration API and database table schema.

### Manual Refinement

I adjusted the patient ID generation logic and customized the response format for frontend dashboard usage.

---

## Prompt 4 — Token Queue System

> “Implement a FIFO-based hospital token system where each patient receives a unique token number in T-001 format. Store token status such as Waiting, In Consultation, and Completed in the database.”

### AI Usage Summary

AI generated token numbering logic and queue API endpoints.

### Manual Refinement

I customized queue rendering on the frontend and added dynamic queue status updates.

---

## Prompt 5 — Doctor Management System

> “Create APIs for adding, viewing, and deleting doctors in a hospital management system. Each doctor should contain specialization, department, schedule, and availability status. Automatically create login credentials for doctors.”

### AI Usage Summary

AI created CRUD endpoints for doctor management and auto-user creation logic.

### Manual Refinement

I improved doctor dashboard integration and modified doctor username generation.

---

## Prompt 6 — Frontend to Backend Integration

> “Fix frontend fetch requests failing while connecting HTML/JavaScript frontend with FastAPI backend deployed on Railway. Explain proper API base URL usage and production deployment differences.”

### AI Usage Summary

AI identified incorrect localhost API usage after deployment.

### Manual Refinement

I replaced localhost URLs with Railway deployment URLs and updated fetch requests across frontend pages.

---

## Prompt 7 — CORS and Deployment Configuration

> “Resolve CORS issues between Vercel frontend and Railway FastAPI backend. Provide proper CORSMiddleware configuration and explain secure production deployment practices.”

### AI Usage Summary

AI generated CORS middleware configuration for FastAPI.

### Manual Refinement

I updated allowed origins and tested cross-origin requests after deployment.

---

## Prompt 8 — Railway Deployment Debugging

> “Fix FastAPI deployment issues on Railway where the application shows 404 Not Found or deployment startup failures. Configure uvicorn properly using the PORT environment variable.”

### AI Usage Summary

AI explained production deployment differences and startup configuration.

### Manual Refinement

I updated Railway deployment settings and verified live API endpoints.

---

## Prompt 9 — Frontend Login Integration

> “Connect a modern HTML/CSS/JavaScript login page with FastAPI backend authentication. Store authenticated sessions in localStorage and redirect users according to their roles.”

### AI Usage Summary

AI generated fetch-based login functionality and role-based redirects.

### Manual Refinement

I improved loading states, validation messages, and UI responsiveness.

---

## Prompt 10 — Failed Fetch Error Debugging

> “Explain and fix ‘Failed to fetch’ errors occurring between deployed frontend and backend applications. Include possible causes such as incorrect URLs, server downtime, CORS, and deployment failures.”

### AI Usage Summary

AI provided deployment debugging steps and networking explanations.

### Manual Refinement

I verified backend availability, corrected API URLs, and updated frontend fetch configurations.

---

## Prompt 11 — Database Session Handling

> “Fix SQLAlchemy database issues in FastAPI where data is not saving correctly. Ensure proper database session creation, commit handling, and connection closing.”

### AI Usage Summary

AI generated improved session management logic for SQLite database operations.

### Manual Refinement

I updated commit and close handling inside CRUD APIs and verified data persistence.
