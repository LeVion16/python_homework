def division_by_3(nums: tuple[int]) -> int:
    '''Visszadobja a tuple első olyan elemének indexét, amely osztható 3-mal.'''
    i = 0
    while i < len(nums):
        if nums[i] % 3 == 0:
            return i
        i += 1
    return -1  # ha nincs 3-mal osztható elem

nums = (1, 4, 9, 10, 11, 13, 16)