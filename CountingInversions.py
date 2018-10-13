# an implementation of counting number of inversions in an array  with O(nlogn) running time

def merge_and_count(left, right):
    ret_array = []
    invs = 0

    i = 0  # left index tracker
    j = 0  # right index tracker

    while i != len(left) and j != len(right):
        if left[i] <= right[j]:
            ret_array.append(left[i])
            i += 1
        else:
            ret_array.append(right[j])
            j += 1
            invs += len(left) - i

    if i == len(left):
        for temp in right[j:]:
            ret_array.append(temp)
    else:
        for temp in left[i:]:
            ret_array.append(temp)

    return ret_array, invs




def count_inversions(arry):
    if len(arry) == 1:
        return arry, 0

    mid = int(len(arry)/2)

    left_sorted, left_invs = count_inversions(arry[:mid])
    right_sorted, right_invs = count_inversions(arry[mid:])
    both_sorted, two_sided_invs = merge_and_count(left_sorted, right_sorted)

    total_inversions = left_invs + right_invs + two_sided_invs

    return both_sorted, total_inversions


a = [2, 4, 1, 3, 5]
b =count_inversions(a)

print("sorted array:", b[0], ", number of inversions: ", b[1])

