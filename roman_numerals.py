# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
def to_roman(num):
# 2. Create a OUTPUT string, set to ''
    output = ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
    ROMAN_NUMERAL_TO_ARABIC_MAP = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1,
    }
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
    for i in ROMAN_NUMERAL_TO_ARABIC_MAP:
        # print(i, ROMAN_NUMERAL_TO_ARABIC_MAP[i])
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
        EVENLY_DIVISIBLE_TIMES = int(num / ROMAN_NUMERAL_TO_ARABIC_MAP[i])
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
        if EVENLY_DIVISIBLE_TIMES >= 1:
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
            output += (i * EVENLY_DIVISIBLE_TIMES)
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
            num -= (ROMAN_NUMERAL_TO_ARABIC_MAP[i] * EVENLY_DIVISIBLE_TIMES)
            # print(num)
# 7. Return OUTPUT
    return output


print(to_roman(14))



# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
def to_roman(num):
# 2. Create a OUTPUT string, set to ''
    output = ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
    ROMAN_NUMERAL_TO_ARABIC_MAP = {
        "M" : 1000,
        "CMXLIV" : 944,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "XLIV" : 44,
        "XIV" : 14,
        "X" : 10,
        "IX" : 9,
        "V" : 5,
        "IV" : 4,
        "I" : 1,
    }
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
    for i in ROMAN_NUMERAL_TO_ARABIC_MAP:
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
        EVENLY_DIVISIBLE_TIMES = int(num / ROMAN_NUMERAL_TO_ARABIC_MAP[i])
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
        if EVENLY_DIVISIBLE_TIMES >= 1:
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
            output += (i * EVENLY_DIVISIBLE_TIMES)
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
            num -= (ROMAN_NUMERAL_TO_ARABIC_MAP[i] * EVENLY_DIVISIBLE_TIMES)
# 7. Return OUTPUT
    return output


print(to_roman(1554))