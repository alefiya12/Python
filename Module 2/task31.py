# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# o Expected Output: Counter ({'item1': 1150, 'item2': 300})
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined_values = {}

for entry in data:
    item = entry['item']
    amount = entry['amount']
    
    # Check if the item is already in the combined_values dictionary
    if item in combined_values:
        combined_values[item] += amount
    else:
        combined_values[item] = amount

print("Combined values:", combined_values)