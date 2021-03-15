# https://skillsmart.ru/algo/15-121-cm/oac89ac8i9.html

def depth_calc(length_arr, i=0):
    depth = 2**(i+1)-1
    if length_arr > depth:
        return depth_calc(length_arr, i+1)
    return depth

def FindKeyIndex(tree, key, i=0):
    if i >= len(tree):
        return None
    elif tree[i] is None:
        return -i
    if key < tree[i]:
        return FindKeyIndex(tree, key, 2*i+1)
    elif tree[i] == key:
        return i
    else:
        return FindKeyIndex(tree, key, 2*i+2)

def AddKey(tree, key):
    i = FindKeyIndex(tree, key)
    if i is not None:
        if i <= 0 and tree[i] != key:
            i = -i
            tree[i] = key
    else:
        i = -1
    return i

def GenerateTreeArray(tree, arr):
    if len(arr):
        i = (len(arr)-1)//2
        AddKey(tree, arr[i])
        GenerateTreeArray(tree, arr[:i])
        GenerateTreeArray(tree, arr[i+1:])
    return tree

def GenerateBBSTArray(arr):
    arr = sorted(arr)
    tree = [None] * depth_calc(len(arr))
    return GenerateTreeArray(tree, arr)
