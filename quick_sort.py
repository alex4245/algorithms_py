arr = [3,51,2,4,1,5,32,11]

def q_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr.pop()  
    less = [i for i in arr if i <= pivot]
    greater = [i for i in arr if i > pivot]
    return q_sort(less) + [pivot] + q_sort(greater)

print q_sort(arr)
