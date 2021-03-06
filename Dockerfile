FROM python:3.7
MAINTAINER Vladimir Pushkarev
RUN mkdir /app

ENV HOME=/app
ENV PYTHONPATH=$HOME
ENV PYTHONDONTWRITEBYTECODE yes

WORKDIR $HOME

COPY requirements.txt .
COPY manage.py .
COPY entry_point.sh .
RUN apt-get update && apt-get install -y wait-for-it --no-install-recommends
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
RUN pip freeze
COPY fishing fishing
COPY app app
COPY blog blog
RUN python manage.py collectstatic --noinput
RUN chmod +x entry_point.sh
