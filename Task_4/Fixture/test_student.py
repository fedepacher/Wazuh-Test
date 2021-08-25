from student import StudentDB
import pytest

@pytest.fixture(scope='module')#seteando el scope en module este metodo se llama solo una vez al comienzo y luego se ejecutan los test, de lo contrario se llamaria en cada test consumiendo memoria al pedo
def db():
    print('----------------Setup method----------------')
    db = StudentDB()
    db.connect('students.json')
    #return db si en lugar de retornar coloco 
    yield db #va a devolver esta variable y cuadno se terminen los test continua despues del yield 
    print('----------------Teardown method---------------')
    db.close()

#si usamos el fixture a los metodos le tenems que ingerar el parametro db
def test_scott_data(db):    
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):    
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'  