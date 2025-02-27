import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from _src.point import Point


@pytest.fixture(scope="function", autouse=True)
def bootstrap():
    print('setup------')
    yield Point(1,2)
    print('teardown-----')