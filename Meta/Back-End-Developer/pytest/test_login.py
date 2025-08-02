from main import user_db, login
import pytest

@pytest.mark.parametrize("username,password,expected", [
    ("Alice", "password123", True),
    ("Bob", "password456", True),
    ("Charlie", "password789", True),
    ("unknown", "password123", False),
    ("", "", False),
])
def test_login(username, password, expected):
    assert login(username, password) == expected


# pytest -v

"""
================================================================================================= test session starts ==================================================================================================
platform win32 -- Python 3.10.9, pytest-7.1.2, pluggy-1.0.0 -- 
cachedir: .pytest_cache
plugins: anyio-3.5.0
collected 5 items                                                                                                                                                                                                       

test_login.py::test_login[Alice-password123-True] PASSED                                                                                                                                                          [ 20%] 
test_login.py::test_login[Bob-password456-True] PASSED                                                                                                                                                            [ 40%] 
test_login.py::test_login[Charlie-password789-True] PASSED                                                                                                                                                        [ 60%]
test_login.py::test_login[unknown-password123-False] PASSED                                                                                                                                                       [ 80%] 
test_login.py::test_login[--False] PASSED                                                                                                                                                                         [100%] 

================================================================================================== 5 passed in 0.02s ===================================================================================================                                                                                                                                                                       [100%] 
"""
"""
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed

"""


"""
Fixtures
Fixtures are a type of function that is applied to functions to be tested. 
These functions must run before that test is executed. 
The purpose of fixtures is to supply data from multiple sources including 
URLs and databases to the test before running the test. Fixtures are used in cases where code repeats initialization.

Format:

@pytest.fixture 

Markers
Markers are used to 'mark' specific functions to be executed by letting 
users create special names. There are many built-in markers such as xfail, xpass, skip and so on.

They follow a format such as:

@pytest.mark.<markername> 

For example:

@pytest.mark.alpha 

Running the specific marked test in the command line can be done with the following command:

pytest -m <markername> -v 

Which will be as follows for a marker called alpha.

pytest -m alpha -v 

"""