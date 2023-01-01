import pytest
from main import BooksCollector

@pytest.fixture(scope="function")
def new_books_collector():
    '''Фикстура для создания нового объекта класса BooksCollector'''
    yield BooksCollector()