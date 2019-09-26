def int_to_roman_converter(numeral):
  if type(numeral) is int:
    if numeral > 0:
      return convert(numeral)
    else:
      return "Please insert integer greater than 0"
  else:
    return "Please enter valid integers greater than 0 only"

def convert(numeral):
  result_list = []
  quotient_ten = numeral // 10
  result_list.append("X" * quotient_ten)
  remainder_ten = numeral % 10
  if remainder_ten == 9:
    result_list.append("IX")
  else:
    quotient_five = remainder_ten // 5
    remainder_five = remainder_ten % 5
    if remainder_five == 4:
      result_list.append("IV")
    else:
      result_list.append(("V" * quotient_five) + ("I" * remainder_five))
  return ''.join(result_list)
    