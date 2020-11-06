
# %%

def fib(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

# %%


def fib(n):
    i = 0
    next = 1
    present = 1
    previous = 0

    while i < n:
        next = present + previous
        present = previous
        previous = next
        i += 1

    return next


fib(4444)

# %%


def mergesort(lst):

    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2

    left = lst[0:middle]
    right = lst[middle:len(lst)]

    return merge(mergesort(left), mergesort(right))


mergesort([3, 2, 1, 33, 2, 5, 3, 21, 2])

# %%


def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if len(left) == 0:
        result += right
    else:
        result += left

    return result


merge([1, 2, 3], [4, 5, 6])
#merge([5, 7, 9], [4, 5, 6])
#merge([5], [4])

# %%
