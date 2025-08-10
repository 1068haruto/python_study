FROM python:3.13-slim

WORKDIR /code

COPY ./requirements.lock /code/requirements.lock
RUN pip install --no-cache-dir --upgrade -r /code/requirements.lock

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]