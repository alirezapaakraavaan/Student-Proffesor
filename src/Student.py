from src.Person import Person
from src.Actions import show_prof_lectures
import json

class Student(Person):
    def __init__(self, name, family, grade, std_id):
        super().__init__(name, family)
        self.grade = grade
        self.std_id = std_id

    def pick_lecture(self, all_lectures):
        show_prof_lectures(all_lectures)
        lectures = []

        for i in range(3):
            lectures.append(input("Please enter lecture's name: "))

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