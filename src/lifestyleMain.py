__author__ = "Akash Karmakar"

import logging
from concurrent.futures.thread import ThreadPoolExecutor

from camunda_external.external_task_worker import ExternalTaskWorker
from camunda_external.external_task import TaskResult
from src.lifestyleFlow import fetchExpAndSalaryTask, logResponseTask
from src.start_process import start_proc

BASE_URL = "http://localhost:8080/engine-rest"
default_config = {
    "maxTasks": 1,
    "lockDuration": 60000,  #Adujust the duration according to your choice
    "asyncResponseTimeout": 60000,
    "retries": 1,
    "retryTimeout": 50000,
    "sleepSeconds": 0,
    "isDebug": True,
}

def configure_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[logging.StreamHandler()])
    return logging.getLogger(__name__)

class Worker:
    def __init__(self, worker_id, base_url, config={}):
        self.config = config
        self.worker_id = worker_id
        self.stopped = False
        self.logger = configure_logging()
        self.worker = ExternalTaskWorker(self.worker_id, base_url, config)

    #This function will subscribe to the topic until it is completed
    def subscribe(self, topic, action, process_variables=None):
        while not self.stopped:
            self.logger.debug(f"subscribed to {topic}")
            result = self.worker._fetch_and_execute_safe(topic, action, process_variables)
            if isinstance(result, TaskResult):
                self.logger.debug(f"task completed for {topic}")
                break
    
def worker_run(base_url=BASE_URL):
    logger = configure_logging()
    logger.debug(f"Coming here in worker func: {base_url}")
    try:
        #To start a deployed process instance in camunda server
        start_proc(base_url, 'lifestyleFlow', business_key="10")
    except Exception as err:
        logger.error(f"Error starting the process: {err}")
        raise err

    #Topic name and respective function mapping
    topics = [
        ('fetchValuesTask', fetchExpAndSalaryTask),
        ('logResponseTask', logResponseTask)
    ]
    executor = ThreadPoolExecutor(max_workers=len(topics))
    
    for index, topic_handler in enumerate(topics):
        topic = topic_handler[0]
        handler_func = topic_handler[1]
        worker = Worker(worker_id=index, base_url=base_url, config=default_config)
        executor.submit(worker.subscribe(topic, handler_func))
    
    return True
