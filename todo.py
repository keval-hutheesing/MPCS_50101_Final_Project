import argparse
from datetime import date, datetime
import pickle
from tabulate import tabulate
import argparse

class Task:
    
    def __init__(self, name, unique_id, due_date = None, priority = 1):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = None
        self.created = datetime.now()
        self.unique_id = unique_id
        self.age = "0d"
        self.list_short = [self.unique_id, self.age, self.due_date, self.priority, self.name]
        self.list_long = [self.unique_id, self.age, self.due_date, self.priority, self.name, self.created.strftime("%a %b %d %H:%M:%S %Z %Y"), self.completed.strftime("%a %b %d %H:%M:%S %Z %Y")]


    def __str__(self):
        return "Name" + self.name  + "Created on: " + str(self.created)
    
class Tasks:
   
    headers_short = ["ID", "Age", "Due Date", "Priority", "Task"]
    headers_long = ["ID", "Age", "Due Date", "Priority", "Task", "Created", "Completed"]

    def __init__(self, filename):
        """Read pickled tasks file into a list"""
        self.unique_id_counter = 1
        try:
            self.tasks = pickle.load(open(filename, "rb"))
            self.tasks_print_short = []
            self.tasks_print_long = []
            for task in self.tasks:
                task_age = datetime.now() - task.created
                task.age = str(task_age.days) + "d"
                self.tasks_print_short.append(task.list_short)
                self.tasks_print_long.append(task.list_long)
                if task.unique_id >= self.unique_id_counter:
                    self.unique_id_counter = task.unique_id + 1
        except:
            self.tasks = []

    def pickle_tasks(self, filename):
        """Picle your task list to a file"""
        pickle.dump(self.tasks,open(filename,"wb"))
        # your code here

    def update_short(self):
        self.tasks_print_short = []
        for task in self.tasks:
            if task.completed == None:
                self.tasks_print_short.append(task.list_short)
    
    def update_long(self):
        self.tasks_print_short = []
        for task in self.tasks:
            self.tasks_print_short.append(task.list_long)


    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        self.tasks.sort(key = lambda x: x.created, reverse=True)
        self.update_short()
        print(tabulate(self.tasks_print_short, headers = self.headers_short))

    def report(self):
        self.tasks.sort(key = lambda x: x.created, reverse=True)
        self.update_long()
        print(tabulate(self.tasks_print_long, headers = self.headers_long))

    def done(self, unique_id):
        for task in self.tasks:
            if task.unique_id == int(unique_id):
                task.completed = "done"
                print("Completed task", unique_id)

    def query(self, query_list):
        self.query_print = []
        for query in query_list:
            for task in self.tasks:
                if task.name.find(query) > -1:
                    self.query_print.append(task.list_short)

    def add(self, name, due_date = None, priority = 1):
        self.tasks.append(Task(name, self.unique_id_counter, due_date, priority))
        print("Created task", self.unique_id_counter)
        self.unique_id_counter = self.unique_id_counter + 1

    def delete(self, unique_id):
        for i in range(0, len(self.tasks)):
            if self.tasks[i].unique_id == int(unique_id):
                self.tasks.remove(self.tasks[i])
                print("Deleted task", unique_id)
                break

                




def main():
    a = Tasks(".todo.pickle")
    parser = argparse.ArgumentParser()

    parser.add_argument("--list", action="store_true")

    parser.add_argument("--report", action="store_true")

    parser.add_argument("--add")
    parser.add_argument("--due")
    parser.add_argument("--priority")

    parser.add_argument("--delete")

    parser.add_argument("--done")

    parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")



    args = parser.parse_args()


    if args.query:
        a.query(args.query)
       
    if args.add:
        due_date = None
        priority = 1
        if args.due:
            due_date = args.due

        if args.priority:
            priority = args.priority
        
        a.add(args.add, due_date, priority)
    
    if args.list:
        a.list()

    if args.delete:
        a.delete(args.delete)
    
    if args.done:
        a.done(args.done)

    if args.report:
        a.report()

    a.pickle_tasks(".todo.pickle")

if __name__ == "__main__":
    main()

