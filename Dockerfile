# Dockerfile for ai-communication-assistant
# Multi-stage build for backend (Python) and frontend (React)

# --- Backend Stage ---
FROM python:3.10-slim AS backend
WORKDIR /app/backend
COPY backend/ ./
RUN pip install --no-cache-dir -r requirements.txt

# --- Frontend Stage ---
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY frontend/ ./
RUN npm install && npm run build

# --- Final Stage ---
FROM python:3.10-slim
WORKDIR /app
# Copy backend from backend stage
COPY --from=backend /app/backend ./backend
# Copy frontend build from frontend stage
COPY --from=frontend /app/frontend/build ./frontend/build

# Expose backend port (adjust if needed)
EXPOSE 5000

# Start backend (adjust if your entrypoint is different)
CMD ["python", "backend/app.py"]
