def int_to_roman_converter(numeral):
  if type(numeral) is int:
    if numeral > 0:
      return convert(numeral)
    else:
      return "Please insert integer greater than 0"
  else:
    return "Please enter valid integers greater than 0 only"

def convert(numeral):
  key_list = {50 : 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'}
  result_list = []
  for key,value in key_list.items():
    count = numeral // key
    result_list.append(value * count)
    numeral -= key * count
    
  return ''.join(result_list)
    