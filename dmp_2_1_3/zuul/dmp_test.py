from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    def s1_200ms1k(self):

        with self.client.get("/test-zuul/s1/500ms/1k", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "http://192.168.1.23:30452"
    # host = "http://192.168.0.105:31251"
    min_wait = 0
    max_wait = 0