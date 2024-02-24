import json
from src.Person import Person

class Proffesor(Person):
    def __init__(self, name, family, prof_id):
        super().__init__(name, family)
        self.prof_id = prof_id


    def give_lecture(self):
        lectures = []

        for i in range(3):
            lectures.append(input("Please enter lecture's name: "))

        return lectures
    

    def give_grade(self, student):

        with open('Student_Grades.json', 'r') as f:
            existing_data = json.load(f)

        new_values = {}

        for lecture in existing_data[student]:
            new_value = float(input(f"Enter new value for {lecture}: "))
            new_values[lecture] = new_value

        existing_data[student].update(new_values)

        with open('Student_Grades.json', 'w') as f:
            json.dump(existing_data, f)