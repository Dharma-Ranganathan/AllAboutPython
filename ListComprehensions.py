"""
understanding list comprehension

make a new list contains,
- a price copy
- price greater than 2000
- price greater than 2000 else "less valued"
"""

price = [2000,3000,5000,1000,1500]

# making a copy
price_copy = [p for p in price]
print(price_copy)

# price > 2000
price_gt_2000 = [p for p in price if p > 2000]
print(price_gt_2000)

# price > 2000 else "less valued"
price_else = [p if p > 2000 else "less valued" for p in price]
print(price_else)
