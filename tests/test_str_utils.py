# Filename has to start with test

#def test_dummy():
    # You can assert for whatever you want,
    # *but* people usually avoid them in production code
    # assert [1,2]==[1,2,3]
    #assert True

from titanic_utils.str_utils import extract_titles

import pytest

def test_extract_titles_returns_expected_output():
    #1.Preconditions
    expected_input = "Mr. John Doe"  #what I am using as input
    expected_output = "Mr."           #what I expect ro recieve

    #2.Run the code
    output = extract_titles(expected_input)

    #3. Verify
    assert output == expected_output
