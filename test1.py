"""
You have to find the minimum number of processors required to execute jobs as and when they come.


T1 - 12:00 AM	6:00 PM   -> 18hrs   a
T2 -  2:00 AM      	8:00 AM  ->  6hrs     b
T3 - 5:00 PM		7:00 PM  ->  2hrs     b
T4 - 12:00 PM	11.59 PM  -> 12hrs  c
T5 - 8:00 PM		10:00 PM  -> 2hrs    b

Processor = [{“name”: “p1”, “status”: false, task: none}, {“name”: “p2”, “status”: false}]

For task in tasks:
	

"""

from datetime import datetime
import time


"Tasks needs to be sorted"
tasks = [
    {"name": "Task1", "start": "12:00AM", "end": "6:00PM"},
    {"name": "Task2", "start": "2:00AM", "end": "8:00AM"},
    {"name": "Task4", "start": "12:00PM", "end": "11:59PM"},
    {"name": "Task3", "start": "5:00PM", "end": "7:00PM"},
    {"name": "Task5", "start": "8:00PM", "end": "10:00PM"},
]

newlist = sorted(tasks, key=lambda d: d['start']) 

print(newlist)

ongoing_task = []

list_of_processors = ["p1", "p2", "p3", "p4", "p5",]
processors_in_use = []
used_processors = []

for task in tasks:
    print(task, "needs processor.")
    if len(ongoing_task):
        for o_task in ongoing_task:
            # Check if the ongoing task has ended.
            s = datetime.strptime(task["start"], "%H:%M%p")
            e = datetime.strptime(o_task["end"], "%H:%M%p")
            if s > e:
                # Add to task ended
                ongoing_task.remove(o_task)
                print(o_task, "completed.")
                # Free the processor used by it.
                up = processors_in_use.pop(-1)
                # Bring it back to list_of_processors
                list_of_processors.insert(0, up)
                print(f"processor {p} free to work again.")
    
    p = list_of_processors.pop(0)
    print(f"processor {p} assigned to {task}.")
    processors_in_use.append(p)
    used_processors.append(p)
    ongoing_task.append(task)
    print(task, "started.")
    time.sleep(2)
    print("/////////////////////////////////")

print("Processors required:", len(set(used_processors)))


