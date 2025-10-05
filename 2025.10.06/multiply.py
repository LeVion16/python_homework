def multiply(nums: tuple[int]) -> int:
    '''Összeszorozza a tuple elemeit, de ha 0-át talál akkor leáll és visszatér a pillanatnyi szorzattal'''
    amount = 1 # összeg
    for ch in nums:
        if ch == 0:
            return amount
        amount *= ch
    return amount

nums = (1, 4, 9, 10, 0, 13, 16)
print(multiply(nums))