import pytest

from converter import converter

def test_converter_hundred():
  assert converter.int_to_roman_converter(100) == "C"

def test_converter_two_hundred():
  assert converter.int_to_roman_converter(200) == "CC"

def test_converter_three_hundred_ninety_nine():
  assert converter.int_to_roman_converter(399) == "CCCXCIX"

