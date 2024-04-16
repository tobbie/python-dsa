import pytest
from arrays_and_hashes.medium.longestsequence import LongestSequence

def test_placeholder():
    pass

def test_longest_sequence():
    #Arrange 
    sol = LongestSequence()

    #Act
    expected = sol.longestConsecutive([100, 4, 200, 1, 3, 2])
    #Assert
    assert  expected == 4

@pytest.mark.parametrize(
        "input_array, expected", [
            ([100, 4, 200, 1, 3, 2], 4),  
            ([0,3,7,2,5,8,4,6,0,1], 9)     
        ]
)
def test_longest_sequence_with_params(input_array, expected):
    #Arrange 
    sol = LongestSequence()
    #Act
    actual = sol.longestConsecutive(input_array)
    #Assert
    assert  expected == actual