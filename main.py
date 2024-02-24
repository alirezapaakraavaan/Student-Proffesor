from src.Proffesor import Proffesor
from src.Actions import *
from src.Student import Student

def main():
    farzad = Proffesor("Farzad", "Alizadeh", 123456)
    prof_lectures = []

    while len(prof_lectures) < 3:
        prof_lectures = farzad.give_lecture()

    alireza = Student("Alireza", "Pakravan", 3, 456789)
    std_lectures = alireza.pick_lecture(prof_lectures)

    while std_lectures == []:
        std_lectures = alireza.pick_lecture(prof_lectures)

    
    std_dictionary_of_lectures = create_std_dictionary(std_lectures, f"{alireza.name} {alireza.family}")
    create_std_dictionary_file(std_dictionary_of_lectures)

    result = farzad.give_grade(f"{alireza.name} {alireza.family}")

    while result != "Done":
        result = farzad.give_grade(f"{alireza.name} {alireza.family}")
        

    average = alireza.avg()
    print(f"Average of {alireza.name} {alireza.family} in this semister is: {average}")
    alireza.status(average)

main()