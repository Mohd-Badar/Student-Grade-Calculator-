# Simple student grade calculator (Python)
# Created by Mohd Badar 

print("==== Student Grade Calculator ====")

name = input("Enter Student Name: ")

subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n==== Result ====")
print("Student Name :", name)
print("Total Marks  :", total, "/500")
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
