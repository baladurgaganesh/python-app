# =========================
# Stage 1 - Build Stage
# =========================
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app ./app


# =========================
# Stage 2 - Runtime Stage
# =========================
FROM python:3.12-alpine

# Create working directory
WORKDIR /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages \
                    /usr/local/lib/python3.12/site-packages

# Copy application code
COPY --from=builder /app/app ./app

# Expose application port
EXPOSE 5000

# Run application
CMD ["python", "-m", "app.main"]
