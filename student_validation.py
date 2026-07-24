print("=" * 40)
print("Student Validation")
print("=" * 40)
student_name= input("Enter Student Name: ")
try:
    student_marks=int(input("Enter Stdent marks: "))
    print("Marks = ",student_marks)
    if(0<=student_marks<=100):
        print("Valid Marks")
        if(student_marks>=33):
            print("Passed")
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
            print("Fail")
    else:
            print("Please Enter Marks Between 0 to 100")
except:
    print("Please Enter Valid Marks")