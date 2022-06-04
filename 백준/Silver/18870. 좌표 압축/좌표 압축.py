n = int(input())
arr = list(map(int, input().split()))
sorted_arr = list(sorted(set(arr)))
dict_arr = dict(zip(sorted_arr, range(n)))
for i in arr:
    print(dict_arr[i], end=" ")