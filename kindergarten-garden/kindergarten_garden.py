class Garden(object):

    students_list = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=students_list):
        self.plants_dict = {'R': 'Radishes',
                            'C': 'Clover',
                            'G': 'Grass',
                            'V': 'Violets'}

        self.students = sorted(students)

            #Given \n splits the diagram string in two rows of flower pots,
            #the code below splits the string in two arrays(rows) that can be
            #iterated over in the plants() method

        if len(diagram.split('\n')) == 2:
            self.diagram = diagram.split('\n')
        else:
            raise ValueError('The diagram can contain two rows only separated by "\\n"')

    def plants(self, name):
        results = []
        if name in self.students:
            index_of_student = self.students.index(name)

            #range_limit calculates the exclusive stop attribute of
            #the in range iterator.
            #range_limit is tightly linked with index_of_student variable
            #if student's index is 0, then we only need to add 2 to it to obtain the adequate stop attribute

            range_limit = index_of_student*2+2 if index_of_student != 0 else index_of_student + 2
            for row in self.diagram:
                for i in range(index_of_student*2, range_limit):
                    results.append(row[i])
        return self.decrypt_the_results(results)

    def decrypt_the_results(self, result):
        decrypted_result = []
        for el in result:
            decrypted_result.append(self.plants_dict[el])
        return decrypted_result