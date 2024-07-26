# Combine Two Dictionaries Adding Values for Common Keys
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}
print(combined_dict)