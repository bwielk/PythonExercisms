class School(object):
    def __init__(self):
        self.list = []

    def add_student(self, name, grade):
        student = {'name': name, 'grade': grade}
        self.list.append(student)

    def roster(self):
        sorted_roster = sorted(self.list, key= lambda i:(i['grade'], i['name']))
        result = [student['name'] for student in sorted_roster]
        return result

    def grade(self, grade_number):
        grade_number_students = filter(lambda student: student['grade'] == grade_number, self.list)
        result = [student['name'] for student in grade_number_students]
        return sorted(result)
