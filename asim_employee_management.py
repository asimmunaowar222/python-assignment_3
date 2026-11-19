# Format employee details
def get_employee_details(name, id, salary ):
    return f"{name} | {id} | {salary:.0f}"


# Save record to file
def save_to_file(record):
    with open("employees.txt", "a") as file:
        file.write(record + "\n")


# Take input and add employee
def add_employee():
    print()                               
    name = input("Enter Name: ")
    id = input("Enter ID: ")

    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid salary! Please enter a number.")
        return

    record = get_employee_details(name, id, salary)
    save_to_file(record)
    print("\nEmployee Added Successfully")   


# View all employee records
def view_the_file():
    try:
        with open("employees.txt", "r") as file:
            record = file.readlines()

            if not record:
                print("No employee records found.")

            else:
                for records in record:
                    print(records.strip())

    except FileNotFoundError:
        print("No records found. The file does not exist yet.")


# Main menu function
def main():
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        print()                            

        choice = input("Choose Option: ")

        # Add employee
        if choice == "1":
            add_employee()

        # View employees
        elif choice == "2":
            view_the_file()

        # Exit program
        elif choice == "3":
            print("Exit")
            break

        # Invalid input
        else:
            print("Invalid option! Please choose 1, 2, or 3.")

        print()                            
        

# Start program
main()