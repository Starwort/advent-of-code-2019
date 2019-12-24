from math import ceil
import itertools

data = [
    int(i)
    for i in "59772698208671263608240764571860866740121164692713197043172876418614411671204569068438371694198033241854293277505547521082227127768000396875825588514931816469636073669086528579846568167984238468847424310692809356588283194938312247006770713872391449523616600709476337381408155057994717671310487116607321731472193054148383351831456193884046899113727301389297433553956552888308567897333657138353770191097676986516493304731239036959591922009371079393026332649558536888902303554797360691183681625604439250088062481052510016157472847289467410561025668637527408406615316940050060474260802000437356279910335624476330375485351373298491579364732029523664108987"
]
data2 = data.copy() * 10000


def calculate_fft(input_array):
    output_array = []
    length = len(input_array)
    for i in range(1, length + 1):
        pattern = itertools.cycle([0] * i + [1] * i + [0] * i + [-1] * i)
        next(pattern)
        output_array.append(
            abs(sum(item * mult for item, mult in zip(input_array, pattern))) % 10
        )
    return output_array


output_array = data

for i in range(100):
    output_array = calculate_fft(output_array)

print(output_array[:8])

offset = int("".join(str(i) for i in data[:7]))

data2 = data2[offset:]  # because all positions before output are 0

for i in range(100):
    rev_sum = data2[-1:]

    for i in data2[-2::-1]:
        rev_sum.append(rev_sum[-1] + i)

    data2 = [abs(i) % 10 for i in reversed(rev_sum)]

print(data2[:8])
