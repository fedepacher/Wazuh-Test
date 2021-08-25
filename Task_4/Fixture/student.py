import json

class StudentDB:

    def __init__(self):
        self.__data = None

    '''
    Get student list from json file
    param data_file     filemane with student info
    '''
    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    '''
    Get student in case existe in the list
    param name      student name
    '''
    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                return student


    def close(self):
        pass
