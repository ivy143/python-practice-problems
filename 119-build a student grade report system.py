# Build a student grade report system
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def generate_report(self):
        report = f"Grade Report for {self.name}:\n"
        for subject, grade in self.grades.items():
            report += f"{subject}: {grade}\n"
        report += f"Average Grade: {self.get_average():.2f}\n"
        return report
# Example usage
student = Student("Alice")
student.add_grade("Math", 85)
student.add_grade("Science", 90)
student.add_grade("History", 78)
print(student.generate_report())
student2 = Student("Bob")
student2.add_grade("Math", 92)
student2.add_grade("Science", 88)
student2.add_grade("History", 81)
print(student2.generate_report())
