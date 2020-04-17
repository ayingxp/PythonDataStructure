"""
归并排序:
1. 计算一个列表的中间位置，并且递归地排序其左边和右边的子列表
2. 将两个排好序的子列表重新合并为单个的排好序的列表
3. 当子列表不能够再划分的时候，停止这个过程
"""

def merge_sort(lyst, left, right):
    mid = (left + right) // 2
    if left < right:   # 递归终止条件
        merge_sort(lyst, left, mid)  #  递归排序左半部分
        merge_sort(lyst, mid+1, right) # 递归排序右半部分
        merge(lyst, left, right)   # 归并左右两个有序列表

def merge(lyst, left,right):
    mid = (left + right) // 2
    tmp = []
    llst = lyst[left:mid+1]   # 左半部分的有序列表
    rlst = lyst[mid+1:right+1]  # 右半部分的有序列表
    li = 0
    ri = 0

    while li < len(llst) and ri < len(rlst):
        if llst[li] <= rlst[ri]:
            tmp.append(llst[li])
            li += 1
        else:
            tmp.append(rlst[ri])
            ri += 1

    while li < len(llst):
        tmp.append(llst[li])
        li += 1

    while ri < len(rlst):
        tmp.append(rlst[ri])
        ri += 1

    lyst[left:right+1] = tmp  # 回写到lyst中，通过引用来在递归函数中传递值


if __name__ == "__main__":
    import random

    a = [random.randint(1, 50) for _ in range(10)]
    # a = [48, 19, 18, 28, 3, 4, 46, 41, 30, 27]
    print(a)
    merge_sort(a, 0, len(a)-1)
    print(a)