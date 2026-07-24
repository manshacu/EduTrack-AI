def heading():
    print("=" * 40)
    print("Student information")
    print("=" * 40)
def student_info(name,marks):
    print("Student Name: ", name)
    print("Marks: ",marks)
def result(marks):
    if(marks>=50):
        print("Status : Passed")
    else:
        print("Status: Failed")
    if(marks>=80):
        print("Grade : A")
    elif (marks>=70):
        print("Grade : B")
    elif (marks>=60):
        print("Grade : C")
    elif (marks>=50):
        print("Grade : D")
    else:
        print("Grade: E")
def remarks(marks):
    if(marks>=80):
        print("Excelent")
    elif (marks>=70):
        print("Very Good")
    elif (marks>=60):
        print("Good")
    elif (marks>=50):
        print("Satisfactory")
    else:
        print("Need improvement")
student_name=input("Enter Student name: ")
student_marks=int(input("Enter Student Marks: "))
heading()
student_info(student_name,student_marks)
result(student_marks)
remarks(student_marks)