import re

data = """5 LKQCJ, 1 GDSDP, 2 HPXCL => 9 LVRSZ
5 HPXCL, 5 PVJGF => 3 KZRTJ
7 LVRSZ, 2 GFSZ => 5 FRWGJ
9 ZPTXL, 5 HGXJH, 9 LQMT => 7 LVCXN
2 LQMT, 2 PVJGF, 10 CKRVN => 9 VWJS
2 VRMXL, 12 NBRCS, 2 WSXN => 7 GDSDP
1 CKRP => 8 TBHVH
1 SVMNB, 2 KZRTJ => 8 WKGQS
6 LKQCJ, 8 HPXCL, 7 MPZH => 1 BQPG
1 RCWL => 7 MPZH
4 FGCMS, 2 LQMT, 1 LKQCJ => 1 KTBRM
1 ZTCSK, 6 CXQB, 2 ZBZRT => 3 PVJGF
7 DBNLM => 9 ZBZRT
5 BGNQ, 2 WBPD, 5 KTBRM => 9 GFSZ
6 XQBHG, 1 GPWVC => 8 CKFTS
1 XWLQM, 29 XQBHG, 7 KPNWG => 5 BXVL
6 TBHVH, 1 KTBRM => 7 HJGR
1 LQMT, 14 KPNWG => 7 GPWVC
18 LVCXN, 8 XVLT, 4 KPNWG, 13 LKQCJ, 12 MFJFW, 5 GZNJZ, 1 FLFT, 7 WBPD => 8 KZGD
1 TBHVH => 1 VWKJ
118 ORE => 2 CKRP
2 LTCQX => 3 XQBHG
1 GPWVC => 4 SMFQ
6 CKRP => 4 RCWL
39 LHZMD, 15 CKFTS, 26 HVBW, 57 KTBRM, 13 DFCM, 30 KZGD, 35 FPNB, 1 LKQCJ, 45 HJGR, 22 RCZS, 34 VWKJ => 1 FUEL
1 BQPG, 2 BGNQ, 12 WBPD => 8 LTCQX
2 WSXN => 2 HPXCL
3 GRFPX => 5 XVLT
1 LVRSZ => 3 SVMNB
6 HLMT => 9 ZPTXL
20 GFSZ => 5 GZNJZ
1 RCWL => 9 KPNWG
24 BGNQ, 31 KTBRM => 8 FLFT
14 VSVG => 9 DBNLM
191 ORE => 8 CXQB
115 ORE => 2 SWVLZ
17 KZRTJ, 13 KPNWG => 7 CKRVN
9 BQPG => 4 XWLQM
4 SMFQ, 2 GRFPX => 1 MFJFW
6 CXQB, 4 CKRP, 2 BXVL, 5 GZNJZ, 3 VWJS, 1 FLFT, 4 KPNWG => 7 DFCM
1 TBHVH => 6 BGNQ
3 LQMT => 7 HLMT
11 GDSDP => 4 WBPD
2 KPNWG, 5 VWJS, 33 NBRCS => 7 NVDW
5 GDSDP => 6 FGCMS
1 GPWVC, 7 BGNQ, 1 FRWGJ => 8 GRFPX
23 KTBRM, 11 VRMXL, 6 GPWVC => 5 SRJHK
2 XQBHG, 1 GZNJZ => 3 HVBW
1 ZTCSK => 4 WSXN
1 XVLT, 5 HLMT, 1 ZPTXL, 2 HVBW, 7 NVDW, 1 WKGQS, 1 LTCQX, 5 MPZH => 3 FPNB
16 SRJHK => 6 DWBW
1 SVMNB, 1 VRMXL => 3 HGXJH
133 ORE => 6 VSVG
3 NBRCS, 1 FGCMS => 4 LQMT
1 CKRP => 4 ZTCSK
5 CKRVN, 1 FLFT => 1 RCZS
4 ZTCSK, 15 RCWL => 9 LKQCJ
1 SWVLZ => 8 NBRCS
5 CKRP, 14 CXQB => 5 VRMXL
1 SMFQ, 1 DWBW => 2 LHZMD""".splitlines()
# data = """171 ORE => 8 CNZTR
# 7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
# 114 ORE => 4 BHXH
# 14 VRPVC => 6 BMBT
# 6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
# 6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
# 15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
# 13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
# 5 BMBT => 4 WPTQ
# 189 ORE => 9 KTJDG
# 1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
# 12 VRPVC, 27 CNZTR => 2 XDBXC
# 15 KTJDG, 12 BHXH => 5 XCVML
# 3 BHXH, 2 VRPVC => 7 MZWV
# 121 ORE => 7 VRPVC
# 7 XCVML => 6 RJRHP
# 5 BHXH, 4 VRPVC => 5 LTCX""".splitlines()
from math import ceil
from collections import defaultdict

pattern = re.compile(r"(\d+) (\w+)")
recipes = [[[item for item in pattern.findall(line)]] for line in data]

for reaction in recipes:
    for index, item in enumerate(reaction[0]):
        reaction[0][index] = (int(item[0]), item[1])
    reaction.append(reaction[0].pop())

leftover_ingredients = defaultdict(int)
float_leftover_ingredients = defaultdict(int)


def ingredients_for(quantity, product):
    recipe = [i for i in recipes if i[1][1] == product][0]
    ingredients, product_tuple = recipe
    product_quantity = product_tuple[0]
    recipe_times = ceil(quantity / product_quantity)
    adjusted_ingredients = [
        (i[0] * recipe_times - leftover_ingredients[i[1]], i[1]) for i in ingredients
    ]
    final = []
    for i, material in adjusted_ingredients:
        leftover_ingredients[material] = 0
        if i < 0:
            leftover_ingredients[material] = -i
        else:
            final.append((i, material))
    if product_quantity * recipe_times > quantity:
        leftover_ingredients[product] += product_quantity * recipe_times - quantity
    return final


def float_ingredients_for(quantity, product):
    recipe = [i for i in recipes if i[1][1] == product][0]
    ingredients, product_tuple = recipe
    product_quantity = product_tuple[0]
    recipe_times = quantity / product_quantity
    adjusted_ingredients = [
        (i[0] * recipe_times - float_leftover_ingredients[i[1]], i[1])
        for i in ingredients
    ]
    final = []
    for i, material in adjusted_ingredients:
        float_leftover_ingredients[material] = 0
        if i < 0:
            float_leftover_ingredients[material] = -i
        else:
            final.append((i, material))
    if product_quantity * recipe_times > quantity:
        float_leftover_ingredients[product] += (
            product_quantity * recipe_times - quantity
        )
    return final


def calculate_ore(fuel_amount=1):
    ore = 0
    to_calculate = defaultdict(int)
    to_calculate.update({"FUEL": fuel_amount})

    while to_calculate:
        material = list(to_calculate.keys())[0]
        amount = to_calculate.pop(material)
        # print("produce", material, amount)
        # print(leftover_ingredients)
        ingredients = ingredients_for(amount, material)
        # print("need", ingredients)
        for i in ingredients:
            if i[1] == "ORE":
                ore += i[0]
            else:
                to_calculate[i[1]] += i[0]
    return ore


def calculate_ore_float(fuel_amount=1):
    ore = 0
    to_calculate = defaultdict(int)
    to_calculate.update({"FUEL": fuel_amount})

    while to_calculate:
        material = list(to_calculate.keys())[0]
        amount = to_calculate.pop(material)
        # print("produce", material, amount)
        # print(leftover_ingredients)
        ingredients = float_ingredients_for(amount, material)
        # print("need", ingredients)
        for i in ingredients:
            if i[1] == "ORE":
                ore += i[0]
            else:
                to_calculate[i[1]] += i[0]
    return ore


if __name__ == "__main__":
    print(calculate_ore())

    AVAILABLE_ORE = 1000000000000
    max_fuel = int(AVAILABLE_ORE / ceil(calculate_ore_float()))
    leftover_ingredients.clear()
    while calculate_ore(max_fuel + 1) <= AVAILABLE_ORE:
        max_fuel += 1
        leftover_ingredients.clear()
    print(int(max_fuel))