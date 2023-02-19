from pathlib import Path

import pytest

from app.exceptions import FileNotFoundException
from app.models.database import Data
from app.models.operation import Operation
from settings import PATH_WITH_FIXTURES


def test_data_exists():
    data = Data(PATH_WITH_FIXTURES).get_data()
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_data_not_exists():
    path = Path(__file__).joinpath('not_exists')
    with pytest.raises(FileNotFoundException):
        Data(path).get_data()


def test_get_operation_list(valid_data):
    operation_list = Data(PATH_WITH_FIXTURES)._get_operation_list(valid_data)
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[0], Operation)
    assert len(operation_list) == 2
    assert operation_list[1].id == valid_data[1]['id']


def test_get_first_five_sorted_operations(valid_data):
    operation_list = Data(PATH_WITH_FIXTURES)._get_first_five_sorted_operations(valid_data)
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[0], Operation)
    assert len(operation_list) == 2
    assert operation_list[1].id == valid_data[0]['id']


def test_get_result(valid_data):
    operation_successfully = Data(PATH_WITH_FIXTURES).get_result(valid_data)
    assert operation_successfully is True

