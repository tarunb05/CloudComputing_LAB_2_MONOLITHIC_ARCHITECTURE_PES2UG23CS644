from locust import HttpUser, task, between
import random

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        self.users = ["locust_user", "test_user", "demo_user"]

    @task
    def view_my_events(self):
        user = random.choice(self.users)
        with self.client.get(
            f"my-events?user={user}",
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status code: {response.status_code}")
