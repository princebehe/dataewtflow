# Accept a list of student names from the user
student_names = []
print("Enter student names (type 'done' to finish):")
while True:
    name = input("Student name: ").strip()
    if name.lower() == 'done':
        break
    if name:
        student_names.append(name)

# Save them to a text file
filename = "students.txt"
with open(filename, "w") as file:
    for name in student_names:
        file.write(name + "\n")

print(f"\nNames successfully saved to {filename}.")

# Read and display them from the file
print("\n--- Reading from File ---")
with open(filename, "r") as file:
    content = file.read()
    print(content)