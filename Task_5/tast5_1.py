import json

class Task5:

    def __init__(self):
        self.__data = None
        
    '''
    Get file content
    param data_file     filename
    '''
    def connect(self, data_file):
        with open(data_file) as file:
            self.__data = file.readline()

    '''
    Return data from file
    return data
    '''
    def get_data(self):
        return self.__data


    def close(self):
        pass