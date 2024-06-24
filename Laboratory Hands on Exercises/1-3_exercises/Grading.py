print("AWARD CALCULATOR")

written = float(input("Written Works Grade: "))
performance = float(input("Performance Tasks Grades: "))
quarterly = float(input("Quarterly Exam Grades: "))

x = written * .20
y = performance * .60
z = quarterly * .20

grade = x + y + z
final_grade = round(grade)

if 100 >= final_grade >= 98:
    print(f"Grade: {final_grade} Award: With Highest Honors")
elif 97 >= final_grade >= 94:
    print(f"Grade: {final_grade} Award: With High Honors")
elif 93 >= final_grade >= 90:
    print(f"Grade: {final_grade} Award: With Honors")
elif 89 >= final_grade >= 0:
    print(f"Grade: {final_grade} Award: No Award")
else: 
    print("Invalid")
