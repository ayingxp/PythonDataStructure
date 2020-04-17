"""
1. 首先，从列表中选取一项作为基准点(pivot)。
2. 将列表中的项分区, 将小于基准点的所有项都移动到基准点左边，将大于基准点的所有项都移动到基准点的右边。
3. 分而治之。对于在基准点分割列表形成的子列表，递归地重复调用该过程。
4. 每次遇到少于两个项的一个子列表，就结束这个过程.
"""

def partition(lyst, left, right):
    pivot = lyst[left]  # 第一个元素作为基准点

    while left <= right:
        if left == right:   # 当左右箭头指向同一元素时用基准点填充该值，并退出
            lyst[left] = pivot  # lyst[right] = pivot
            break
        while right > left:   # 先从右边往左搜寻，直到找到一个不大于基准点的数据，并用此数据填充当前的位置
            if lyst[right] <= pivot:
                lyst[left] = lyst[right]
                break
            else:
                right -= 1
        while left < right:  # 从左往右搜寻
            if lyst[left] > pivot:
                lyst[right] = lyst[left]
                break
            else:
                left += 1
    return left  # right


def quick_sort(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)  # 确定pivotLocation位置的元素
        quick_sort(lyst, left, pivotLocation-1)  # 递归排序pivot左边的元素
        quick_sort(lyst, pivotLocation+1, right)  # 递归排序pivot右边的元素




if __name__ == "__main__":
    import random
    a = [random.randint(1, 30) for _ in range(10)]
    # a = [21, 7, 20, 17, 21, 17, 9, 7, 30, 3]
    print(a)
    # partition(a, 0, len(a)-1)
    quick_sort(a, 0, len(a) - 1)
    print(a)