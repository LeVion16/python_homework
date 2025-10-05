def is_even(nums: tuple[int]) -> int:
    '''osztható-e 2-vel'''
    count = 0
    for ch in nums: 
        if ch % 2 == 0: count += 1
    return count if count > 0 else -1

nums = (1, 4, 7, 8, 10, 13, 16)
print(is_even(nums))