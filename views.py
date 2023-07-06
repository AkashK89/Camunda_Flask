__author__ = "Akash Karmakar"

import os
from flask import Flask, abort, request
from src.lifestyleMain import worker_run, configure_logging

app = Flask(__name__)

#This environment variable is for Docker. If you run this application using docker \
#make sure you use system IPV4 address for `CAMUNDA_HOST`
camunda_host = os.environ.get('CAMUNDA_HOST', 'localhost')
camunda_port = os.environ.get('CAMUNDA_PORT', '8080')

BASE_URL = 'http://'+camunda_host+':'+camunda_port+'/engine-rest'

@app.route('/test_lifestyle_flow', methods=['GET', 'POST'])
def test_flow():
    logger = configure_logging()
    if request.method == 'POST':
        try:
            worker_run(base_url = BASE_URL)
        except Exception as err:
            logger.error(err)
            abort(500, {"error": "Internal server error"}) 
        return {}, 204
    else:
        return "<h1>Welcome to Camunda Flask Application page</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')