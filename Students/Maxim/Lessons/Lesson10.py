import io
import os
import sys

# def process_logs():
#     #1. prepare raw log data in a stream
#     log_data = "Info: user logged in\nError: Connection failed" \
#     "\nInfo: Data received\nError: Timeout"

#     input_stream = io.StringIO(log_data)

#     #2 filter errors in a new stream
#     error_stream = io.StringIO()
#     for line in input_stream:
#         if line.startswith("Error"):
#             error_stream.write(f"[ALERT] {line}")

#     #prepare error_stream to be read
#     error_stream.seek(0)
#     error_content = error_stream.read()
# #3 use os to manage directories
#     log_dir = "logs"
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)

#     #4 save results to a file
    
#     file_path = os.path.join(log_dir, "errors.txt")
#     with open(file_path, "w") as f:
#         f.write(error_content)
#     #5 use sys to check for the --silent flag
#     if "--silent" not in sys.argv:
#         print("Proccessing completed, errors saved to logs/errors.txt")  
# if __name__ == "__main__":
#     process_logs()        

import datetime

# def deadline_manager():
#     #1 get current date and time
#     now = datetime.datetime.now() # now = a varibale that shows time from now
#     print(f"Current time: {now}")

#     #2 calculate future deadline 7 days and 3 hours)
#     duration = datetime.timedelta(days=7, hours=3)
#     deadline = now + duration
#     print(f"Deadline is set for: {deadline}")

#     #3 calculate days passed since a specific date in the past
#     project_start = datetime.datetime(2026, 1, 1)
#     time_passed = now - project_start
#     print(f"Days passed since project start: {time_passed.days}")

#     #4 format the deadline string
#     #format:day-month-year hours:min
#     formatted_deadline = deadline.strftime("%d-%m-%Y %H:%M")
#     print(f"formatted deadline: {formatted_deadline}")

#     #parse str to datetime obj
#     user_input = "2026-12-31"
#     parsed_data = datetime.datetime.strptime(user_input, "%Y-%m-%d")

#     #bonus check if workday is over (18;00)
#     end_of_day = datetime.time(18, 0, 0)
#     if now.time() > end_of_day:
#         print("The workday is over")
#     else:
#         print("Keep working!")

# if __name__ == "__main__":
#     deadline_manager()

import random

# #random number from 1 to 10
# number = random.randint(1,10)
# #choose random winner from list
# players = ["A", "B", "W", "D"]
# winner = random.choice(players)

# #change sequince of lists element
# random.shuffle(players)

# print(f"Number: {number}, Winner: {winner} shuffled: {players}")

def prize_draw():
    #1 define a list of participants
    participants = ['A', 'B', 'C', 'D', 'E', 'F']

    #2 shuffle the participants (rearrange the list order)
    random.shuffle(participants)
    print(f'Participants after shuffling: {participants}')
    #3 choose one lucky winner using random.choce
    winner = random.choice(participants)
    print(f"\nThe main winner is: {winner}")
    #4 generate a randome score to determine the prize
    #using randint to get an int between 1 and 100 

    prize_score = random.randint(1,100)
    if prize_score > 90:
        prize = "Super Prize!"
    elif prize_score > 50:
        prize = "badge"
    else:
        prize = "sticker"
    print(f"The winners score is {prize_score}, Prize: {prize}")

    #5 select 3 unique participants for consolaton prizes
    #use random.sample it picks multiple unique elements from the list
    consolation_winners = random.sample(participants, 3)
    print(f"\nConsolation prizes go to: {consolation_winners}")
if __name__ == "__main__":
    prize_draw()
