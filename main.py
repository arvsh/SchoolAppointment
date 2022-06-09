import os

# Add student
# Edit student
# Search among students
# Delete student
# Exit
Student_List = []


def add_student():
    os.system('cls')
    get_name = input(str("Enter your Name: "))
    Student_List.append(get_name)
    print(Student_List)


def edit_student():
    os.system('cls')
    get_name = input(str("Enter your Name: "))
    for i in range(len(Student_List)):
        if Student_List[i] == get_name:
            get_new_name = input(str("Enter new name: "))
            Student_List[i] = get_new_name


def search_student():
    os.system('cls')
    get_name = input("Enter your Name: ")
    for i in range(len(Student_List)):
        if Student_List[i] == get_name:
            print(Student_List[i] + " is found")


def delete_student():
    os.system('cls')
    get_name = input(str("Enter your Name: "))
    for i in range(len(Student_List)):
        if Student_List[i] == get_name:
            Student_List.remove(get_name)
            print("Student deleted successfully")


while True:
    print("""
    1) Add a student
    2) Edit a student
    3) Search a student
    4) Delete a student
    5) Exit""")

    choose = int(input("Choose an option: "))

    if choose == 1:  # add
        add_student()
    if choose == 2:  # edit
        edit_student()
    if choose == 3:  # search
        search_student()
    if choose == 4:  # delete
        delete_student()
    if choose == 5:
        break