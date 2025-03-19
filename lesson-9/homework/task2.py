import csv


def gen_average_grades(filepath='grades.csv'):
    """Reads student grades from a CSV file and calculates the average for each subject."""

    # Open the file safely using 'with'
    with open(filepath, 'r', newline='') as file:
        data = csv.DictReader(file)

        average_grades = {}  # Stores total grades per subject
        count = {}  # Stores count of students per subject

        for row in data:
            subject = row["Subject"]
            grade = float(row["Grade"])

            # Initialize if not present, then update values
            average_grades[subject] = average_grades.get(subject, 0) + grade
            count[subject] = count.get(subject, 0) + 1

    # Compute final averages
    for subject in average_grades:
        average_grades[subject] /= count[subject]

    # Write results to a new CSV file
    with open('average_grades.csv', 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Average Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows([{"Subject": sub, "Average Grade": avg} for sub, avg in average_grades.items()])


if __name__ == '__main__':
    gen_average_grades()
