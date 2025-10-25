def save_to_file(students):
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f"Name: {s['name']}, ID: {s['student_id']}, Favorite AI Tool: {s['favorite_AI_tool']}\n")

students = []

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    student_id = input("Enter student ID: ")
    favorite_AI_tool = input("Enter favorite AI tool: ")

    student = {"name": name, "student_id": student_id, "favorite_AI_tool": favorite_AI_tool}
    students.append(student)

save_to_file(students)
print(f"\nTotal students: {len(students)}")
for s in students:
    print(s)
