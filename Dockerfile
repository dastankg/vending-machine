FROM python:3.12-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y netcat-openbsd

RUN pip install --upgrade pip

COPY requirements.txt  /app/
COPY entrypoint.sh /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh


CMD ["/app/entrypoint.sh"]