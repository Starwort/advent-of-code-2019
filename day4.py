input = "136760-595730"
input_range = range(136760, 595731)
import re

valid_pass = 0


def is_ascending(i: str):
    highest = 0
    for j in i:
        if int(j) >= highest:
            highest = int(j)
        else:
            return False
    return True


def has_matching(i: str):
    last_char = ""
    run = 0
    for j in i:
        if j != last_char:
            if run == 1:
                return True
            last_char = j
            run = 0
        else:
            run += 1
    if run == 1:
        return True
    return False


for i in input_range:
    if re.match(".*(00|11|22|33|44|55|66|77|88|99).*", str(i)) and is_ascending(str(i)):
        valid_pass += 1
print(valid_pass)
valid_pass = 0
for i in input_range:
    if has_matching(str(i)) and is_ascending(str(i)):
        valid_pass += 1
print(valid_pass)
