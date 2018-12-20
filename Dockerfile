FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
ADD . /code/
RUN pipenv install
RUN pipenv run python manage.py collectstatic --no-input
