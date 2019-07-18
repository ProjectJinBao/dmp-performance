from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    def s1_200ms1k(self):

        with self.client.get("/p/service/s1/200ms/1k", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "http://192.168.0.83:32677"
    # host = "http://192.168.0.105:31251"
    min_wait = 0
    max_wait = 0