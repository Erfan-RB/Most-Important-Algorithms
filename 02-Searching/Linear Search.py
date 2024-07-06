#Linear Search
def search(a, l, x):
    for i in range(l):
        if (a[i] == x):
            return i
    return -1

a = [10, 8, 6, 4, 2]
print("The given array is ", a)
x = 6
print("Element to be searched is ", x)
l = len(a)
ind = search(a, l, x)
if(ind == -1):
    print("Element Not Found")
else:
    print("Element is at index ", ind)