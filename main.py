from src.Proffesor import Proffesor
from src.Actions import *
from src.Student import Student

def main():
    ali = Proffesor("Ali", "Alizadeh", 123456)
    prof_lectures = ali.give_lecture()

    sam = Student("Sam", "Amini", 3, 456789)
    std_lectures = sam.pick_lecture(prof_lectures)
    std_dictionary_of_lectures = create_std_dictionary(std_lectures, f"{sam.name} {sam.family}")
    create_std_dictionary_file(std_dictionary_of_lectures)

    ali.give_grade(f"{sam.name} {sam.family}")
    average = sam.avg()
    print(f"Average of {sam.name} {sam.family} in this semister is: {average}")
    sam.status(average)

main()