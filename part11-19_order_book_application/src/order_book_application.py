# Write your solution here

class Task: 
    id_counter = 1
    def __init__(self, description: str, programmer: str, workload: float):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.id = Task.id_counter
        self.done = False
        Task.id_counter += 1
    
    def is_finished(self):
        if self.done == True:
            return True
        return False
        
    def mark_finished(self):
        self.done = True
        
    def __iter__(self):
        self.task = 0
        return self
    
    def __next__(self):
        task = self.task
        self.task += 1
        return task
        
    
    def __str__(self):
        if self.is_finished() == True:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"
    
    
class OrderBook:
    def __init__(self):
        self.tasks = []
        
    def add_order(self, description, programmer, workload):
        task_to_add = Task(description, programmer, workload)
        self.tasks.append(task_to_add)
        
    def all_orders(self):
        return [task for task in self.tasks]
                    
    def programmers(self):
        names_only = [task.programmer for task in self.tasks]
        return list(set(names_only))
    
    def mark_finished(self, id: int):
        finished_task = None
        for task in self.tasks: 
            if task.id == id:
                finished_task = task
                task.mark_finished()
        if finished_task == None:
            raise ValueError
            
    def finished_orders(self):
        return [task for task in self.tasks if task.done == True]
    
    def unfinished_orders(self):
        return [task for task in self.tasks if task.done == False]
    
    def __str__(self):
        return [task for task in self.tasks]
        
    def status_of_programmer(self, programmer: str):
        tasks_per_programmer = []
        name_exists = False
        finished = 0
        unfinished = 0
        finished_hours = 0
        unfinished_hours = 0
        
        for task in self.tasks: 
            if task.programmer == programmer:
                tasks_per_programmer.append(task)
                name_exists = True
        for task in tasks_per_programmer: 
            if task.done == True:
                finished += 1
                finished_hours += int(task.workload)
            elif task.done == False: 
                unfinished += 1
                unfinished_hours += int(task.workload)
        if name_exists:
            return (finished, unfinished, finished_hours, unfinished_hours)
        return False
    
    
    
def application_for_tasks():
    tasks = OrderBook()
    while True:
        command = int(input("command: "))
    
        if command == 0:
            break
        if command == 1:
            add_task(tasks)
        if command == 2:
            get_finished(tasks)
        if command == 3:
            get_unfinished(tasks)   
        if command == 4: 
            mark_finished(tasks)
        if command == 5: 
            print_programmer(tasks)
        if command == 6: 
            programmer_status(tasks)
            
def commands():
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")
              
        
def add_task(tasks: OrderBook):
    description = input("description: ")
    programmer_and_workload = input("programmer and workload estimate: ")
    pw = programmer_and_workload.split()
    if len(pw) < 2:
        print("erroneous input")
        return
    programmer = pw[0]
    workload = pw[-1]
    for n in workload: 
        if n not in "1234567890":
            print("erroneous input")
            return
    OrderBook.add_order(tasks, description, programmer, workload)
    print("added!")

def get_finished(tasks: OrderBook):
    finished = OrderBook.finished_orders(tasks)
    if len(finished) < 1:
        print("no finished tasks")
    else: 
        for task in finished: 
            print(task)

def get_unfinished(tasks: OrderBook):
    unfinished = OrderBook.unfinished_orders(tasks)
    if len(unfinished) < 1:
        print("no unfinished tasks")
    else: 
        for task in unfinished: 
            print(task)
            
def mark_finished(tasks: OrderBook):
    try:
        id = int(input("id: "))
        OrderBook.mark_finished(tasks, id)
        print("marked as finished")
    except: 
        print("erroneous input")
        return
    OrderBook.mark_finished(tasks, id)
    print("marked as finished")
    
def print_programmer(tasks: OrderBook):
    names = OrderBook.programmers(tasks)
    for name in names:
        print(name)
        
def programmer_status(tasks: OrderBook):
    name = input("programmer: ")
    if OrderBook.status_of_programmer(tasks, name) == False:
        print("erroneous input")
        return
    stats = OrderBook.status_of_programmer(tasks, name)
    print(f"tasks: finished {stats[0]} not finished {stats[1]}, hours: done {stats[2]} scheduled {stats[3]}")
    
    
commands()    
application_for_tasks()