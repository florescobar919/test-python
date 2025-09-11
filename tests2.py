import reminder as app

from reminder import Task

import pytest


def test_find_task():
    task_list = [Task(name="pay rent"), Task(name="pay bills")]
    assert app._find_task("pay bills", task_list) == Task(name="pay bills")


def test_find_task_none():
    task_list = [Task(name="pay rent"), Task(name="pay bills")]
    assert app._find_task("pay home", task_list) is None
