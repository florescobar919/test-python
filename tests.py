import reminder as app

from reminder import Task

import datetime as dt
import pytest

from sys import version_info, platform


@pytest.fixture
def task_list():
    return [Task(name="pay rent"), Task(name="pay bills")]


# First Option Parametrize
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("pay bills", Task(name="pay bills")),
        ("pay home", None),
        ("PAY rent", Task(name="pay rent")),
    ],
)
def test_find_task(test_input, expected, task_list):
    task_list_w = task_list
    # assert app._find_task("pay bills", task_list) == Task(name="pay bills")
    assert app._find_task(test_input, task_list_w) == expected


def test_save_load_task_list(task_list):
    app._save_task_list(task_list)
    load_list = app._get_task_list()
    assert task_list == load_list


@pytest.mark.skip(reason="coming soon")
def test_new_feature(task_list):
    assert task_list == [Task(name="task one"), Task(name="task two")]


"""
def test_something():
    if not valid_platform():
        pytest.skip("unsupported")
"""


@pytest.mark.skipif(version_info < (4, 0), reason="requires >= python 4.0")
def test_funcion(task_list):
    assert task_list == [Task(name="pay rent"), Task(name="pay bills")]


@pytest.mark.xfail(reason="know issue")
def test_compare_length():
    assert 5 == 4


"""
def test_check_date():
    assert app._to_date("2022-09-01") == dt.date(2022, 9, 1)
"""

"""
def test_check_date_exception():
    with pytest.raises(ValueError, match="12345 is not in YYYY-MM-DD format."):
    #with pytest.raises(ValueError, match="Invalid isoformat string: '12345'"):
        app._to_date("12345")
"""

"""
#First Option Parametrize
@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("pay bills", Task(name="pay bills")),
        ("pay home", None),
        ("PAY rent", Task(name="pay rent")),
    ])
    

def test_find_task(test_input, expected):
    task_list = [Task(name="pay rent"), Task(name="pay bills")]
    # assert app._find_task("pay bills", task_list) == Task(name="pay bills")
    assert app._find_task(test_input, task_list) == expected
"""


"""
#First Option Unit
def test_find_task():
    task_list = [Task(name="pay rent"), Task(name="pay bills")]
    assert app._find_task("pay bills", task_list) == Task(name="pay bills")
    


def test_find_task_none():
    task_list = [Task(name="pay rent"), Task(name="pay bills")]
    assert app._find_task("pay home", task_list) is None
"""
