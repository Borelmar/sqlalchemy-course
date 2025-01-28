FROM python:3.12-alpine3.21

RUN pip install --no-cache-dir poetry

COPY /bot /bot

WORKDIR /bot

RUN poetry install --no-interaction

ENTRYPOINT ["poetry", "run", "python", "run.py"]