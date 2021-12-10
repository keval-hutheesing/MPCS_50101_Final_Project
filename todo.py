import argparse
from datetime import datetime

class Task:
    
    def __init__(self, name, unique_id, due_date = None, priority = 1):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.completed = None
        self.created = datetime.now()
        self.unique_id = unique_id
        
  """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
    
class Tasks:
   """A list of `Task` objects."""
   
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # your code here

    def pickle_tasks(self):
        """Picle your task list to a file"""
        # your code here

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        pass

    def report(self):
        pass

    def done(self):
        pass

    def query(self):
        pass

    def add(self):
        pass

