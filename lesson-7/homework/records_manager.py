import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        """Initialize an employee with ID, name, position, and salary."""
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        """String representation for debugging."""
        return f"{self.employee_id} {self.name} {self.position} {self.salary}"

    def __str__(self):
        """String representation for printing."""
        return f"{self.employee_id} {self.name} {self.position} {self.salary}"


class EmployeeManager:
    def __init__(self):
        """Load employees from file if it exists."""
        self.employees = []
        self.load_employees()

    def load_employees(self):
        """Loads employees from the file into memory."""
        if os.path.exists("employees.txt"):
            with open("employees.txt", "r") as f:
                for line in f:
                    details = line.strip().split()
                    if len(details) == 4:
                        self.employees.append(Employee(details[0], details[1], details[2], details[3]))

    def update(self):
        """Writes the employee list to the file (overwrites old data)."""
        with open("employees.txt", "w") as f:
            f.write("\n".join(str(emp) for emp in self.employees) + "\n")

    def add_employee(self, employee_id, name, position, salary):
        """Adds a new employee and updates the file."""
        self.employees.append(Employee(employee_id, name, position, salary))
        self.update()
        print("Successfully added new employee record.")

    def view(self):
        """Returns a formatted string of all employees."""
        return "\n".join(str(emp) for emp in self.employees) if self.employees else "No employee records found."

    def search(self, employee_id):
        """Finds an employee by ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return "Employee not found."

    def update_employee_info(self, employee_id, name=None, position=None, salary=None):
        """Updates employee details and writes changes to file."""
        employee = self.search(employee_id)
        if isinstance(employee, Employee):
            if name:
                employee.name = name
            if position:
                employee.position = position
            if salary:
                employee.salary = salary
            self.update()
            print("Updated successfully.")
        else:
            print("Employee not found.")

    def delete_employee(self, employee_id):
        """Removes an employee and updates the file."""
        employee = self.search(employee_id)
        if isinstance(employee, Employee):
            self.employees.remove(employee)
            self.update()
            print("Deleted employee successfully.")
        else:
            print("Employee not found.")


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
    """Gets employee details from user input, allows skipping fields in update mode."""
    id_ = input("Enter employee ID: ")
    name = input("Enter employee name: ") if not update_mode else input("Enter new name (leave blank to keep current): ")
    pos = input("Enter employee position: ") if not update_mode else input("Enter new position (leave blank to keep current): ")
    salary = input("Enter employee salary: ") if not update_mode else input("Enter new salary (leave blank to keep current): ")
    return [id_, name, pos, salary]


def main():
    manager = EmployeeManager()  # Create an instance of EmployeeManager
    while True:
        show_menu()
        try:
            menu = int(input("Enter menu number: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue  # Skip invalid input and restart loop

        if menu == 1:
            line = get_input()
            manager.add_employee(line[0], line[1], line[2], line[3])

        elif menu == 2:
            print("Employee Records:")
            print(manager.view())

        elif menu == 3:
            em_id = input("Enter employee ID: ")
            print(manager.search(em_id))

        elif menu == 4:
            print("To update, enter the details. If you don't want to change something, leave it blank.")
            line = get_input(update_mode=True)
            manager.update_employee_info(line[0], line[1] or None, line[2] or None, line[3] or None)

        elif menu == 5:
            em_id = input("Enter employee ID: ")
            manager.delete_employee(em_id)

        elif menu == 6:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid menu number. Please choose a valid option.")


if __name__ == '__main__':
    main()
