import json
import os
from pathlib import Path

from pydantic import ValidationError

from app.exceptions import FileNotFoundException
from app.models.operation import Operation


class Data:
    def __init__(self, path: Path | None = None):
        self._path = path

    def get_data(self) -> list[dict]:
        if os.path.exists(self._path):
            with open(self._path) as file:
                return json.load(file)
        raise FileNotFoundException()

    @staticmethod
    def _get_operation_list(operations: list[dict]) -> list[Operation]:
        operations_list: list[Operation] = []
        for iteration, operation in enumerate(operations, start=1):
            try:
                operations_list.append(Operation(**operation))
            except ValidationError:
                print(f'не валидные данные в операции №{iteration}: {operation}')
                continue
        return operations_list

    def _get_first_five_sorted_operations(self, operations: list[dict]) -> list[Operation]:
        operations = self._get_operation_list(operations)
        length = 6 if len(operations) > 6 else len(operations)
        return sorted(operations,
                      key=lambda operation_data: (operation_data.state, operation_data.date),
                      reverse=True)[:length]

    def get_result(self, data: list[dict]) -> bool:
        five_operations: list[Operation] = self._get_first_five_sorted_operations(data)
        for operation in five_operations:
            print(operation.get_info_for_operation())
        return True
