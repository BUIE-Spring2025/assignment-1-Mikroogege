import pytest
from main.py import int_to_roman

# do not change this file

def test_int_to_roman_3999():
    assert int_to_roman(3999) == "MMMCMXCIX"