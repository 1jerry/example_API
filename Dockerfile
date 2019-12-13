FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8
RUN pip install pipenv
WORKDIR /app
ADD Pipfile /app
ADD Pipfile.lock /app
RUN pipenv install --system --deploy --ignore-pipfile
ADD main.py /app
