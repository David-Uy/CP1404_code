import datetime
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n" \
       "(F)ilter projects by date(A)dd new project\n(U)pdate project\n(Q)uit"


def main():
    print(MENU)


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                name, start_date_str, priority, estimate, completion = line.strip().split('\t')
                start_date = datetime.datetime.strptime(start_date_str, '%d/%m/%Y').date()
                priority = int(priority)
                estimate = float(estimate)
                completion = int(completion)
                projects.append(Project(name, start_date, priority, estimate, completion))
    except FileNotFoundError:
        pass  # File not found, start with an empty list
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")
