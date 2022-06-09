def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False


Student_List = ['arash']
get_name = input("Enter a name: ")

if search(Student_List, get_name):
    print("Platform is found")
else:
    print("Platform does not found")