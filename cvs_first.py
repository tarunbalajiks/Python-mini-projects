                # ===== load_thecode =====#
import csv


def create_file():
    with open('Mark.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        n = int(input("Enter no of students"))
        for i in range(0, n):
            reg_no = int(input("Enter registration no of student"))
            name = input("Enter name")
            Rank = int(input("Enter Rank"))
            writer.writerow([reg_no, name, Rank])


def read_file():
    with open('Mark.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def copy_file():
    with open('Mark.csv', 'r') as old_file:
        with open('Mark1.csv', 'w') as new_file:
            reader = csv.reader(old_file)
            writer = csv.writer(new_file)
            for row in reader:
                if int(row[2]) > 500:
                    writer.writerow(row)


def search_file():
    name = input("Input Name to search")
    with open('Mark.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                print(row)


# maincode
create_file()

while True:
    query = (input("Enter option \n Read file(r) \n" 
                   "copy file(c) \n search(s) \n quit(q)"))
    if query.lower() == 'q':
        break
    elif query == 'r':
        read_file()
    elif query == 'c':
        copy_file()
    elif query == 's':
        search_file()
    else:
        print("Invalid option, please try again")
