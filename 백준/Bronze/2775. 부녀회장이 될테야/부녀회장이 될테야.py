for i in range(int(input())):
    count = 0
    k = int(input())
    n = int(input())
    arr = [i for i in range(1, 15)]
    while(count != k):
        newArr = []
        count += 1
        for j in range(1, 15):
            newArr.append(sum(arr[:j]))
        arr = newArr
    print(arr[n-1])