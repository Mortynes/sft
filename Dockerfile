FROM python:3.11

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/sft_site

RUN python manage.py collectstatic

CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 sft_site.wsgi:application

