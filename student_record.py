import csv

filename = "student_record.csv"


def add():
    file = open(filename, "a", newline="")
    w = csv.writer(file)

    n = int(input("Enter number of entries: "))

    for i in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        w.writerow([roll, name, marks])

    file.close()
    print("Records added successfully!")


def dis():
    try:
        file = open(filename, "r")
        r = csv.reader(file)

        print("\n==============================================")
        print("              STUDENT RECORDS")
        print("==============================================")
        print(f"{'R.No':<10}{'Name':<25}{'Marks':>10}")
        print("----------------------------------------------")

        found = False

        for i in r:
            print(f"{i[0]:<10}{i[1]:<25}{float(i[2]):>10.2f}")
            found = True

        file.close()

        if not found:
            print("No records found.")

        print("==============================================")

    except FileNotFoundError:
        print("No records found.")


def search():
    roll = input("Enter Roll Number to search: ")

    try:
        file = open(filename, "r")
        r = csv.reader(file)

        found = False

        for i in r:
            if i[0] == roll:
                print("\nRecord Found!")
                print("Roll Number :", i[0])
                print("Name        :", i[1])
                print("Marks       :", i[2])
                found = True
                break

        file.close()

        if not found:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")


def update():
    roll = input("Enter Roll Number to update: ")

    try:
        file = open(filename, "r")
        r = csv.reader(file)
        rows = list(r)
        file.close()

        found = False

        for i in rows:
            if i[0] == roll:

                print("\n1. Update Name")
                print("2. Update Marks")

                choice = input("Enter your choice: ")

                if choice == "1":
                    i[1] = input("Enter New Name: ")

                elif choice == "2":
                    i[2] = float(input("Enter New Marks: "))

                else:
                    print("Invalid choice.")
                    return

                found = True
                break

        if found:
            file = open(filename, "w", newline="")
            w = csv.writer(file)
            w.writerows(rows)
            file.close()

            print("Record updated successfully!")

        else:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")


def delete():
    roll = input("Enter Roll Number to delete: ")

    try:
        file = open(filename, "r")
        r = csv.reader(file)
        rows = list(r)
        file.close()

        new_rows = []
        found = False

        for i in rows:
            if i[0] == roll:
                found = True
            else:
                new_rows.append(i)

        if found:
            file = open(filename, "w", newline="")
            w = csv.writer(file)
            w.writerows(new_rows)
            file.close()

            print("Record deleted successfully!")

        else:
            print("Record not found.")

    except FileNotFoundError:
        print("No records found.")


def statistics():
    try:
        file = open(filename, "r")
        r = csv.reader(file)

        marks = []
        names = []

        for i in r:
            marks.append(float(i[2]))
            names.append(i[1])

        file.close()

        if not marks:
            print("No records found.")
            return

        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)

        highest_index = marks.index(highest)
        lowest_index = marks.index(lowest)

        print("\n==============================================")
        print("               CLASS STATISTICS")
        print("==============================================")
        print("Total Students :", len(marks))
        print(f"Average Marks  : {average:.1f}")
        print("Highest Marks  :", highest)
        print("Highest Scorer :", names[highest_index])
        print("Lowest Marks   :", lowest)
        print("Lowest Scorer  :", names[lowest_index])
        print("==============================================")


    except FileNotFoundError:
        print("No records found.")


def menu():
    print("\n==============================================")
    print("           STUDENT RECORD SYSTEM")
    print("==============================================")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Statistics")
    print("7. Exit")
    print("==============================================")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        dis()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        statistics()

    elif choice == "7":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice, try again.")