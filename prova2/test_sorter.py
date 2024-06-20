import pytest
from sorter import Sorter

@pytest.fixture
def sorter():
    return Sorter()

@pytest.fixture
def file_for_test():
    with open('m_test.txt') as file:
        return [int(line.strip()) for line in file.readlines()]

@pytest.fixture
def huge_file_for_test():
    with open('m_test_huge.txt') as file:
        return [int(line.strip()) for line in file.readlines()]

def test_sort(sorter):
    sorter.lines = [11, 22, 4, 12]
    assert sorter.sort_array() == [4, 11, 12, 22]

def test_sort_lines(sorter, file_for_test):
    line_array = file_for_test
    assert sorter.sort_lines(line_array) == [11, 22, 33, 44]

def test_bufferize_huge(sorter, huge_file_for_test):
    large_array = list(range(1, 3001))
    sorter.bufferize(large_array)
    
    assert len(sorter.thousand_line_buffer) == 3

    assert len(sorter.thousand_line_buffer[0]) == 1000
    assert len(sorter.thousand_line_buffer[1]) == 1000
    assert len(sorter.thousand_line_buffer[2]) == 1000
    assert sorter.thousand_line_buffer[0][0] == 1
    assert sorter.thousand_line_buffer[1][0] == 1001
    assert sorter.thousand_line_buffer[2][0] == 2001

def test_bufferize_small(sorter, huge_file_for_test):
    # array smaller than 1000 (needed for max points)

    small_array = list(range(1, 50))
    sorter.bufferize(small_array)

    assert len(sorter.thousand_line_buffer) == 1

    assert len(sorter.thousand_line_buffer[0]) == 49