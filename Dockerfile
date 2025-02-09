FROM python:3.13.1-alpine3.21

RUN apk add libpq-dev python3-dev libpq

WORKDIR /app

COPY /app /app

RUN pip install --disable-pip-version-check --root-user-action ignore --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
# ENTRYPOINT ["/bin/sh"]
