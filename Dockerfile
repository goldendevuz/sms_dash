FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files twice for correct manifest generation
ENV DEBUG=True
RUN python manage.py collectstatic --noinput

# ENV DEBUG=False
# RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "5005"]
