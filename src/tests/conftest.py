import pytest

from modules.load import Loader


@pytest.fixture(scope='session')
def maze1():
    loader: Loader = Loader()
    loader.download('tests/files/1.txt')
    yield loader.maze
