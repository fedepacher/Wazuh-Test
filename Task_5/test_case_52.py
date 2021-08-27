from task5_2 import Task5_2
import pytest
import logging


@pytest.fixture(scope='class')
def db(request):
    logging.info('----------------Setup method----------------')
    database = "clients.db"    
    connection = Task5_2(database)
    request.cls.db = connection 
    request.cls.table = 'CLIENTS'
    yield
    logging.info('----------------Teardown method-------------')
    connection.closeConn()

@pytest.mark.usefixtures("db")
class TestTask52:
    '''
    Test to check database structure
    '''
    def test_columns(self):     
        value_expected = ['id', 'name', 'country', 'age']  
        logging.info(f'Testing database structure {value_expected}')
        assert value_expected == self.db.columnExist(self.table)
        
    '''
    Test to check age values
    '''
    def test_ages(self):     
        column = 'age'
        logging.info(f'Testing {column} values')
        for i in range(self.db.countObjects(self.table)):
            assert self.db.getObjectByColumn(self.table, column)[i] > 5
                    

    '''
    Test to check if there is a null value
    '''
    def test_null_values(self):
        columnList = self.db.columnExist(self.table)
        numComp = self.db.countObjects(self.table)
        for column in columnList:
            logging.info(f'Testing column {column}')
            for i in range(numComp):
                assert self.db.getObjectByColumn(self.table, column)[i] != 'null'


    '''
    Test to check age values are int type
    '''
    def test_ages_type(self):
        column = 'age'
        logging.info(f'Testing {column} column type')
        for i in range(self.db.countObjects(self.table)):
            assert type(self.db.getObjectByColumn(self.table, column)[i]) == int