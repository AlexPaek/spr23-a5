#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Divison check: checks that the program outputs "11" for an input of "44 / 4"
assert run("44 / 4").output == "11"
# Subtraction check: checks that the program outputs "12" for an input of "15 - 3"
assert run("15 - 3").output == "12"
# Checks that the program fails (correctly errors) for input "2 % 4"
assert run("2 % 4").exit_status != 0

###

print("All tests passed!")