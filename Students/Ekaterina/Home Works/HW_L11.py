from datetime import datetime, timedelta
import random


now = datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

rest_time = now + timedelta(hours=4, minutes=30)
print(
    "Rest start time (in 4 hours 30 minutes):"
    f" {rest_time.strftime('%Y-%m-%d %H:%M:%S')}"
)


activities = ["Python learning", "Park walk", "Book reading"]
chosen_activity = random.choice(activities)
print(f"Randomly chosen activity for this time: {chosen_activity}")