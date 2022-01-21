# Filename has to start with test

# def test_dummy():
# You can assert for whatever you want,
# *but* people usually avoid them in production code
# assert [1,2]==[1,2,3]
# assert True

from titanic_utils.str_utils import extract_titles

import pytest

# @ = "Decorator"
@pytest.mark.parametrize(
    "expected_input, expected_output",
    [("Mr. John Doe", "Mr."), ("Miss. Jane Doe", "Miss."), ("Dr. Manhattan", "Dr.")],
)
def test_extract_titles_returns_expected_output(expected_input, expected_output):
    # 2.Run the code
    output = extract_titles(expected_input)

    # 3. Verify
    assert output == expected_output
