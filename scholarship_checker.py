print("=" * 40)
print("Student Scholarship checking")
print("=" * 40)
student_name= input("Enter Student Name: ")
student_marks=int(input("Enter Stdent marks: "))
student_attendance=int(input("Enter Student Attendendance"))
student_sports_certificate=input("Have you Sports Certificate? yes/no:  ")
print("=" * 40)
print("Student Scholarship Status")
print("=" * 40)
print("Name:              ",student_name)
print("Marks:             ",student_marks)
print("Attendance:        ", student_attendance)
print("Sports Certificate:", student_sports_certificate)
if(student_marks>=50):
    print("Status : Pass")
else:
    print("Fail")
if(student_marks>=80 and student_attendance>=90):
    print("Scholarship Status: Approved")
else:
    print("Not Eligible")
if(student_marks>=80 or student_sports_certificate.lower() == "yes"):
    print ("Special Award Eligible")
else:
    print ("Not Eligible Special Award")
