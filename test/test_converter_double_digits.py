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

def test_converter_forty():
  assert converter.int_to_roman_converter(40) == "XL"

def test_converter_forty_eight():
  assert converter.int_to_roman_converter(48) == "XLVIII"

def test_converter_fifty():
  assert converter.int_to_roman_converter(50) == "L"

def test_converter_fifty_nine():
  assert converter.int_to_roman_converter(59) == "LIX"

def test_converter_seventy():
  assert converter.int_to_roman_converter(70) == "LXX"

def test_converter_eighty_nine():
  assert converter.int_to_roman_converter(89) == "LXXXIX"
