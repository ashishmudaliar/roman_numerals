import pytest

from converter import converter

def test_invalid():
  assert converter.int_to_roman_converter("1") == "Please enter valid integers between 0 and 4000 only"

def test_converter_negative():
  assert converter.int_to_roman_converter(-10) == "Please insert integer between 0 and 4000"

def test_converter_zero():
  assert converter.int_to_roman_converter(0) == "Please insert integer between 0 and 4000"

def test_converter_4000_and_above():
  assert converter.int_to_roman_converter(4000) == "Please insert integer between 0 and 4000"
