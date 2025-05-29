FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# TEMPORARILY enable DEBUG during build to avoid collectstatic crash
ENV DEBUG=True

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (only works in DEBUG=True without WhiteNoise errors)
RUN python manage.py collectstatic --no-input

# Apply migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Set back to production mode by default
ENV DEBUG=False

# Run Uvicorn ASGI app
CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "5005", "--log-level", "debug", "--reload"]
