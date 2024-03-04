FROM python:3.11.7-slim-bullseye

RUN mkdir /app
COPY ./app.py ./requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5001
CMD ["python", "app.py"]
