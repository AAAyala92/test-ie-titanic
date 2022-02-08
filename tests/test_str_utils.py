# Filename has to start with test

# def test_dummy():
# You can assert for whatever you want,
# *but* people usually avoid them in production code
# assert [1,2]==[1,2,3]
# assert True

from titanic_utils.str_utils import extract_titles
import hypothesis.strategies as st
from hypothesis import given


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


def test_extract_titles_without_dot_raises_error():
    with pytest.raises(ValueError):
        extract_titles("Alabama")


@given(st.text(alphabet=st.characters(blacklist_characters=["."])))
def test_extract_titles_with_gibberish_without_dots_raise_error(input_text):
    with pytest.raises(ValueError):
        extract_titles(input_text)
