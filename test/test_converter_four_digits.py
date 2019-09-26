import pytest

from converter import converter

def test_converter_thousand():
  assert converter.int_to_roman_converter(1000) == "M"

def test_converter_two_thousand():
  assert converter.int_to_roman_converter(2000) == "MM"

def test_converter_two_thousand_four_hundred_fifty_nine():
  assert converter.int_to_roman_converter(2459) == "MMCDLIX"

def test_converter_one_thousand_nine_hundred_eighty_one():
  assert converter.int_to_roman_converter(1981) == "MCMLXXXI"

def test_converter_three_thousand_nine_hundred_ninety_nine():
  assert converter.int_to_roman_converter(3999) == "MMMCMXCIX"