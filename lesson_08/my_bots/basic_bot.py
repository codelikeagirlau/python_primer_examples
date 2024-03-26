class Bot:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def perform_task(self):
        return f"{self.name} is {self.task}"

