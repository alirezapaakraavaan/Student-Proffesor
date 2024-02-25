import json
from src.Person import Person
from MyErrors.MyErrors import *

class Proffesor(Person):
    def __init__(self, name, family, prof_id):
        super().__init__(name, family)
        self.prof_id = prof_id


    def give_lecture(self):
        lectures = []

        duplicated = 0
        try:
            for i in range(3):
                inp = input("Please enter lecture's name: ")
                
                if inp in lectures:
                    duplicated += 1
                    raise MyErrors()
                
                lectures.append(inp)

        except MyErrors as me:
            if duplicated != 0:
                print(me.duplicated_lecture())

        return lectures
    

    def give_grade(self, student, message=""):

        with open('Student_Grades.json', 'r') as f:
            existing_data = json.load(f)

        new_values = {}

        try:
            for lecture in existing_data[student]:
                inp = input(f"Enter new point for {student}'s {lecture}: ")

                if (float(inp) < 0) or (float(inp) > 20):
                    raise MyErrors()
                
                new_value = float(inp)
                new_values[lecture] = new_value
            existing_data[student].update(new_values)
            message = "Done"

        except MyErrors as me:
            print(me.invalid_point())


        with open('Student_Grades.json', 'w') as f:
            json.dump(existing_data, f)

        return message