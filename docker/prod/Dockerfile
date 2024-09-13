# Pull official base image
FROM python:3.12.6-alpine3.20

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN apk update
RUN pip3 install poetry
COPY ../../pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY ../.. /code

# Copy start
COPY ./docker/prod/start.sh start.sh
RUN sed -i 's/\r$//g' start.sh
RUN chmod +x start.sh
EXPOSE 8000
ENTRYPOINT ["./start.sh"]