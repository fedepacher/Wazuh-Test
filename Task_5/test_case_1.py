import pytest
from tast5 import Task5
import logging

@pytest.mark.parametrize('filename, content',
                        [
                            ('1.txt', 'a\n'),
                            ('2.txt', 'b\n'),
                            ('3.txt', 'c\n'),
                            ('4.txt', 'd\n'),
                            ('5.txt', 'e\n')
                        ]
                        )
def test_data(filename, content): 
    db = Task5()
    logging.info(f'Testing file {filename}')
    db.connect(filename)   
    data = db.get_data()
    assert data == content
    
