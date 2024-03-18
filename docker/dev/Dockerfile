# Pull official base image
FROM python:3.12.2-alpine3.19

# Set working directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache bash
RUN apk add --no-cache --update npm

COPY package*.json ./
RUN npm install

COPY poetry.lock pyproject.toml /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
# Install dependencies
RUN poetry install --with dev

# Copy start
COPY ./docker/dev/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY . /app

CMD ["manage.py", "runserver", "0.0.0.0:8000"]