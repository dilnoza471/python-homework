import csv
def gen_average_grades(filepath = 'grades.csv'):
    data = csv.DictReader(open(filepath))
    average_grades = {}
    count = {}
    for row in data:
        if row["Subject"] in average_grades:
            average_grades[row["Subject"]] += float(row["Grade"])
            count[row["Subject"]] += 1
        else:
            average_grades[row["Subject"]] = float(row["Grade"])
            count[row["Subject"]] = 1
    for key, value in average_grades.items():
        average_grades[key] = float(value) / count[key]
    fieldnames = ['Subject', 'Average Grade']
    content = []
    for key, value in average_grades.items():
        content.append({"Subject": key, "Average Grade": value})
    with open('average_grades.csv', 'wt', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)

if __name__ == '__main__':
    gen_average_grades()
