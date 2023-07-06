# Camunda-Flask-Python3

This repository contains Camunda External Task with Flask in Python3.
Implement your BPMN Service Task in Python3.

> Python >= 3.7 is required

## Installing
```
pip install -r requirements.txt`
```
## Usage

1.  Make sure to have [Camunda](https://camunda.com/download/) running either locally or anywhere.
2.  Create a simple process model with an External Service Task and define the topic as 'topicName'.
3.  Deploy the process to the Camunda BPM engine.

## Running Camunda with Docker

To run both Camunda server and Flask application in docker container, follow the steps below:

    To run camunda server in docker
    ```
    $> docker pull camunda/camunda-bpm-platform:latest
    $> docker run -d --name camunda -p 8080:8080 camunda/camunda-bpm-platform:latest
    ```

    To run flask application in docker
    ```
    $> docker build -t <docker_image> .
    $> docker run -p 5000:5000 -e CAMUNDA_HOST=<camunda_host_ip> CAMUNDA_PORT=<camunda_port> -d <docker_image>
    ```