import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitar data from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                if len(line) == 3:
                    name, year, cost = line
                    year = int(year)
                    cost = float(cost)
                    guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a CSV file."""
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for guitar in guitars:
                writer.writerow([guitar.name, guitar.year, guitar.cost])
        print(f"Saved {len(guitars)} guitars to '{filename}'.")
    except IOError:
        print(f"Error saving to '{filename}'.")


def main():
    """Guitar program, using Guitar class."""
    guitars = load_guitars("guitars.csv")

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    print("\n... snip ...\n")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort(key=lambda x: x.year)  # Sort by year (oldest to newest)
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name}, {guitar.year}, worth ${guitar.cost:,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")

    save_guitars("guitars.csv", guitars)


main()