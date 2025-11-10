def swap_ends(L, k):

    if k <= 0 or len(L) == 0 or k > len(L)//2:
        return (L.copy(), 0)
    new_list = L.copy()
    first_part = L[:k]
    last_part = L[-k:]
    new_list[:k] = last_part
    new_list[-k:] = first_part
    return (new_list, k)

print(swap_ends([1, 2, 3, 4, 5, 6], 2))