import pytest

from converter import converter

def test_converter_one():
  assert converter.int_to_roman_converter(1) == "I"

def test_converter_two():
  assert converter.int_to_roman_converter(2) == "II"

def test_converter_three():
  assert converter.int_to_roman_converter(3) == "III"

def test_converter_four():
  assert converter.int_to_roman_converter(4) == "IV"

def test_converter_five():
  assert converter.int_to_roman_converter(5) == "V"

def test_converter_eight():
  assert converter.int_to_roman_converter(8) == "VIII"

def test_converter_nine():
  assert converter.int_to_roman_converter(9) == "IX"



