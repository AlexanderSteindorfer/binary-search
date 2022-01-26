import random


def binary_search(numbers_list, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if target == numbers_list[mid]:
        return mid
    elif target < numbers_list[mid]:
        return binary_search(numbers_list, target, left, mid-1)
    else:
        return binary_search(numbers_list, target, mid+1, right)


def test_binary_search():
    """Example for demonstration. The randomly generated list will stay the same.
    Adapt search_target to any number you want to search for.
    """

    numbers = []
    search_target = 8

    random.seed("RandomSeed")

    for _ in range(1000):
        numbers.append(random.randint(0, 1000))

    numbers.sort()

    if binary_search(numbers, search_target, 0, len(numbers)-1) >= 0:
        print("Number", search_target, "found!\nIndex:", binary_search(numbers, search_target, 0, len(numbers) - 1))
    else:
        print(search_target, "not found!")


if __name__ == '__main__':
    test_binary_search()
