"""
插入排序:
第i次排序时，前面的i-1个元素已经排好
"""

def insertSort1(lyst):
    res = []
    for i in lyst:
        if not res:
            res.append(i)
            continue
        for j in range(len(res)):
            if res[j] <= i:
                continue
            else:
                # res.insert(j, i)
                break
        if j == len(res) - 1 and res[j] <= i:
            res.insert(j+1, i)
        else:
            res.insert(j, i)
    return res


def insertSort(lyst):
    i = 1
    while i < len(lyst):   # 外循环，控制前i个数据有序
        itemToInsert = lyst[i]  # 哨兵单元，保存当前要插入的结点
        j = i - 1
        while j >= 0:  # 从后往前搜索插入位置
            if itemToInsert < lyst[j]:   # 如果当前位置的元素大于待插入的元素，则把当前元素往后移动
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert  # 把待插入元素插入到指定位置
        i += 1


if __name__ == "__main__":
    import random

    a = [random.randint(0, 100) for _ in range(10)]
    print(a)
    # res = insertSort1(a)
    insertSort(a)
    print(a)
