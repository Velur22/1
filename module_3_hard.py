data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data):
    sum_ = 0
    for item in data:
        if isinstance(item, set | tuple | list):
            sum_ += calculate_structure_sum(item)
        elif isinstance(item, dict):
            sum_ += calculate_structure_sum(item.items())
        elif isinstance(item, int | float):
            sum_ += item
        elif isinstance(item, str):
            sum_ += len(item)
    return sum_

result = calculate_structure_sum(data_structure)
print(result)





