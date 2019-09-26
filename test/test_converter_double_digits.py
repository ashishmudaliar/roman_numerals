import pytest

from converter import converter

def test_converter_ten():
  assert converter.int_to_roman_converter(10) == "X"

def test_converter_fifteen():
  assert converter.int_to_roman_converter(15) == "XV"

def test_converter_twenty_one():
  assert converter.int_to_roman_converter(21) == "XXI"

def test_converter_thirty_five():
  assert converter.int_to_roman_converter(34) == "XXXIV"

def test_converter_thirty_nine():
  assert converter.int_to_roman_converter(39) == "XXXIX"
