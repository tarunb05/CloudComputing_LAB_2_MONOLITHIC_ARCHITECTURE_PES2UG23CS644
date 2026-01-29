from locust import HttpUser, task, between
import random

class EventsUser(HttpUser):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        self.users = ["locust_user", "test_user", "demo_user"]

    @task(3)  # Higher weight = more frequent
    def view_events(self):
        user = random.choice(self.users)
        with self.client.get(
            f"/events?user={user}",
            name="/events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"Failed with {response.status_code}")
