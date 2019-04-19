from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    def s1_200ms1k(self):

        with self.client.get("/service/s1/200ms/1k", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "https://dmp-n1.daocloud.io"
    min_wait = 0
    max_wait = 0