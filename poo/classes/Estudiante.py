class Estudiante:

    def __init__(self, name, course, grades, average):
        self.name = name
        self.course = course
        self.grades = grades
        self.average = average
        self.calculate_average()

    def add_grade(self, grade):
        self.grades.append(grade)
        self.calculate_average()

        return self.grades

    def calculate_average(self):
        if self.grades:
            self.average = sum(self.grades) / len(self.grades)
        else:
            self.average = 0

        return self.average

    def isApproved(self):
        return self.average >= 5