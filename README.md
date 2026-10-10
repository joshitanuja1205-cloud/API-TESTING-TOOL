
# API Security Testing Tool

An educational cybersecurity project designed to test authorized APIs for common security vulnerabilities and misconfigurations.

## Technology Stack

- **Frontend:** React.js, Vite
- **Backend:** Python, FastAPI
- **HTTP Client:** HTTPX
- **Database:** MongoDB (planned)

## Current Progress

- [x] Initial React frontend scaffold
- [x] FastAPI backend setup
- [x] Health-check endpoint
- [x] Interactive API documentation
- [ ] HTTPX-based security testing engine
- [ ] MongoDB scan history
- [ ] Vulnerability findings dashboard
- [ ] Security report generation

## Getting Started

### Backend Setup

Open a terminal:

    cd backend
    python3 -m venv .venv

Activate the environment on macOS/Linux:

    source .venv/bin/activate

Install dependencies:

    python -m pip install fastapi "uvicorn[standard]" httpx pymongo

Start the server:

    python -m uvicorn main:app --reload

Open the API documentation at:

    http://127.0.0.1:8000/docs

Health check:

    http://127.0.0.1:8000/api/health

### Frontend Setup

Open a second terminal:

    cd frontend
    npm install
    npm run dev

Open the local URL printed by Vite, usually http://localhost:5173.

## Planned Security Checks

- Security header analysis
- Authentication and authorization testing
- Input validation checks
- Rate-limiting analysis
- JWT configuration checks
- Object-level authorization testing using controlled test accounts

## Responsible Use

Only test APIs you own or have explicit permission to assess. Use non-destructive tests, controlled environments, and appropriate request limits.

## Project Status

Early development. Additional security checks, persistent storage, and reporting features are planned.
