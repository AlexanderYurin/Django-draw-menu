FROM python:3.11-alpine3.16
COPY service /service
WORKDIR /service
COPY requirements.txt /temp/requirements.txt
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

CMD ["sh", "-c", "service/python manage.py migrate && python manage.py loaddata service/app/fixtures/fixtures.json"]