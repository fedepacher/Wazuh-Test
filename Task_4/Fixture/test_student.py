from student import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------------Setup method----------------')
    db = StudentDB()
    db.connect('students.json')
    yield db 
    print('----------------Teardown method---------------')
    db.close()

'''
Test for student called Scott
param db    student list
'''
def test_scott_data(db):    
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

'''
Test for student called Mark
param db    student list
'''
def test_mark_data(db):    
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'  