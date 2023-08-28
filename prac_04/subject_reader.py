FILENAME = "subject_data.txt"


def main():
    subject_data = get_data()
    display_subject_details(subject_data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []

    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number to an integer
        subject_data.append(parts)  # Append the parts to the subject_data list

    input_file.close()
    return subject_data


def display_subject_details(data):
    """Display subject details from the provided data."""
    for subject in data:
        subject_code, lecturer, num_students = subject
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()
