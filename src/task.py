from datetime import datetime

# Task Object
class Task:
    current_task = None

    def __init__(self, name, desc="Default Task Description", priority=3):
        self.name = name
        self.description = desc[:(len(desc) if len(desc) < 256 else 256)]
        self.priority = priority if (priority > 0 and priority < 6) else 3
        self.dtg_created = datetime.now()
        self.is_active = False
        self.is_paused = False
        self.finished = False       # or maybe 'self.done'?
        self.time_total = None
        self.time_session = None
        self.dtg_session_paused = None
        self.dtg_session_start = None
        self.dtg_session_stop = None

    def set_current_task(self):
        # if no task is "running" then clicking a button makes that task current, active and running
        # if a task is "running" then clicking the button for that task just pauses it
        # if a task is "running" then clicking another task's button switches to that new task and makes
        #     it active and running
        # 
        if Task.current_task != self and Task.current_task != None:
            temp = Task.get_current_task(self)
            temp.is_active = False
        Task.current_task = self
        self.is_active = True

    def get_current_task(self):
        return Task.current_task
    
    def no_current_task(self):
        if self.is_active:
            self.is_active = False
        Task.current_task = None
    

def testTaskList(count=10):
    taskList = []
    for tID in range(count):
        taskList.append(Task(f"Task {tID}", "New Task", tID))
    
    return taskList
