# Accept marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)
print(f"Average Mark: {average:.2f}")

# Determine the grade
if 80 <= average <= 100:
    grade = "A"
elif 60 <= average < 80:
    grade = "B"
elif 40 <= average < 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")