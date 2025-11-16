def division_by_3(nums: list) -> int:
    count = 0
    for n in nums:
        if n // 3 == 0:
            count += 1
        return count if count > 0 else -1

nums = [1, 3, 9, 10, 12, 20]
print(division_by_3(nums))


print()


def get_list_num(list: list[int]) -> int: return len(list)

list = [1, 2, 3, 4, 5]
print(get_list_num(list))