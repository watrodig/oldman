FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/api
COPY requirements.txt /app/api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install --upgrade djangorestframework 

RUN pip install six

RUN pip install mysqlclient
RUN pip install drf-generators
RUN pip install --upgrade django-cors-headers



EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]