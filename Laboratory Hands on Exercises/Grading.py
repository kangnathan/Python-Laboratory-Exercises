print("Input Grades")

written = input("Written Works Grade: ")
performance = input("Performance Tasks Grades: ")
quarterly = input("Quarterly Exam Grades: ")

x = float(written) * .20
y = float(performance) * .60
z = float(quarterly) * .20

grade = str(x + y + z)

print("Your Final Grade Is: " + grade)





