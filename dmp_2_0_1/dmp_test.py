from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    def s1_200ms1k(self):

        headers = {
            'jwt': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o"
        }

        with self.client.get("/1x/s1/sleep/1k", catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    host = "http://10.15.1.51:32681"
    # host = "http://192.168.0.105:31251"
    min_wait = 0
    max_wait = 0