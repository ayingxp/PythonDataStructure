"""
选择排序:
搜索整个列表，每一次找到一个最小的位置
"""


def selectionSort(lyst):
    """
    :param lyst:
    :return:
    """
    for i in range(len(lyst)):
        minIndex = i
        for j in range(i, len(lyst)):
            if lyst[minIndex] > lyst[j]:
                minIndex = j
        if lyst[minIndex] != lyst[i]:
            lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]


if __name__ == "__main__":
    import random

    a = [random.randint(0, 100) for _ in range(20)]
    print(a)
    selectionSort(a)
    print(a)