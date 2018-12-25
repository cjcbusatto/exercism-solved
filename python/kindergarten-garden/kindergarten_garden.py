class Student:
    default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
               'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class FlowerLookup:
    table = {
        'v': 'Violets',
        'r': 'Radishes',
        'c': 'Clover',
        'g': 'Grass'
    }


class GardenDecoder:
    def __init__(self, encoded_garden_diagram):
        self.encoded_garden_diagram = encoded_garden_diagram

    def decode(self):
        garden_map = self.encoded_garden_diagram.lower().replace("\n", " ").split()

        garden_rows = []
        garden_rows.append(list(garden_map[0]))
        garden_rows.append(list(garden_map[1]))

        return garden_rows


class Garden(object):
    def __init__(self, diagram, students=Student.default):
        garden_row_1, garden_row_2 = GardenDecoder(diagram).decode()
        self.student_plants = {}
        students.sort()

        for index, student in enumerate(students):
            try:
                self.student_plants[student] = [
                    garden_row_1[index * 2],
                    garden_row_1[index * 2 + 1],
                    garden_row_2[index * 2],
                    garden_row_2[index * 2 + 1]
                ]
            except IndexError:
                break

    def plants(self, student):
        return list(map(lambda plant: FlowerLookup.table.get(plant), self.student_plants.get(student)))
