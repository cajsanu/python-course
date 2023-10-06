# Write your solution here:




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
        if finished_task == None:
            raise ValueError("id not found")
        finished_task.mark_finished()
        
    def finished_orders(self):
        return [task for task in self.tasks if task.done == True]
    
    def unfinished_orders(self):
        return [task for task in self.tasks if task.done == False]
        
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
        raise ValueError("programmer not found")
    
    
    
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# status = orders.status_of_programmer("Adele")
# print(status)
        
        
    