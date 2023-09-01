import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"Name: {self.name}, Start Date: {self.start_date}, Priority: {self.priority}, " \
               f"Cost Estimate: {self.cost_estimate}, Completion Percentage: {self.completion_percentage}%"

    def is_completed(self):
        return self.completion_percentage == 100

    def days_until_completion(self):
        if self.is_completed():
            return 0
        today = datetime.date.today()
        return (self.start_date - today).days
