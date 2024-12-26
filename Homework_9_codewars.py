# 5 kyu: Pete, the baker
# https://www.codewars.com/kata/525c65e51bf619685c000059/python

def cakes(recipe, available):
    total = {}

    for key, value in recipe.items():
        if not key in available:
            return 0
        elif available[key] < value:
            return 0
        else:
            total.setdefault(key, available[key] // value)

    count = min(total.values())
    return count


#5 kyu: The Hashtag Generator
# https://www.codewars.com/kata/52449b062fb80683ec000024/python

def generate_hashtag(s):
    s = list(map(lambda x: x.strip().capitalize(), s.split()))
    s = '#' + ''.join(s)
    return s if 1 < len(s) <= 140 else False


#5 kyu: First non-repeating character
# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/python

def first_non_repeating_letter(s):
    for i, el in enumerate(s):
        if s.lower().count(s.lower()[i]) == 1:
            return el
    return ''