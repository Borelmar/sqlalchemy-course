FROM python:3.13.1-alpine3.21

# RUN apk add libpq-dev python3-dev

WORKDIR /app

COPY /app /app

RUN pip install --root-user-action ignore -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
# ENTRYPOINT ["/bin/sh"]
