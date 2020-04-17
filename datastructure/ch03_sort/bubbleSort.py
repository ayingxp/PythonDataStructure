"""
所有的排序算法
"""

import random

# 冒泡排序
def bubbleSort(lyst):
    """
    每次迭代时都会产生一个最大的值
    :param lyst:
    :return:
    """
    for i in range(len(lyst)):  # 控制迭代的轮次
        for j in range(1, len(lyst) - i):  # 进行一次具体的排序, 每次排序完成之后会产生一个（最大值）的固定位置
            if lyst[j] < lyst[j-1]:
                lyst[j-1], lyst[j] = lyst[j], lyst[j-1]


if __name__ == "__main__":
    a = [5, 3, 1, 2, 4]
    a = [random.randint(0, 100) for _ in range(20)]
    print(a)
    bubbleSort(a)
    print(a)