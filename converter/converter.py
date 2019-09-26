def int_to_roman_converter(numeral):
  if type(numeral) is int:
    if numeral > 0:
      return "I" * numeral
    else:
      return "Please insert integer greater than 0"
  else:
    return "Please enter valid integers greater than 0 only"