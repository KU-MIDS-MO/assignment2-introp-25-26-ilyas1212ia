def has_adjacent_duplicate(L):

    if len(L) <= 1:
        return False

    for i in range (len(L)-1):
        if L[i] == L[i+1]:
            return True
    
    return False

print(has_adjacent_duplicate([1, 2, 2, 3]))
print(has_adjacent_duplicate([3, 4, 2, 3]))

