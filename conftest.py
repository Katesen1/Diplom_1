import pytest
from extra.burger import Burger

@pytest.fixture
def burger():
    burger = Burger()
    yield burger