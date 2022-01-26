from binary_search_def import binary_search


numbers = []
numbers.sort()

search_target = 8


if binary_search(numbers, search_target, 0, len(numbers) - 1) >= 0:
    print("Number", search_target, "found!\nIndex:", binary_search(numbers, search_target, 0, len(numbers) - 1))
else:
    print(search_target, "not found!")