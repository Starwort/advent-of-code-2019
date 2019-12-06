data = """102562
138390
145043
86679
120601
58443
54761
81175
127897
69559
56776
145671
69003
119334
130205
77249
74637
92068
66594
90485
140465
73444
107772
107639
144420
58764
56299
66010
84841
83686
139830
136298
135009
136506
61547
73653
136219
138875
95483
91695
146597
121813
131555
145848
139396
141520
54207
86748
98355
67179
59820
137299
92371
74512
110854
111960
63787
114701
63773
127377
128159
120370
138193
106409
135550
107235
56662
99314
69052
131816
138788
96494
73025
148907
85883
86138
86965
55645
119284
80690
69276
116640
108595
50721
94623
93224
137069
130118
97916
82232
137621
97909
74061
140419
101795
69316
64973
90578
118503
100369"""

ints = [int(i) for i in data.splitlines()]


def get_fuel(mass):
    rv = mass // 3 - 2
    if rv < 0:
        rv = 0
    if rv:
        rv += get_fuel(rv)
    return rv


# fmt: off
print(sum([i // 3 - 2 for i in ints])) or ((get_fuel_1l := lambda mass: ((rv := max(mass//3-2, 0)) + (get_fuel_1l(rv) if rv else 0))) and print(sum([get_fuel_1l(i) for i in ints])))
# print(sum([i // 3 - 2 for i in [int(i) for i in '<snip>'.splitlines()]])) or ((get_fuel_1l := lambda mass: ((rv := max(mass//3-2, 0)) + (get_fuel_1l(rv) if rv else 0))) and print(sum([get_fuel_1l(i) for i in [int(i) for i in '<snip>'.splitlines()]])))
# fmt: on
print(sum([i // 3 - 2 for i in ints])) or (
    (
        get_fuel_1l := lambda mass: (
            (rv := max(mass // 3 - 2, 0)) + (get_fuel_1l(rv) if rv else 0)
        )
    )
    and print(sum([get_fuel_1l(i) for i in ints]))
)

print(sum([i // 3 - 2 for i in ints]))
print(sum([get_fuel(i) for i in ints]))
