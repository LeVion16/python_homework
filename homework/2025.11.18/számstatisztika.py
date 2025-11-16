import random as rr

def create_rnd_number() -> tuple:
    for n in range(100):
        nums = rr.randint(0,100)
    return nums

def nums_statistic() -> dict:
    nums = create_rnd_number()
    statistic = 0
    for n in str(nums):
        if int(n) > 50:
            statistic += 1
    print(f"50-nél kisebb számok: {nums - statistic} | 50-nél nagyobb számok: {statistic}")

nums_statistic()