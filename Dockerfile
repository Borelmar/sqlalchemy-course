FROM python:3.12-alpine3.21

WORKDIR /app

COPY /app /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "database.py"]