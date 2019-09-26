import pytest

from converter import converter

def test_invalid():
  assert converter.int_to_roman_converter("1") == "Please enter valid integers greater than 0 only"

def test_converter_negative():
  assert converter.int_to_roman_converter(-10) == "Please insert integer greater than 0"

def test_converter_zero():
  assert converter.int_to_roman_converter(0) == "Please insert integer greater than 0"
