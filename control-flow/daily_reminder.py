#

task = input("Enter your task: " )

priority = input("Priority (high/medium/low):" )

time_bound = input("Is it time-bound? (yes/no):" )

# print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today! ")

match time_bound:
    # case "yes":
    #     print (f"Reminder: {task} is a high priority task that requires immediate attention today!")

    # case "no":
    #     print (f"Note: {task} is a low priority task. Consider completing it when you have free time.")

    case "high":
        if time_bound == "yes":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")


    case "low":
        if time_bound == "yes":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")
        # print (f"Reminder: {task} is a low priority task that requires immediate attention today!")

    case "medium":
        # print (f"Reminder: {task} is a medium priority task that requires immediate attention today!")

        if time_bound == "yes":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print (f"Reminder: {task} is a high priority task that requires immediate attention today!")


    





