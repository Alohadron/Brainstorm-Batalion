import random
import datetime

def date() -> None:
    now = datetime.datetime.now()
    print(f"Current time: {now}")

    duration = datetime.timedelta(hours=4, minutes=30)
    Time_until_leisure = now + duration
    print(f"Time until leisure: {Time_until_leisure}")

def hobby() -> None:
    hobbies = ['learning python', 'reading books', 'a walk in park']
    leisure = random.choice(hobbies)
    print(f'A hobby for leisure time today will be: {leisure}')

date()
hobby()