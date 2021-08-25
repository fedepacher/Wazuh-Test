Wazuh-Test
==========

This repository solves Wazuh QA Technical Test 

# Task 3

## Code execution 🚀

Under Task_3 folder run the next command:

python3 script.py

the expected result is:

![architecture](images/task3.png)



# Task 4

## Code execution 🚀

Under Task_4/Fixture/Module folder run the next command:

```
pytest -v test_student.py
```
the expected result is:

![architecture](images/test_fixture.png)

Under Task_4/Fixture/Class folder run the next command:

```
pytest -v --log-cli-level=0 classFixture.py
```
the expected result is:

![architecture](images/class.png)

Under Task_4/Parametrize folder run the next command:

```
pytest -v test_math_func_param.py 
```
the expected result is:

![architecture](images/test_parametrize.png)


## Author 👥

* **[Federico Pacher](https://github.com/fedepacher)**: Project creation and mantainance.

## License 📄

This project was created under MIT license ([MIT](https://choosealicense.com/licenses/mit/)).