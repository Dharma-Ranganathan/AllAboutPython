"""
understanding dictionary comprehension

product with price

- product copy
- price higher than 350 product names
- price higher than 350 else 'no discount'
"""

products = {
    'ssd':4000,
    'os': 350,
    'pc':10000
}

# making a copy
products_copy = {k:v for (k,v) in products.items()}
print(products_copy)

# price higher than 2000 product names
products_gt_2000 = {k for (k,v) in products.items() if v >350}
print(products_gt_2000)

# price higher than 350 else "no discount"
product_discounted = {k:"discount" if v>350 else "no discount" for (k,v) in products.items()}
print(product_discounted)
