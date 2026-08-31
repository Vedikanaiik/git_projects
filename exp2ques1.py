#1Student Record Manager:Maintain a dictionary where keys are roll numbers and values are tuples (name, list_of_marks).
#Allow the user to: 1. Add a student record,
#2.Display all student names who have an average mark above 80,
#3.	Update marks for a specific roll number.
 
#Name: Vedika Pradeep Naik 
#prn: 26070122230 cse c-3

student = { }
print("1. Add Student Record")
print("2. Display names of students with average marks above 80")
print("3. Update details/marks of student")

rollno = int(input("Enter the roll number of student:"))
name = input ("Enter Student name: ")
marks = []

for i in range(5):
            mark = float(input("Enter mark: "))
            marks.append(mark)
student [rollno] = (name, marks)
print (student)

#2. All student names with average over 80
print("Stuents with average mark above 80")
for rollno in student:
            name = student[rollno][0]
            marks = student[rollno][1]

            total = 0

            for mark in marks:
                total = total + mark

            average = total / len(marks)

            if average > 80:
                print(name, "Average =", average)


