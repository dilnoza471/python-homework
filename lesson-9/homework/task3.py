import json
import csv



def view_tasks(filepath="tasks.json"):
    data = get_data(filepath)
    for row in data:
        for key, value in row.items():
            print(f"{key}: {value}")
        print()

def get_data(filepath="tasks.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data
def update_tasks(data, filepath="tasks.json"):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
def stat_tasks(filepath="tasks.json"):
    data = get_data(filepath)
    total_tasks = len(data)
    completed_tasks = len([row for row in data if row['completed']])
    pending_tasks = total_tasks - completed_tasks
    average_priority = float(sum([row['priority'] for row in data]))/total_tasks
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority}")

def from_json_to_csv(filepath="tasks.csv"):
    data = get_data()
    with open(filepath, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
if __name__ == "__main__":
    view_tasks()
    stat_tasks()
    from_json_to_csv()