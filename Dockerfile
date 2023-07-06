# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV FLASK_DEBUG=1

#You can set the camunda host and port here
ENV CAMUNDA_HOST=
ENV CAMUNDA_PORT=

CMD ["python3", "views.py"]