# Demonstrating the use of enumerate()
# We have a list of tasks to complete, and we want to print each task with its corresponding number.

# TO DO : use enumerate() to get index and task from the list, and print "Task i: task"

tasks_to_do = ["Wash the car", "Buy some food", "Bath the dog", "Prepare for the meeting", "Call Mom", "Read a book", "Go for a walk", "Cook dinner", "Sleep"]
for index, task in enumerate(tasks_to_do, start=1):
    print(f"Task #{index}: {task}")
