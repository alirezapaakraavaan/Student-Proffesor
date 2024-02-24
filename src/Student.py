from src.Person import Person
from src.Actions import show_prof_lectures
import json
from MyErrors.MyErrors import *

class Student(Person):
    def __init__(self, name, family, grade, std_id):
        super().__init__(name, family)
        self.grade = grade
        self.std_id = std_id

    def pick_lecture(self, all_lectures):
        show_prof_lectures(all_lectures)
        lectures = []

        not_defined = 0
        duplicated = 0
        try:
            for i in range(3):
                inp = input("Please enter lecture's name in the order that is presented: ")

                if inp not in all_lectures:
                    not_defined += 1
                    raise MyErrors()

                elif inp in lectures:
                    duplicated += 1
                    raise MyErrors()
                
                lectures.append(inp)

        except MyErrors as me:
            if not_defined != 0:
                print(me.lecture_not_defined())

            elif duplicated != 0:
                print(me.duplicated_lecture())
            
            lectures = []

        return lectures


    def avg(self):
        with open('Student_Grades.json', 'r') as f:
            existing_data = json.load(f)

        total_sum = 0

        for person_lectures in existing_data.values():
            for value in person_lectures.values():
                if isinstance(value, (int, float)):
                    total_sum += value
                    
        average = total_sum / 3

        return average


    def status(self, average):
        if average >= 10:
            print(f"{self.name} {self.family} Passed")
        else:
            print(f"{self.name} {self.family} Failed")