from task5_2 import Task5_2
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------------Setup method----------------')
    database = "clients.db"    
    db = Task5_2(database)
    yield db 
    print('----------------Teardown method---------------')
    db.closeConn()

'''
Test to check database structure
'''
def test_columns(db): 
    table = 'CLIENTS'
    value_expected = ['id', 'name', 'country', 'age']  
    assert value_expected == db.columnExist(table)
    
'''
Test to check age values
'''
def test_ages(db): 
    table = 'CLIENTS'
    column = 'age'
    for i in range(db.countObjects(table)):
        assert db.getObjectByColumn(table, column)[i] > 5
                

'''
Test to check if there is a null value
'''
def test_null_values(db):
    table = 'CLIENTS'   
    columnList = db.columnExist(table)
    numComp = db.countObjects(table)
    for column in columnList:
        for i in range(numComp):
            assert db.getObjectByColumn(table, column)[i] != 'null'


'''
Test to check age values are int type
'''
def test_ages_type(db): 
    table = 'CLIENTS'
    column = 'age'
    for i in range(db.countObjects(table)):
        assert type(db.getObjectByColumn(table, column)[i]) == int