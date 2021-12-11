import argparse
from datetime import datetime
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
    
    def __str__(self):
        return "Name" + self.name  + "Created on: " + str(self.created)
    
class Tasks:
   
    headers_short = ["ID", "Age", "Due Date", "Priority", "Task"]

    def __init__(self, filename):
        """Read pickled tasks file into a list"""
        try:
            self.tasks = pickle.load(open(filename, "rb"))
            self.tasks_print_short = []
            for task in self.tasks:
                self.tasks_print_short.append(task.list_short)
        except:
            self.tasks = []

    def pickle_tasks(self, filename):
        """Picle your task list to a file"""
        pickle.dump(self.tasks,open(filename,"wb"))
        # your code here

    def update_short(self):
        self.tasks_print_short = []
        for task in self.tasks:
            self.tasks_print_short.append(task.list_short)


    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        self.tasks.sort(key = lambda x: x.created, reverse=True)
        self.update_short()
        print(tabulate(self.tasks_print_short, headers = self.headers_short))

    def report(self):
        pass

    def done(self):
        pass

    def query(self, query_list):
        self.query_print = []
        for query in query_list:
            for task in self.tasks:
                if task.name.find(query) > -1:
                    self.query_print.append(task.list_short)

    def add(self, name, unique_id, due_date = None, priority = 1):
        self.tasks.append(Task(name, unique_id, due_date, priority))
        pass




def main():
    a = Tasks(".todo.pickle")
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    if args.list:
        a.list()

    
    
    a.pickle_tasks(".todo.pickle")

if __name__ == "__main__":
    main()

