import datetime
from project import Project

FILENAME = "projects.txt"

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
       "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n-(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    projects = load_projects(FILENAME)
    while choice != "Q":
        if choice == 'L':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)

        elif choice == 'S':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved.")

        elif choice == 'D':
            incomplete_projects, complete_projects = check_complete_project(projects)

            print("Incomplete Projects:")
            display_projects(incomplete_projects)
            print()
            print("Complete Projects:")
            display_projects(complete_projects)

        elif choice == 'F':
            date = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_data_by_date(date, projects)
            sorted_projects = sort_by_date(filtered_projects)
            display_projects(sorted_projects)

        elif choice == 'A':
            print("Let's add a new project")
            name = get_valid_string("Name: ")
            start_date = get_valid_string("Start date (dd/mm/yy): ")
            priority = int(get_valid_string("Priority: "))  # Ensure priority is an integer
            cost_estimate = float(get_valid_string("Cost estimate: $"))
            percent_complete = float(get_valid_string("Percent complete: "))  # Assuming percent complete is a float
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)

        elif choice == 'U':
            projects_number = {}

            for number, project in enumerate(projects):
                projects_number[str(number)] = project
                print(f"{number}. {project}")
            try:
                choice = input("Project choice: ")
                chosen_project = projects_number[choice]
                print(chosen_project)
                new_percentage = get_valid_string("New Percentage: ")
                new_priority = get_valid_string("New Priority: ")
                update_completion_percentage(chosen_project, int(new_percentage))
                update_priority(chosen_project, int(new_priority))

            except KeyError:
                print("Invalid Choice")

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
                try:
                    name, start_date_str, priority, estimate, completion = line.strip().split('\t')
                    start_date = datetime.datetime.strptime(start_date_str, '%d/%m/%Y').date()
                    priority = int(priority)
                    estimate = float(estimate)
                    completion = float(completion)
                    project = Project(name, start_date, priority, estimate, completion)
                    projects.append(project)
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()}. {e}")

    except FileNotFoundError:
        print(f"File {filename} is not found")

    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")


def display_projects(projects):
    for project in projects:
        print(f" {project}")


def check_complete_project(projects):
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        project.completion_percentage = int(project.completion_percentage)
        if project.completion_percentage < 100:
            project.completion_percentage = str(project.completion_percentage)
            incomplete_projects.append(project)
        if project.completion_percentage == 100:
            project.completion_percentage = str(project.completion_percentage)
            complete_projects.append(project)
    incomplete_projects.sort(key=lambda project: project.priority)
    complete_projects.sort(key=lambda project: project.priority)
    return incomplete_projects, complete_projects


def filter_data_by_date(date, projects):
    filtered_datas = []
    for project in projects:
        if project.compare_date(date):
            filtered_datas.append(project)
    return filtered_datas


def sort_by_date(projects):
    date_list = []
    for project in projects:
        if project.start_date not in date_list:
            date_list.append(project.start_date)
    date_list.sort()
    sorted_project = []
    for date in date_list:
        for project in projects:
            if project.start_date == date:
                sorted_project.append(project)
    return sorted_project


def get_valid_string(prompt):
    string = input(prompt)
    while string == "":
        print("Input can not be blank")
        string = input(prompt)
    return string


def update_completion_percentage(self, new_percentage):
    new_percentage = float(new_percentage)
    if 0 <= new_percentage <= 100:
        self.completion_percentage = new_percentage
    else:
        print("Invalid percentage. Please enter a value between 0 and 100.")


def update_priority(self, new_priority):
    try:
        new_priority = int(new_priority)
        self.priority = new_priority
    except ValueError:
        print("Invalid input. Please enter an integer value for the priority.")


main()
