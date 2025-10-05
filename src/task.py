from datetime import datetime, timedelta
from enum import Enum
from database import dbUpdate, dbGetTaskData

class ResetFrequency(Enum):
    DAILY = 1
    WEEKDAY = 2
    WEEKLY = 3
    WORKWEEKLY = 4
    BIWEEKLY = 5
    MONTHLY = 6
    QUARTERLY = 7
    SEMIANNUALLY = 8      # twice a year, basically every 6 months
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

    # the number of days in each of the ResetFrequencies
    day_counts = {
        "DAILY": 1,
        "WEEKDAY": 5,
        "WEEKLY": 7, 
        "WORKWEEKLY": 5, 
        "BIWEEKLY": 14,
        "MONTHLY": 30,
        "QUARTERLY": 91.313,
        "SEMIANNUALY": 182.625,
        "ANNUALLY": 365.25
    }

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
        self.frequency = frequency              # how often this task should 'reset'
        self.reset = Task.calcResetDateTime(self.frequency) # the time of the next 'reset' for this task
        self.target = timedelta(hours=1)        # how much time to spend on this task each reset period
        # internal fields...
        self.created = datetime.now()           # creation date of this task
        self.state = TaskState.READY
        self.duration_total = 0.0               # decimal minutes
        self.duration_period = 0.0              # decimal minutes
        self.duration_session = 0.0             # decimal minutes
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
        #       - finishes the task if the task's target for the reset period has been reached
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

    def saveToDatabase(self, conn, cursor):
        # before saving to the database, change the state to READY so that
        # it will be "ready" when it's read back in 
        self.state = TaskState.READY
        # convert the task into text strings and integers that can be
        # saved in the database
        fldValues = self.__dict__
        # call dbUpdate(conn, cursor, tableName, <key tuple>, <values dictionary>) to 
        # update or insert the record as appropriate
        dbUpdate(conn, cursor, 'tasks', key=('name', fldValues['name']), values=fldValues)
        pass

    def taskToDictionary(self):
        return self.__dict__

    def get_current_task():
        return Task.current_task
    
    def clear_current_task():
        if Task.current_task != None:
            Task.current_task.pause_task()
            Task.current_task = None

    def getTaskDetailsString(self):
        if self == Task.get_current_task():
            sessionMoniker = "this"
        else:
            sessionMoniker = "last"
        detailString = ''
        detailString += f'Priority: {self.priority},    Next Reset: {self.reset} ({self.frequency.name.lower()})'
        detailString += f'\nDuration (in decimal minutes): {round(self.duration_session, 1)} ({sessionMoniker} session), {round(self.duration_period, 1)} (this period), {round(self.duration_total, 1)} (total)'
        return detailString

    def updateTaskDurations(self):
        oldSessionDuration = self.duration_session
        session = datetime.now() - self.dtg_session_start
        self.duration_session = session.total_seconds() / 60.0
        delta = self.duration_session - oldSessionDuration

        if self.duration_total == None:
            self.duration_total = delta
            self.duration_period = delta
        else:
            self.duration_total = self.duration_total + delta
            self.duration_period = self.duration_period + delta
    
    def updateTaskState(self):
        # id duration_period >= to target duration, FINISHED for this period
        targetInMinutes = float(self.target.total_seconds() / 60)
        if self.duration_period >= targetInMinutes:
            self.state = TaskState.FINISHED
            return
        
        # if next reset - now less than (.25 * days in reset freq), then in DANGER
        daysLeft = self.reset - datetime.now()
        daysLeft = daysLeft.total_seconds() / 86400.0
        deltaDays = Task.day_counts[self.frequency.name] * .25
        if (daysLeft * 24) < (self.target.total_seconds()/3600.0):
            self.state = TaskState.OVERDUE
            return
        if daysLeft < deltaDays:
            self.state = TaskState.DANGER
            return


        # if we get here, we're okay, and state is just READY
        self.state=TaskState.READY
        return

    def start_task(self):
        self.state = TaskState.CURRENT
        self.duration_session = 0.0
        self.dtg_session_start = datetime.now()

    def pause_task(self):
        self.state = TaskState.PAUSED
        self.dtg_session_paused = datetime.now()
        self.updateTaskDurations()

        # session = self.dtg_session_paused - self.dtg_session_start
        # self.duration_session = session.total_seconds() / 60.0
        # if self.duration_total == None:
        #     self.duration_total = self.duration_session
        #     self.duration_period = self.duration_session
        # else:
        #     self.duration_total = self.duration_total + self.duration_session
        #     self.duration_period = self.duration_period + self.duration_session

        # To-Do: check for and handle when a task is finished for the current period
        task_is_finished = False
        if task_is_finished:
            self.finish_task()

        pass

    def finish_task(self):
        self.state = TaskState.FINISHED
        pass

    def calcResetDateTime(rFreq=ResetFrequency.DAILY, currentResetDateTime=datetime.now()):
        # ToDo: calculate timedelta for "WEEKDAY" and "WORKWEEKLY" ResetFrequency (?)

        # if the current reset date has passed, we calculate what the next one should be,
        # otherwise, we keep the current one
        if currentResetDateTime <= datetime.now():
            # the current reset date has passed...
            deltaDays = Task.day_counts[rFreq.name]
            nextDateTime = currentResetDateTime
            while nextDateTime.date() <= datetime.now().date():
                nextDateTime = datetime.combine(nextDateTime.date() + timedelta(days=deltaDays), datetime.min.time())
        else:
            # the current reset date is in the future...
            nextDateTime = currentResetDateTime
        return nextDateTime

    def clean_up_for_exit():
        Task.clear_current_task()  

    def newTaskFromDictionary(task_dictionary):
        # user configurable fields
        task = Task(task_dictionary["name"], task_dictionary["description"], eval(task_dictionary["priority"]))
        frequency = eval(task_dictionary["frequency"])
        task.frequency = frequency
        # if the reset date is 'None', then this is a newly added task, and we need to 
        # calculate the reset date from the frequency and the current date;
        # otherwise, just use the date from the database record.
        if task_dictionary["reset"] == None:
            task.reset = Task.calcResetDateTime(frequency)
            task.duration_period = 0.0
        else:
            currentReset = datetime.fromisoformat(datetime_str_to_ISO8601(task_dictionary["reset"]))
            task.reset = Task.calcResetDateTime(task.frequency, currentReset)
            if task.reset != currentReset:
                task.duration_period = 0.0
                task.duration_session = 0.0
            else:
                task.duration_period = eval(task_dictionary["duration_period"])
                task.duration_session = eval(task_dictionary["duration_session"])
        target = timedelta_from_str(task_dictionary["target"])
        task.target = target

        # internal persistent fields
        task.created = datetime.fromisoformat(datetime_str_to_ISO8601(task_dictionary["created"]))
        task.state = TaskState.READY
        task.duration_total = eval(task_dictionary["duration_total"])

        # internal temporary fields
        # task.duration_session = eval(task_dictionary["duration_session"])
        # task.duration_period = eval(task_dictionary["duration_period"])
        task.dtg_session_paused = task_dictionary["dtg_session_paused"]
        task.dtg_session_start = task_dictionary["dtg_session_start"]
        task.dtg_session_stop  = task_dictionary["dtg_session_stop"]

        # return the new task object
        return task

    def getTaskList(cursor):
        taskList = []
        info, columns, rows = dbGetTaskData(cursor)
        for row in rows:
            taskDict = {}   # NB: this must be declared here to make a NEW dictionary for EACH task
            for column in columns:
                taskDict[f"{column}"] = row[columns.index(column)]
            taskList.append(Task.newTaskFromDictionary(taskDict))
        
        return taskList

def datetime_str_to_ISO8601(s):
    # example: 2025-09-03 16:29:43.455888 becomes "2025-09-03T14:30:00"
    #         "2025-09-03T14:30:00"
    return (s[:19]).replace(" ", "T")

# def timedelta_str_to_ISO8601(s):
#     days = 0
#     hours = 0
#     minutes = 0
#     seconds = 0
#     # example: 1 day, 0:00:00 or 1:00:00
#     if "," in s:
#         # must have a 'day(s)' value, which is at the beginning
#         days = int((s[:(s.find(" "))]).strip())
#         hms = (s[s.find(",")+1:]).strip()
#     else:
#         hms = s.strip()

#     hc = hms.find(":")
#     hours = int(hms[:hc])

#     hms = hms[hc+1:]
#     mc = hms.find(":")
#     minutes = int(hms[:mc])

#     hms = hms[mc+1:]
#     seconds = int(hms)

#     return f"P{days}DT{hours}H{minutes}M{seconds}S"

# def timedelta_from_ISO8601(s):
#     pass

def timedelta_from_str(s):
    # if the string is None, return Python None
    if s == "None" or s == None:
        return None

    if "," in s:
        # Parse the string
        days, time = s.split(", ")
        hours, minutes, seconds = map(int, time.split(":"))
        days = int(days.split()[0])
    else:
        hours, minutes, seconds = map(int, s.split(":"))
        days = 0

    # create and return the timedelta object
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def testTaskList(count=10):
    taskList = []
    for tID in range(count):
        taskList.append(Task(f"Task {tID}", "New Task", tID))
    
    return taskList
