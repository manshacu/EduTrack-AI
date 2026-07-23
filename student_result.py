print("=" * 40)
print("Student Result Entry")
print("=" * 40)
student_name= input("Enter Student Name: ")
student_marks=int(input("Enter Stdent marks: "))
print("=" * 40)
print("Student Result")
print("=" * 40)
print("Name: ",student_name)
print("Marks: ",student_marks)
if(student_marks >= 50):
    print("Status : Pass")
    print("Congratulations!")
else:
    print("Status: Fail")
    print("Better luck Next time")
if(student_marks>=80):
    print("Grade : A")
    print("Excelent")
elif (student_marks>=70):
    print("Grade : B")
    print("Very Good")
elif (student_marks>=60):
    print("Grade : C")
    print("Good")
elif (student_marks>=50):
    print("Grade : D")
    print("Satisfactory")
else:
    print("Grade: E")
    print("Need improvement")

print("=" * 40)