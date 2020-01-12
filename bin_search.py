arr = [i for i in range(100)]
N = input('Enter nubmer (0-100): ')
c = 0

def search_in_arr(arr):
    global c
    c += 1
    middle = len(arr) / 2
    if arr[middle] == N:
        print arr[middle]
        return

    if N >= arr[middle]:
        search_in_arr(arr[middle:])
    else:
        search_in_arr(arr[:middle])


search_in_arr(arr)
print c
