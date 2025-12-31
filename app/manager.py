from app.student import Student
from app.storage import load_students, save_students


class StudentManager:
    def __init__(self):
        self.students = load_students()

    def add_student(self, student_id, name, age, course):
        for s in self.students:
            if s["student_id"] == student_id:
                raise ValueError("Student ID already exists")

        student = Student(student_id, name, age, course)
        self.students.append(student.to_dict())
        save_students(self.students)

    def view_students(self):
        return self.students

    def delete_student(self, student_id):
        self.students = [
            s for s in self.students if s["student_id"] != student_id
        ]
        save_students(self.students)
