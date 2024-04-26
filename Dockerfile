FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

# Add makemigrations and migrate commands
RUN python manage.py makemigrations
RUN python manage.py wait_for_db
RUN python manage.py migrate

RUN python manage.py scraper