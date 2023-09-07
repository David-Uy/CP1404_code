import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate}, {self.completion_percentage}"

    def is_completed(self):
        return int(self.completion_percentage) == 100

    def __lt__(self, other):
        return self.priority <= other.priortiy

    def compare_date(self, new_date):
        new_date = datetime.datetime.strptime(new_date, "%d/%m/%Y").date()
        return self.start_date >= new_date

    def update_percentage(self, new_percent):
        self.completion_percentage = new_percent

    def update_priority(self, value):
        self.priority = value

