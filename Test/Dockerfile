FROM python:3.9.0-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app /code/app
RUN ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
