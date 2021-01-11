FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

ENV FLASK_APP=src/app.py FLASK_ENV="docker"

CMD ["bash","docker-entrypoint.sh"]

