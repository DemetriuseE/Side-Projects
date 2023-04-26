give_me_your_name = "What is your name?"
print(give_me_your_name)
name = input()
Learning_how_to_manage_time_1 = f"Hello there {name}. Thank you for taking some time out of your day for self care in time management."
Learning_how_to_manage_time_2 = "There are 365 days in a year. 12 months a year. 28,30,31 days in a month. 7 days a week. and 1440 hours within one day."
Learning_how_to_manage_time_3 = "Most of us don't actually talk about the amount of time we spend during each day."
Learning_how_to_manage_time_4 = "Most of us don't normally think about the fact that we spend 480 minutes each day for 8 hours of sleep."
Learning_how_to_manage_time_5 = "Many of us might not realize that we spend another 480 hours a day trying to work an 8 hour shift."
Learning_how_to_manage_time_6 = "However once we realize that 960 of 1440 hours have been utilized for day to day adulting, we realize we have more time left."
Learning_how_to_manage_time_7 = "Which leaves us with the remainder of 480 hours left."
Learning_how_to_manage_time_8 = "Some of us have commutes to work that require 60, 120 minutes."
Learning_how_to_manage_time_9 = "But we'll dive more into all of this shortly."
Learning_how_to_manage_time_10 = "Let's dive into your personal schedule to get a better assesment of where your time is utilized."
full_versus_part = f" {name} are you a full-time employee or a part-time employee?"
employment_status_full = "full_time"
employment_status_part = "part-time"
Commute_to_work = "Do you commute to work?"
Commute_to_work_time_spent = "How much time does it take for you to commute to work (in minutes)?"
part_time_hours_left = 720
full_time_hours_left = 480
commute_to_work_input_instructions = ("Press [0] for yes otherwise just press [enter]")
#### Commute_to_work_total_multiple_jobs = "Overall, how much time does it take you to commute to work between all jobs?" #To be used later#
#Most variables lay here.#
print()
print(Learning_how_to_manage_time_1)
print(Learning_how_to_manage_time_2)
print(Learning_how_to_manage_time_3)
print(Learning_how_to_manage_time_4)
print(Learning_how_to_manage_time_5)
print(Learning_how_to_manage_time_6)
print(Learning_how_to_manage_time_7)
print(Learning_how_to_manage_time_8)
print(Learning_how_to_manage_time_9)
print(Learning_how_to_manage_time_10)
print()
print(full_versus_part)
print("If full-time press [0] or part time [1] then press [enter]")
employment_status = int(input())
if employment_status == 0:
    print(employment_status_full)
    employment_status = employment_status_full
    #Start up sequence for full-time time management#
    print(f"Because you are a {employment_status} employee you have a total of 480 minutes left or 8 hours {name}")
    print(Commute_to_work)
    print(commute_to_work_input_instructions)
    commute_to_work_response = int(input())
    if commute_to_work_response == 0:
        print(Commute_to_work_time_spent)
        getting_to_work = int(input())
        full_time_hours_left_with_commute = int(full_time_hours_left) - int(getting_to_work)
        full_time_remaining_daily_hours = f"{name} you have {full_time_hours_left_with_commute} minutes left."
        print(full_time_remaining_daily_hours)
        convert_to_hours = int(full_time_hours_left_with_commute) / 60
        daily_amount_of_free_hours_left = convert_to_hours
        print(f"{daily_amount_of_free_hours_left} is the amount of total free time left after commuting to work and sleep.")
        #Make a function that contains the input for the first part, that subtracts it from the total amount of minutes left#
    else:
        print(full_time_hours_left)
    convert_to_hours = int(full_time_hours_left) / 60
    daily_amount_of_free_hours_left = int(convert_to_hours)
    print(f"You have this amount of free time left daily {daily_amount_of_free_hours_left}(hours)")
if employment_status == 1:
    print(employment_status_part)
    employment_status = employment_status_part
    #Start up sequence for part-time time management#
    print(f"Because you are a {employment_status} employee you have a total of 720 minutes left or 12 hours {name}")
    print(Commute_to_work)
    print(commute_to_work_input_instructions)
    commute_to_work_response = int(input())
    if commute_to_work_response == 0:
        print(Commute_to_work_time_spent)
        getting_to_work = int(input())
        #Make a function that contains the input for the first part, that subtracts it from the total amount of minutes left#
        part_time_hours_left_with_commute = int(part_time_hours_left) - int(getting_to_work)
        part_time_remaining_daily_hours = f" {name} you have {part_time_hours_left_with_commute} minutes left each day."
        print(part_time_remaining_daily_hours)
    else:
        print()
    convert_to_hours = int(part_time_hours_left) / 60
    daily_amount_of_free_hours_left = int(convert_to_hours)
    print(f"{name}, you have {daily_amount_of_free_hours_left} hours left in a day for free time.")

#Might need to update for people that work two jobs. This only tackles the amount of hours a person would traditionally have working either of these averages#
#Later need an update for people that have a specific amount of hours allocated to working work. Might have to change the entire functionality to tackle if they work two jobs.#
#Then create a special sequence for those that work multiple jobs and have to commute for them.#