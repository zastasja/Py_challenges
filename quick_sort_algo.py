# quick sorting быстрая сортировка
s = list(map(int, input().split()))
def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    right = list(filter(lambda x: x > elem, s))
    center = [i for i in s if i == elem]

    return quick_sort(left) + center + quick_sort(right)
