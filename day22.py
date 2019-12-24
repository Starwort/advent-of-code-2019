data = """deal into new stack
cut -2732
deal into new stack
deal with increment 57
cut 5974
deal into new stack
deal with increment 32
cut -1725
deal with increment 24
cut 6093
deal with increment 6
cut -2842
deal with increment 14
cut 2609
deal with increment 12
cut -6860
deal with increment 51
cut -6230
deal with increment 61
cut 3152
deal with increment 28
cut 2202
deal into new stack
deal with increment 60
cut 433
deal into new stack
cut -6256
deal with increment 13
deal into new stack
cut 8379
deal into new stack
deal with increment 54
cut 1120
deal with increment 16
cut -5214
deal with increment 63
deal into new stack
cut -8473
deal with increment 11
cut 228
deal with increment 45
cut -6755
deal with increment 50
cut -3391
deal with increment 44
cut -1341
deal with increment 28
cut -6788
deal with increment 52
cut 3062
deal with increment 41
cut 4541
deal with increment 57
cut -7962
deal with increment 56
cut 9621
deal with increment 57
cut 3881
deal with increment 36
deal into new stack
deal with increment 45
cut 522
deal with increment 9
deal into new stack
deal with increment 60
deal into new stack
deal with increment 12
cut -9181
deal with increment 63
deal into new stack
deal with increment 14
cut -2906
deal with increment 10
cut 848
deal with increment 75
cut 798
deal with increment 29
cut 1412
deal with increment 10
deal into new stack
cut -5295
deal into new stack
cut 4432
deal with increment 72
cut -7831
deal into new stack
cut 6216
deal into new stack
deal with increment 7
cut -1720
deal into new stack
cut -5465
deal with increment 70
cut -5173
deal with increment 7
cut 3874
deal with increment 65
cut 921
deal with increment 8
cut -3094""".splitlines()

import re

deal_inc = re.compile(r"deal with increment (\d+)")
deal_new = re.compile(r"deal into new stack")
cut = re.compile(r"cut (-?\d+)")

instructions = [
    [1, int(match.group(1))]
    if (match := cut.match(instruction))
    else (
        [2, int(match.group(1))] if (match := deal_inc.match(instruction)) else [3, 0]
    )
    for instruction in data
]

deck_len = 10007

deck = list(range(deck_len))
for instruction in data:
    if match := deal_new.match(instruction):
        deck = deck[::-1]
    elif match := deal_inc.match(instruction):
        step = int(match.group(1))

        new_deck = deck.copy()
        pos = 0
        while deck:
            new_deck[pos] = deck.pop(0)
            pos += step
            pos %= len(new_deck)
        deck = new_deck
        # print(deck)
    elif match := cut.match(instruction):
        value = int(match.group(1))
        deck = deck[value:] + deck[:value]
    else:
        print(instruction)
        exit()
print(deck.index(2019))

# part 2: number theory!
# deck[n] = increment*n + offset
# now what are increment and offset

# new stack:
# - increment = -increment (because we've just reversed the list direction)
# - offset += increment (so that the first number moves and the new second is first)

# cut a:
# when going back, a=-a
# - card a becomes card 0
# - to move a to beginning, offset = increment*a + offset
# - offset += increment * a

# deal inc a:
# - increment *= a
# aka card i -> i*a
# new card 1 = i*a
# where did it start?
# - i
# i = 1/a = a ** (-1)
# modular inverse (thanks number theory)
# - increment *= modular inverse(a)
# modular inverse(a) = pow(a,base-2,base)
# base = deck_len = 119315717514047
# inverse(a) = pow(a, 119315717514045, 119315717514047)
# - increment *= pow(a, 119315717514045, 119315717514047)

# after one pass:
# increment *= a
# offset += b*increment at that step
#           some n of previous increment
# odiff = offset after one pass from =0 (summative identity)
# idiff = increment after one pass from =1 (multiplicative identity)
# one pass:
# - offset += increment * odiff
# - increment *= idiff
# increment being multiplied by a number repeatedly - exponentiation
# increment = idiff ** number % 119315717514047 (if we go more than one deck at once we could stay put)
#           = pow(idiff, number, 119315717514047)
# offset depends on increment
# offset = 0
#        = 0 + 1*odiff
#        = 0 + 1*odiff + idiff*odiff
#        = 0 + 1*odiff + idiff*odiff + (idiff**2)*odiff
#        = 0 + odiff*(idiff**0+idiff**1 + ... + idiff**(n-2) + idiff**(n-1))
# geometric series
# https://en.wikipedia.org/wiki/Geometric_series
# a+ar+ar**2+...+ar**n-1
#                       = a * (1-r**n)/(1-r) if r != 1
# r = idiff
# a = odiff
# offset = odiff * (1 - pow(idiff, number, 119315717514047) * pow(1-idiff, 119315717514045, 119315717514047))
# calculate diffs

deck_len = 119315717514047
times = 101741582076661
offset, increment = (0, 1)

for instruction in data:
    if match := deal_new.match(instruction):
        increment *= -1
        increment %= deck_len
        offset += increment
        offset %= deck_len
    elif match := deal_inc.match(instruction):
        increment *= pow(int(match.group(1)), deck_len - 2, deck_len)
        increment %= deck_len
    elif match := cut.match(instruction):
        offset += increment * int(match.group(1))
        offset %= deck_len

final_inc = pow(increment, times, deck_len)
final_off = offset * (
    (1 - pow(increment, times, deck_len)) * pow(1 - increment, deck_len - 2, deck_len)
)

print((2020 * final_inc + final_off) % deck_len)
