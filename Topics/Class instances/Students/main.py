class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

        # calculate the student_id here
        self.student_id = self.name[0] + self.last_name + self.birth_year


new_student = Student(input(), input(), input())

print(new_student.student_id)
