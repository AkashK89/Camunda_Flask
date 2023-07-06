from camunda.client.engine_client import EngineClient

def start_proc(base_url, process_key, variables={}, business_key=None):
    client = EngineClient(engine_base_url=base_url, config={"auth_basic": {"username": "demo", "password": "demo"}})
    return client.start_process(process_key=process_key, variables=variables, business_key=business_key)
