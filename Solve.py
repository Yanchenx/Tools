# 正整数解， 非负整数解的话只需要改变循环的上下限即可
def solve(factors, sum):
    if len(factors) == 1: # 只剩一个元了，计算结束
        if sum % factors[0] == 0: # 得到正整数解并返回
            return [[sum // factors[0]]]
        else: # 没有正整数解，返回一个方便辨识的值
            return 0
    t = [] # 用于把所有解整合在一起
    # 默认不会有系数为0，如果有在录入的时候就可以直接删掉了，且如果有那么结果也会爆掉
    # 一个元素的取值为[1, 和 // 系数]，且当和 // 系数为整数值时，右边取不到（剩下的和必然要大于0）
    if sum % factors[-1] == 0:
        max = sum // factors[-1] - 1
    else:
        max = sum // factors[-1]
    for i in range(1, max + 1): # 遍历最后一个元素可以取到的所有值
        x = solve(factors[:-1], sum - i * factors[-1]) # 递归，删去最后一个元素
        if x != 0: # 当删去元素有解时，将原定的最后一个元素补上即可
            for j in x:
                j.append(i)
                t.append(j) # 全部整合进t里，最后返回，因为每次要返回的不止是同一个i下的元素
        else:
            continue
    return t # 如果是空列表，比较与0是否不等还是会返回True，因此不会产生其他问题

print(solve([1, 1, 1, 1], 10))
