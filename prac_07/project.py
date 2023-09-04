import datetime


class Project:
    def __init__(self, name="", start_date="", priority=int, cost_estimate=float, completion_percentage=float):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate:,.2f}, {self.completion_percentage}"

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.cost_estimate:,.2f}, {self.completion_percentage}"

    def is_completed(self):
        return int(self.completion_percentage) == 100

    def __lt__(self, other):
        return self.priority <= other.priortiy

    def compare_date(self, new_date):
        new_date = datetime.datetime.strptime(new_date, __format="%d/%m/%y").date()
        return self.start_date >= new_date

    def update_percentage(self, new_percent):
        self.completion_percentage = new_percent

    def update_priority(self, value):
        self.priority = value

