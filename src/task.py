from datetime import datetime, timedelta
from enum import Enum
from database import dbUpdate, dbGetTaskList

class ResetFrequency(Enum):
    DAILY = 1
    WEEKDAY = 2
    WEEKLY = 3
    WORKWEEKLY = 4
    BIWEEKLY = 5
    MONTHLY = 6
    QUARTERLY = 7
    BIANNUALLY = 8
    ANNUALLY = 9

class TaskState(Enum):
    READY = 1
    CURRENT = 2
    PAUSED = 3
    FINISHED = 4
    DANGER = 5
    OVERDUE = 6

# Task Object
class Task:
    current_task = None
    task_colors = [
        "#ffffff",              # white - not used, but need to fill this list space
        "#11c807",              # 1 - green - ready
        "#3707C8",              # 2 - blue - current
        "#11c807",              # 3 - green - paused (ready to restart)
        "#000000",              # 4 - black - finished for this period
        "#C3D006",              # 5 - yellow - danger
        "#BF0707"               # 6 - red - overdue
    ]
    task_color_pairs = [
        ("black", "#ffffff"),    # black on white - not used, but need to fill this list space
        ("white", "#11c807"),    # 1 - white on green - ready
        ("white", "#3707C8"),    # 2 - white on blue - current
        ("white", "#11c807"),    # 3 - white on green - paused (ready to restart)
        ("white", "#000000"),    # 4 - white on black - finished for this period
        ("black", "#C3D006"),    # 5 - black on yellow - danger
        ("white", "#BF0707")     # 6 - white on red - overdue

    ]

    def __init__(self, name, desc="Default Task Description", priority=3, frequency=ResetFrequency.DAILY):
        # user supplied and user editable fields...
        self.name = name
        self.description = desc[:(len(desc) if len(desc) < 256 else 256)]
        self.priority = priority if (priority > 0 and priority < 6) else 3
        self.frequency = frequency
        self.reset = timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        self.target = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=1, weeks=0)
        # internal fields...
        self.created = datetime.now()
        self.state = TaskState.READY
        self.time_total = None
        self.time_session = None
        self.dtg_session_paused = None
        self.dtg_session_start = None
        self.dtg_session_stop = None

    def change_task_state(self):
        # if no task is "running" then clicking a button makes that task current, active and running
        if Task.current_task == None:
            Task.current_task = self
            Task.current_task.start_task()
            return Task.get_current_task()

        # if a task is "running" then clicking the button for that task
        #       - pauses the task if the task's target for the reset period has not been reached
        #       - finished the task if the task's target for the reset period has been reached
        if Task.current_task == self:
            Task.current_task.pause_task()
            Task.current_task = None
            return Task.get_current_task()
        
        # if a task is "running" then clicking another task's button switches to that new task and makes
        #     it active and running
        # 
        if Task.current_task != self and Task.current_task != None:
            Task.current_task.pause_task()
            Task.current_task = self
            Task.current_task.start_task()
            return Task.get_current_task()

    def saveToDatabase(self, cursor):
        # convert the task into text strings and integers that can be
        # saved in the database
        fldValues = self.__dict__
        # call dbUpdate(cursor, tableName, <key tuple>, <values dictionary>) to 
        # update or insert the record as appropriate
        dbUpdate(cursor, 'tasks', key=('name', fldValues['name']), values=fldValues)
        pass

    def get_current_task():
        return Task.current_task
    
    def clear_current_task():
        if Task.current_task != None:
            Task.current_task.pause_task()
            Task.current_task = None

    def start_task(self):
        self.state = TaskState.CURRENT
        pass

    def pause_task(self):
        self.state = TaskState.PAUSED
        pass

    def finish_task(self):
        self.state = TaskState.FINISHED
        pass

    def clean_up_for_exit():
        Task.clear_current_task()  

    def getTaskList(cursor):
        taskList = dbGetTaskList(cursor)
        return taskList

def testTaskList(count=10):
    taskList = []
    for tID in range(count):
        taskList.append(Task(f"Task {tID}", "New Task", tID))
    
    return taskList
