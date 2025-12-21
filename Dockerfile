FROM python:3.12.4-alpine3.20

WORKDIR /app

COPY . .

CMD ["python","main.py"]

