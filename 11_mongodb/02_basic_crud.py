from pymongo import MongoClient
from pprint import pprint

client=MongoClient("mongodb://admin:admin123@localhost:27017/")

db=client.school
# this is a db 
students=db.students
# this is a collection inside school db

def create_student():
    name=input("enter student name: ")
    age=int(input("enter student age: "))
    skills =input("enter student skills (comma seperated): ").split(",")

    # students.insert_one({
    #     "name":name,
    #     "age":age,
    #     "skills":[skill.strip() for skill in skills ]
    # })
    docs={
        "name":name,
        "age":age,
        "skills":[skill.strip() for skill in skills ]
    }
    students.insert_one(docs)
    print(f"✅ Student {name} added successfully! ")


def read_students():
    for student in students.find():
        print("+"*75)
        age=student["age"]
        name=student["name"]
        skills=student["skills"]
        print(f"name : {name}\nage : {age}")
        print("skills are as followed ")
        for i in skills:
            print(i)
        # pprint(student)
    print("+"*75)
        
def search_student():
    # name=input("enter the student name that you wanted to update : ")
    name=input("enter student name to search: ")

    # for student in students.find({"name":name}):
    #     print(student)  
    result=students.find_one({
        "name":name
    })

    if result is not None:
        print(result)
    else:
        print("no student of such name exists ")
     
def update_student():
    name=input("enter student name to search: ")
    age=int(input("enter the updated age of "))
    result=students.update_one(
        {"name":name},
        {"$set":{"age":age}}
    )
    if result.modified_count:
        print("updated succesfully ")
    else:
        print("no matching student find ")



def delete_student():
    name=input("name of the student to be deleted ")
    result=students.delete_one({
        "name":name
    })
    if result.deleted_count:
        print("deleted succesfully ")
    else:
        print("no matching student found to be deleted " )




def main():
    while True:
        print("""
========= STUDENT CRUD APP =========
1️⃣  Create Student
2️⃣  View All Students
3️⃣  Search Student
4️⃣  Update Student Age
5️⃣  Delete Student
6️⃣  Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice — try again\n")

if __name__=="__main__":
    print("mongodb connected sucessfully ")
    main()