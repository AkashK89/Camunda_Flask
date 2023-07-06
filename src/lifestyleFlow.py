__author__ = "Akash Karmakar"

import random
from camunda_external.external_task import ExternalTask


def fetchExpAndSalaryTask(task: ExternalTask):
    try:
        totalExp = random.randint(0, 30)
        if totalExp <= 5:
            salary = random.randint(100000, 1000000)
        elif totalExp > 5 and totalExp <= 10:
            salary = random.randint(300000, 3000000)
        else:
            salary = random.randint(1500000, 15000000)
        
        return task.complete(local_variables={"result_totalExperience": totalExp, "result_salary": salary})
    except Exception as err:
        print(f"Oh no! Something went wrong: {err}")
        return task.failure(
            error_message=err.__class__.__name__,
            error_details=str(err),
            max_retries=3,
            retry_timeout=5000,
        )
    
def logResponseTask(task: ExternalTask):
    if task.get_variable('final_decision'):
        if task.get_variable('final_decision') == "yes":
            print("User decides to quit his job")
        else:
            print("User wants to continue his current job")
    else:
        if task.get_variable('feedback') == "yes":
            print(f"User is very happy with his current job")
        elif task.get_variable('feedback') == "no":
            print(f"User is looking for a new job")
    return task.complete()
