import datetime
from project import Project
from operator import itemgetter

FILENAME = "projects.txt"

MENU = "-(L)oad projects\n-(S)ave projects\n-(D)isplay projects\n" \
       "-(F)ilter projects by date\n-(A)dd new project\n-(U)pdate project\n-(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        projects = load_projects(FILENAME)
        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print("Projects loaded.")

        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved.")

        elif choice == 'D':

            incomplete_projects = check_incomplete_project(projects)
            complete_projects = check_complete_project(projects)
            print("Incomplete Projects:")
            display_projects(incomplete_projects)
            print()
            print("Complete Projects:")
            display_projects(complete_projects)

        elif choice == 'F':
            print()

        elif choice == 'A':
            print()

        elif choice == 'U':
            print()

        else:
            print("Invalid choice. Please select a valid option.")

        print(MENU)
        choice = input(">>>").upper()

    save_projects('projects.txt', projects)
    print("Thank you for using custom-built project management software.")


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
                completion = float(completion)
                projects.append(Project(name, start_date, priority, estimate, completion))

    except FileNotFoundError:
        print(f"File {filename} is not found")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    index = 0
    for project in projects:
        print({project})
        index += 1


def check_incomplete_project(projects):
    incomplete_projects = []
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)

    return incomplete_projects


def check_complete_project(projects):
    complete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
    return complete_projects


main()
