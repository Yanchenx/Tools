# 对数组进行快速排序，并删去相同的元素
# 输入值：数组、初始索引、末尾索引、比较函数
# 对比较函数的要求：自行定义，需要确保前者较小时返回-1，前者较大时返回1，相等时返回任意不同于±1的值即可
# 以下的代码中，单#的为注释，双#的为debug过程中使用的代码

def sort(x, first, last, compare):
    ## print(str(first) + "→" + str(last))
    if first == last:
        return 0
    delete = 0 # 在这里删除了多少个元素
    comp = x[first] # 将要用来比较的元素，比它小的插入在first前面，比它大的插入在last-delete+1前面
    smaller = 0 # 比较后发现比较小的元素
    larger = 0 # 比较后发现比较大的元素
    for i in range(1, last - first + 1):
        toBeCompared = x[first + i - delete - larger] # 在之前删除的元素会使下标-1，
                                                        # 在之前插入到last-delete+1前面的元素也会使下标-1
        c = compare(comp, toBeCompared)
        if c == -1: # 比较大
            x.insert(last - delete + 1, toBeCompared)
            del x[first + i - delete - larger]
            larger += 1
            # 先插入再删除，如果先删除，则插入在last-delete前即可
            ## print(str(c) + ":")
            ## print(x)
        elif c == 1: # 比较小
            del x[first + i - delete - larger]
            x.insert(first, toBeCompared)
            smaller += 1
            ## print(str(c) + ":")
            ## print(x)
            # 先删除再插入，如果先插入，则删除x[first+i-delete-larger+1]即可
        else: # 一样大
            del x[first + i - delete - larger]
            delete += 1
            ## print(str(c) + ":")
            ## print(x)
        # 无论怎么操作，在操作结束之后，原本在这个数组元素前面的还会在这个数组前面，原本在后面的也还会在后面，
            # 只是删去了一部分的点
        # 至此，x[first:first+smaller-1]为小的部分，x[first+smaller+1,first+smaller+larger]为大的部分，此外删去了delete个元素
        # 且三种情况下larger+smaller+delete稳定++，故他们的和恰为last-first，所以first+smaller+larger=last-delete，下一个元素
            # x[last-delete+1]恰为删去前的x[last+1]
    a = 0
    if smaller > 0: # 因为可能没有更小的了
        a = sort(x, first, first + smaller -1, compare)
    b = 0
    if larger > 0: # 同理
        b = sort(x, first + smaller + 1 - a, first + smaller + larger - a, compare) # 这里会直接受到a的影响
    return a + b + delete # 返回所有在这期间删去的值


# 以下部分为示例/测试用代码

def com(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

x = [1, 1, 3, 3, 2, 2, 1, 5, 4, 4, 5, 6, 7, 6, 7, 6, 8, 8, 8, 1, 2, 3, 4, 4, 3, 2, 1, 100, 1.4, 100.]
sort(x, 0 ,len(x) - 1, com)
print(x)
