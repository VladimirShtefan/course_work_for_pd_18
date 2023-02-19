from pathlib import Path

CURRENT_PATH = Path(__file__).parent
PATH_WITH_FIXTURES = Path.joinpath(CURRENT_PATH, 'app', 'fixtures', 'data.json')
