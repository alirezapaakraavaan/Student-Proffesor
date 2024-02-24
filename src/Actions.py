import os
import json

def show_prof_lectures(lectures):
    for lecture in lectures:
        print(f"{lecture}\n")

def create_std_dictionary(lectures, std_name):
    std_dictionary = {}
    std_dictionary[std_name] = {}

    for lecture in lectures:
        std_dictionary[std_name][lecture] = None

    return std_dictionary


def create_std_dictionary_file(std_dictionary_of_lectures):

    json_data = json.dumps(std_dictionary_of_lectures)


    if os.path.exists('Student_Grades.json'):
        with open('Student_Grades.json', 'a') as f:
            f.write(json_data)

    else:
        with open('Student_Grades.json', 'w') as f:
            f.write(json_data)