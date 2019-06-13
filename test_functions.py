"""tests for my functions"""

import functions
    
def test_increase_counter():
    """tests for function increase_counter"""
    
    test_list = ["a", "d", "d", "b", "c", "a", "a", "a"]
    
    assert isinstance(increase_counter(test_list), list)
    
    assert increase_counter(test_list) == [4, 1, 1, 2]


def test_find_max():
    """tests for function find_max"""
    
    another_test_list = [41, 26, 66, 5, 40]
    
    assert find_max(another_test_list) == 66

