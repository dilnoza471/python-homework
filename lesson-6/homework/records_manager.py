import os


def entry(employee_id, name, pos, salary):
    """
    Adds a new entry to the employees.txt file.

    Args:
        employee_id (str): Employee ID
        name (str): Employee Name
        pos (str): Employee Position
        salary (str): Employee Salary

    Returns:
        None
    """
    with open("employees.txt", "a") as file:
        file.write(f"{employee_id}, {name}, {pos}, {salary}\n")


def view():
    """
    Reads and returns all employee records from employees.txt.

    Returns:
        list: A list of employee records.
    """
    if not os.path.exists("employees.txt"):
        return []

    with open("employees.txt", "r") as file:
        return list(file.readlines())


def search(em_id):
    """
    Searches for an employee by their employee ID.

    Args:
        em_id (str): Employee ID to search for.

    Returns:
        str: Employee record if found, else "Employee not found".
    """
    employees = view()
    for employee in employees:
        if employee.split(', ')[0] == em_id:
            return employee.strip()
    return "Employee not found."


def update(employee_id, new_name=None, new_pos=None, new_salary=None):
    """
    Updates an employee's name, position, or salary.

    Args:
        employee_id (str): Employee ID to update.
        new_name (str, optional): New employee name (leave None to keep old).
        new_pos (str, optional): New employee position (leave None to keep old).
        new_salary (str, optional): New employee salary (leave None to keep old).

    Returns:
        bool: True if an update occurred, False otherwise.
    """
    lines = view()
    updated_lines = []
    updated = False

    for employee in lines:
        parts = employee.strip().split(', ')
        if parts[0] == employee_id:
            if new_name:
                parts[1] = new_name
            if new_pos:
                parts[2] = new_pos
            if new_salary:
                parts[3] = str(new_salary)
            updated = True
        updated_lines.append(', '.join(parts) + '\n')

    with open("employees.txt", "w") as file:
        file.writelines(updated_lines)

    return updated


def delete(employee_id):
    """
    Deletes an employee by ID.

    Args:
        employee_id (str): Employee ID to delete.

    Returns:
        bool: True if deleted, False otherwise.
    """
    lines = view()
    updated_lines = [line for line in lines if line.split(', ')[0] != employee_id]

    if len(lines) == len(updated_lines):  # No change means ID wasn't found
        return False

    with open("employees.txt", "w") as file:
        file.writelines(updated_lines)

    return True


def show_menu():
    """Displays the menu options."""
    print("""
    1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit
    """)


def get_input(update_mode=False):
    """
    Gets employee details from user input.

    Args:
        update_mode (bool): If True, allows skipping fields by pressing Enter.

    Returns:
        list: [ID, Name, Position, Salary] with empty values if skipped.
    """
    id_ = input("Enter employee ID: ")
    name = input("Enter employee name: ") if not update_mode else input(
        "Enter new name (leave blank to keep current): ")
    pos = input("Enter employee position: ") if not update_mode else input(
        "Enter new position (leave blank to keep current): ")
    salary = input("Enter employee salary: ") if not update_mode else input(
        "Enter new salary (leave blank to keep current): ")

    return [id_, name, pos, salary]


# Main menu loop
def main():
    while True:
        show_menu()
        try:
            menu = int(input("Enter menu number: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue  # Skip the rest of the loop iteration

        if menu == 1:
            line = get_input()
            entry(line[0], line[1], line[2], line[3])
            print("Successfully added new employee record.")

        elif menu == 2:
            lines = view()
            if lines:
                print("Employee Records:")
                for line in lines:
                    print(line.strip())
            else:
                print("No employee records found.")

        elif menu == 3:
            em_id = input("Enter employee ID: ")
            print(search(em_id))

        elif menu == 4:
            print("To update, enter the details. If you don't want to change something, leave it blank.")
            line = get_input(update_mode=True)
            if update(line[0], line[1] or None, line[2] or None, line[3] or None):
                print("Successfully updated employee record.")
            else:
                print("Failed to update employee record. Employee ID not found.")

        elif menu == 5:
            em_id = input("Enter employee ID: ")
            if delete(em_id):
                print("Successfully deleted employee record.")
            else:
                print("Failed to delete employee record. Employee ID not found.")

        elif menu == 6:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid menu number. Please choose a valid option.")


if __name__ == '__main__':
    main()
