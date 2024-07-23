class Employee:
    def __init__(self, id, name, department, manager_id=None):
        self.id = id
        self.name = name
        self.department = department
        self.manager_id = manager_id

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}
        self.reports = {}

    def add_employee(self, id, name, department, manager_id=None):
        if id in self.employees:
            print(f"Employee with ID {id} already exists.")
            return
        if manager_id and manager_id not in self.employees:
            print(f"Manager with ID {manager_id} does not exist.")
            return
        self.employees[id] = Employee(id, name, department, manager_id)
        if manager_id:
            if manager_id not in self.reports:
                self.reports[manager_id] = []
            self.reports[manager_id].append(id)
        print(f"Employee {name} added successfully.")

    def update_employee(self, id, name=None, department=None, manager_id=None):
        if id not in self.employees:
            print(f"Employee with ID {id} does not exist.")
            return
        employee = self.employees[id]
        if name:
            employee.name = name
        if department:
            employee.department = department
        if manager_id:
            if manager_id not in self.employees:
                print(f"Manager with ID {manager_id} does not exist.")
                return
            old_manager_id = employee.manager_id
            if old_manager_id:
                self.reports[old_manager_id].remove(id)
            employee.manager_id = manager_id
            if manager_id not in self.reports:
                self.reports[manager_id] = []
            self.reports[manager_id].append(id)
        print(f"Employee {id} updated successfully.")

    def delete_employee(self, id):
        if id not in self.employees:
            print(f"Employee with ID {id} does not exist.")
            return
        employee = self.employees.pop(id)
        if employee.manager_id:
            self.reports[employee.manager_id].remove(id)
        if id in self.reports:
            for report_id in self.reports.pop(id):
                self.employees[report_id].manager_id = None
        print(f"Employee {id} deleted successfully.")

    def search_employee(self, **criteria):
        results = []
        for emp in self.employees.values():
            match = True
            for key, value in criteria.items():
                if getattr(emp, key) != value:
                    match = False
                    break
            if match:
                results.append(emp)
        return results

    def display_hierarchy(self, id, level=0, visited=None):
        if visited is None:
            visited = set()
        if id in visited:
            print("Circular reference detected. Terminating display.")
            return
        visited.add(id)
        employee = self.employees.get(id)
        if not employee:
            print(f"Employee with ID {id} does not exist.")
            return
        print(" " * level * 4 + f"{employee.name} (ID: {id}, Dept: {employee.department})")
        for report_id in self.reports.get(id, []):
            self.display_hierarchy(report_id, level + 1, visited)

# Testing the system
ems = EmployeeManagementSystem()
ems.add_employee(1, "Alice", "Engineering")
ems.add_employee(2, "Bob", "Engineering", 1)
ems.add_employee(3, "Charlie", "HR", 1)
ems.add_employee(4, "David", "HR", 2)

# Update employee
ems.update_employee(4, name="David Jr.", department="Finance", manager_id=3)

# Delete employee
ems.delete_employee(3)

# Search employees
results = ems.search_employee(department="Engineering")
for emp in results:
    print(f"Found: {emp.name} (ID: {emp.id}, Dept: {emp.department})")

# Display hierarchy
ems.display_hierarchy(1)
