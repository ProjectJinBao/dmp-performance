from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    def configure1(self):
        with self.client.get("/configs/bipkfrfmfi.123456/default/application", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

    @task
    def configure2(self):
        with self.client.get("/configs/bipkfrfmfi.performance/default/application", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "http://192.168.0.83:31121"
    min_wait = 0
    max_wait = 0