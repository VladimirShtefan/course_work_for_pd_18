from app.exceptions import FileNotFoundException
from app.models.database import Data
from settings import PATH_WITH_FIXTURES


def main():
    data = []
    database = Data(PATH_WITH_FIXTURES)
    try:
        data = database.get_data()
    except FileNotFoundException as e:
        print(e.message)
    if data:
        database.get_result(data)


if __name__ == '__main__':
    main()
