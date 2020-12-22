import fileinput
from collections import Counter

def parse():
    foods = []
    for line in fileinput.input():
        l = line[:-1]
        ingredients, allergens = l.replace(')','').replace(' (',';').split(';contains ')
        allergens = allergens.replace(',','')
        foods.append((ingredients.split(' '), allergens.split(' ')))
    return foods

def part1(foods):
    orig_foods = list(foods)
    all_allergens = set()
    for ingredients,allergens in foods:
        for allergen in allergens:
            all_allergens.add(allergen)

    ingredient_allergens = {}
    while all_allergens:
        allergen_candidate_ingredients = {}
        for a in all_allergens:
            allergen_candidate_ingredients[a] = set()
            for ingredients,allergens in foods:
                if a in allergens:
                    ingredients_set = set(ingredients)
                    if not allergen_candidate_ingredients[a]:
                        allergen_candidate_ingredients[a] = ingredients_set
                    else:
                        allergen_candidate_ingredients[a] = allergen_candidate_ingredients[a].intersection(ingredients_set)

        for a,ingredients in allergen_candidate_ingredients.items():
            # print(a,i)
            if len(ingredients) == 1:
                # found the ingredient containing the allergen
                ingr = list(ingredients)[0]
                # print('found',a,ingr)
                ingredient_allergens[ingr] = a
                all_allergens.remove(a)
                for i in range(len(foods)):
                    ingrs,allergens = foods[i]
                    new_ingrs = [ing for ing in ingrs if ing != ingr]
                    new_allergens = [al for al in allergens if al != a]
                    foods[i] = (new_ingrs, new_allergens)
                break
    safe_ingrs = set()
    for f in foods:
        for ingr in f[0]:
            safe_ingrs.add(ingr)

    safe_count = 0
    for f in orig_foods:
        for ingr in f[0]:
            if ingr in safe_ingrs:
                safe_count += 1

    # Part 1
    print(safe_count)

    # Part 2
    s = dict(sorted(ingredient_allergens.items(), key=lambda item: item[1]))
    print(','.join(s.keys()))


foods = parse()
# print(foods)
part1(foods) # parts 1 and 2 printed inside of function

#
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
#
# mxmxvkd: {dairy, fish}
# kfcds: {dairy, fish}
# sqjhc: {dairy, fish}
# nhms: {dairy, fish}

# {dairy, fish, soy}
# dairy: intersection(any ingredients list that contains dairy) --> {mxmxvkd}
# fish: {sqjhc, mxmxvkd}
# soy: {sqjhc, fjvjkl}
#
# find the set that only has one --> dairy
# remove ingredient from all lists
# remove allergen from allergens set
# rerun allergen check
#
# {fish, soy}
# fish: {sqjhc}
# soy: {sqjhc, fjvjkl}
# remove fish from allergens and sqjhc from ingredients lists
#
# soy: {fjvkjl}
