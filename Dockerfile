# Base image
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "sarpras.wsgi:application", "--bind", "0.0.0.0:8000"]
